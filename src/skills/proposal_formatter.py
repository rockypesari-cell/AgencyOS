"""
ProposalFormatterSkill - Formats proposals into professional HTML.

Input:  Proposal data dict (from ProposalAgent)
Output: Professional HTML string

Architecture:
    - This is a SKILL. Transformation/formatting only.
    - No business logic. No pricing decisions.
    - Later: PDF export, email templates, branding.
"""

from typing import Any, Dict
from datetime import datetime, timezone


class ProposalFormatterSkill:
    """Formats proposal data into professional HTML."""

    def __init__(self, agency_name: str = "AgencyOS", agency_email: str = "hello@agencyos.com"):
        self._agency_name = agency_name
        self._agency_email = agency_email

    def format_html(self, proposal_data: Dict[str, Any]) -> str:
        """
        Format proposal data into professional HTML.

        Args:
            proposal_data: Output from ProposalAgent.run()

        Returns:
            Complete HTML document string.
        """
        pricing = proposal_data.get("pricing", {})
        service = proposal_data.get("service", "unknown").replace("_", " ").title()
        price = proposal_data.get("suggested_price", 0)
        currency = proposal_data.get("currency", "USD")
        timeline = proposal_data.get("timeline", "5-7 days")
        status = proposal_data.get("status", "draft")
        proposal_text = proposal_data.get("proposal_text", "")
        date = datetime.now(timezone.utc).strftime("%B %d, %Y")
        proposal_id = f"PROP-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}"

        # Convert proposal text to HTML paragraphs
        paragraphs = proposal_text.split("\n")
        body_html = ""
        for p in paragraphs:
            p = p.strip()
            if not p:
                continue
            if p.isupper() and len(p) < 50:
                body_html += f'<h3 style="margin: 24px 0 8px 0; color: #1a1a2e;">{p}</h3>'
            else:
                body_html += f'<p style="margin: 8px 0; line-height: 1.7; color: #333;">{p}</p>'

        breakdown = pricing.get("breakdown", f"${price} {currency}")

        html = f"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proposal {proposal_id}</title>
</head>
<body style="margin: 0; padding: 0; background: #f5f5f5; font-family: 'Segoe UI', Arial, sans-serif;">

    <table width="100%" cellpadding="0" cellspacing="0" style="background: #f5f5f5; padding: 40px 0;">
        <tr>
            <td align="center">
                <table width="700" cellpadding="0" cellspacing="0" style="background: #ffffff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 24px rgba(0,0,0,0.08);">

                    <!-- Header -->
                    <tr>
                        <td style="background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); padding: 40px;">
                            <h1 style="margin: 0; color: #ffffff; font-size: 28px; font-weight: 700;">{self._agency_name}</h1>
                            <p style="margin: 8px 0 0 0; color: #a0a0b0; font-size: 14px;">Project Proposal</p>
                        </td>
                    </tr>

                    <!-- Meta -->
                    <tr>
                        <td style="padding: 24px 40px; border-bottom: 1px solid #eee;">
                            <table width="100%" cellpadding="0" cellspacing="0">
                                <tr>
                                    <td style="font-size: 13px; color: #888;">Proposal ID</td>
                                    <td align="right" style="font-size: 13px; color: #333; font-weight: 600;">{proposal_id}</td>
                                </tr>
                                <tr>
                                    <td style="font-size: 13px; color: #888; padding-top: 4px;">Date</td>
                                    <td align="right" style="font-size: 13px; color: #333; padding-top: 4px;">{date}</td>
                                </tr>
                                <tr>
                                    <td style="font-size: 13px; color: #888; padding-top: 4px;">Status</td>
                                    <td align="right" style="font-size: 13px; padding-top: 4px;">
                                        <span style="background: #fff3cd; color: #856404; padding: 2px 10px; border-radius: 12px; font-size: 12px; font-weight: 600;">{status.upper()}</span>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Body -->
                    <tr>
                        <td style="padding: 32px 40px;">
                            {body_html}
                        </td>
                    </tr>

                    <!-- Pricing Box -->
                    <tr>
                        <td style="padding: 0 40px 32px 40px;">
                            <table width="100%" cellpadding="0" cellspacing="0" style="background: #f8f9fa; border-radius: 8px; border: 1px solid #e9ecef;">
                                <tr>
                                    <td style="padding: 24px;">
                                        <h3 style="margin: 0 0 16px 0; font-size: 16px; color: #1a1a2e;">Investment Summary</h3>
                                        <table width="100%" cellpadding="0" cellspacing="0">
                                            <tr>
                                                <td style="font-size: 14px; color: #666; padding: 4px 0;">Service</td>
                                                <td align="right" style="font-size: 14px; color: #333; padding: 4px 0;">{service}</td>
                                            </tr>
                                            <tr>
                                                <td style="font-size: 14px; color: #666; padding: 4px 0;">Timeline</td>
                                                <td align="right" style="font-size: 14px; color: #333; padding: 4px 0;">{timeline}</td>
                                            </tr>
                                            <tr>
                                                <td style="font-size: 14px; color: #666; padding: 4px 0;">Pricing</td>
                                                <td align="right" style="font-size: 14px; color: #333; padding: 4px 0;">{breakdown}</td>
                                            </tr>
                                            <tr>
                                                <td colspan="2" style="border-top: 2px solid #dee2e6; padding-top: 12px; margin-top: 8px;">
                                                    <table width="100%" cellpadding="0" cellspacing="0">
                                                        <tr>
                                                            <td style="font-size: 18px; font-weight: 700; color: #1a1a2e;">Total</td>
                                                            <td align="right" style="font-size: 24px; font-weight: 700; color: #2d6a4f;">${price} {currency}</td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- CTA -->
                    <tr>
                        <td style="padding: 0 40px 32px 40px;" align="center">
                            <a href="mailto:{self._agency_email}?subject=Proposal {proposal_id} - Approved"
                               style="display: inline-block; background: #2d6a4f; color: #ffffff; text-decoration: none; padding: 14px 40px; border-radius: 8px; font-size: 16px; font-weight: 600;">
                                Approve Proposal
                            </a>
                        </td>
                    </tr>

                    <!-- Footer -->
                    <tr>
                        <td style="background: #f8f9fa; padding: 24px 40px; border-top: 1px solid #eee;">
                            <p style="margin: 0; font-size: 12px; color: #999; text-align: center;">
                                {self._agency_name} &bull; {self._agency_email}<br>
                                This proposal is valid for 14 days from the date of issue.
                            </p>
                        </td>
                    </tr>

                </table>
            </td>
        </tr>
    </table>

</body>
</html>"""

        return html

    def format_plain_text(self, proposal_data: Dict[str, Any]) -> str:
        """Format proposal as plain text (for email body)."""
        pricing = proposal_data.get("pricing", {})
        service = proposal_data.get("service", "unknown").replace("_", " ").title()
        price = proposal_data.get("suggested_price", 0)
        currency = proposal_data.get("currency", "USD")
        timeline = proposal_data.get("timeline", "5-7 days")
        proposal_text = proposal_data.get("proposal_text", "")

        return f"""{self._agency_name.upper()} - PROJECT PROPOSAL
{'=' * 50}

{proposal_text}

{'=' * 50}
INVESTMENT SUMMARY
{'=' * 50}
Service:    {service}
Timeline:   {timeline}
Total:      ${price} {currency}
{'=' * 50}

To approve, reply to this email.

{self._agency_name}
{self._agency_email}
"""