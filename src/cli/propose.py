"""
CLI Revenue Tool - Generate proposals from the command line.

Usage:
    python -m cli.propose "Need a logo for my startup. Budget $500."
    python -m cli.propose --file lead.txt
    python -m cli.propose --service logo_design --summary "Modern logo" --priority high --client "John"
    python -m cli.propose --interactive

Output:
    - Prints summary to terminal
    - Saves HTML proposal to proposals/ folder
"""

import argparse
import os
import sys
from datetime import datetime, timezone

# Add src to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from skills.lead_parser import LeadParserSkill
from agents.proposal_agent import ProposalAgent
from services.pricing_service import PricingService
from skills.proposal_formatter import ProposalFormatterSkill


def ensure_output_dir():
    """Create proposals output directory if needed."""
    output_dir = os.path.join(os.getcwd(), "proposals")
    os.makedirs(output_dir, exist_ok=True)
    return output_dir


def run_pipeline(
    raw_text=None,
    service=None,
    summary=None,
    priority="normal",
    complexity="normal",
    client_name="Valued Client",
    rush=False,
    agency_name="AgencyOS",
    agency_email="hello@agencyos.com",
):
    """Run the full lead-to-proposal pipeline."""

    # Step 1: Parse or build lead data
    if raw_text:
        parser = LeadParserSkill()
        lead = parser.parse(raw_text)
        service = service or lead["service"]
        summary = summary or lead["summary"]
        priority = lead["priority"] if priority == "normal" else priority
        print(f"\n📋 Parsed Lead:")
        print(f"   Service:  {lead['service']}")
        print(f"   Priority: {lead['priority']}")
        print(f"   Budget:   {lead['budget'] or 'Not specified'}")
        print(f"   Confidence: {lead['confidence']:.0%}")
    else:
        lead = {
            "service": service or "unknown",
            "summary": summary or "",
            "priority": priority,
            "budget": None,
            "client_name": client_name,
            "confidence": 1.0,
        }

    # Step 2: Generate proposal
    pricing = PricingService()
    agent = ProposalAgent(pricing_service=pricing)
    result = agent.run({
        "service": service or lead.get("service", "unknown"),
        "summary": summary or lead.get("summary", ""),
        "priority": priority,
        "complexity": complexity,
        "client_name": client_name,
        "rush": rush,
    })

    if not result.get("success"):
        print(f"\n❌ Error: {result.get('error', 'Unknown error')}")
        return None

    # Step 3: Format HTML
    formatter = ProposalFormatterSkill(
        agency_name=agency_name,
        agency_email=agency_email,
    )
    html = formatter.format_html(result)

    # Step 4: Save
    output_dir = ensure_output_dir()
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    svc = (service or lead.get("service", "unknown")).replace(" ", "_")
    filename = f"proposal_{svc}_{timestamp}.html"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

    # Step 5: Print summary
    p = result.get("pricing", {})
    print(f"\n✅ Proposal Generated!")
    print(f"   Service:  {result['service'].replace('_', ' ').title()}")
    print(f"   Price:    ${result['suggested_price']} {result['currency']}")
    print(f"   Timeline: {result['timeline']}")
    print(f"   Breakdown: {p.get('breakdown', 'N/A')}")
    print(f"\n📄 Saved: {filepath}")
    print(f"\n💡 Open in browser to preview.")

    return filepath


def interactive_mode():
    """Interactive mode: ask questions, generate proposal."""
    print("\n🚀 AgencyOS Proposal Generator (Interactive)")
    print("=" * 50)

    raw = input("\nPaste lead text (or press Enter to skip): ").strip()

    if not raw:
        service = input("Service (logo_design, web_design, etc.): ").strip()
        summary = input("Summary: ").strip()
        priority = input("Priority (low/normal/high) [normal]: ").strip() or "normal"
        client = input("Client name [Valued Client]: ").strip() or "Valued Client"
        run_pipeline(
            service=service,
            summary=summary,
            priority=priority,
            client_name=client,
        )
    else:
        client = input("Client name [Valued Client]: ").strip() or "Valued Client"
        run_pipeline(raw_text=raw, client_name=client)


def main():
    parser = argparse.ArgumentParser(
        description="AgencyOS Proposal Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python -m cli.propose "Need a logo. Budget $500. Urgent!"
  python -m cli.propose --service web_design --summary "Company website" --priority high
  python -m cli.propose --file lead.txt
  python -m cli.propose --interactive
        """,
    )

    parser.add_argument("text", nargs="?", help="Raw lead text")
    parser.add_argument("--file", "-f", help="Read lead text from file")
    parser.add_argument("--service", "-s", help="Service type")
    parser.add_argument("--summary", "-m", help="Project summary")
    parser.add_argument("--priority", "-p", default="normal", choices=["low", "normal", "high"])
    parser.add_argument("--complexity", "-c", default="normal", choices=["simple", "normal", "complex", "enterprise"])
    parser.add_argument("--client", "-n", default="Valued Client", help="Client name")
    parser.add_argument("--rush", "-r", action="store_true", help="Apply rush fee")
    parser.add_argument("--agency", "-a", default="AgencyOS", help="Agency name")
    parser.add_argument("--email", "-e", default="hello@agencyos.com", help="Agency email")
    parser.add_argument("--interactive", "-i", action="store_true", help="Interactive mode")

    args = parser.parse_args()

    if args.interactive:
        interactive_mode()
        return

    raw_text = args.text

    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                raw_text = f.read()
        except FileNotFoundError:
            print(f"❌ File not found: {args.file}")
            sys.exit(1)

    if not raw_text and not args.service:
        parser.print_help()
        sys.exit(0)

    run_pipeline(
        raw_text=raw_text,
        service=args.service,
        summary=args.summary,
        priority=args.priority,
        complexity=args.complexity,
        client_name=args.client,
        rush=args.rush,
        agency_name=args.agency,
        agency_email=args.email,
    )


if __name__ == "__main__":
    main()