"""
LeadParserSkill - Extracts structured lead data from raw text.

Input:  Raw text (job post, email, LinkedIn post, message)
Output: Structured lead dictionary

Architecture:
    - This is a SKILL. Transformation/parsing only.
    - Uses LLM if available, regex fallback otherwise.
    - No business logic. No pricing. No proposals.
"""

import re
import json
from typing import Any, Dict, Optional


# ─── Service Keywords (ordered: specific first) ──────────────
SERVICE_KEYWORDS = {
    "logo_design": ["logo", "logotype", "brand mark", "icon design"],
    "brand_identity": ["brand identity", "branding", "brand guidelines", "visual identity", "rebrand"],
    "seo": ["seo", "search engine optimization", "ranking", "keywords"],
    "landing_page": ["landing page", "squeeze page", "sales page"],
    "web_design": ["website", "web design", "homepage", "ui design", "webflow"],
    "presentation": ["presentation", "pitch deck", "powerpoint", "keynote", "slide deck"],
    "illustration": ["illustration", "illustrator", "character design", "book illustration"],
    "social_media_pack": ["social media pack", "social media kit", "social templates"],
    "social_media": ["social media", "instagram", "facebook", "twitter", "linkedin", "tiktok", "social post"],
    "poster": ["poster", "flyer", "banner", "print design"],
    "brochure": ["brochure", "catalog", "booklet", "pamphlet"],
    "motion_graphics": ["motion graphics", "motion design", "after effects"],
    "video": ["video", "animation", "motion", "reel", "promo video", "explainer"],
    "content_writing": ["content", "copywriting", "blog", "article", "text", "writing"],
    "translation": ["translation", "translate", "localization"],
}

# ─── Budget Patterns ─────────────────────────────────────────
BUDGET_PATTERNS = [
    r"\$\s*(\d[\d,]*)",
    r"(\d[\d,]*)\s*(?:usd|eur|dollars?)",
    r"budget\s*(?::?\s*)\$?\s*(\d[\d,]*)",
    r"(?:pay|paying|offer)\s*(?::?\s*)\$?\s*(\d[\d,]*)",
]

# ─── Priority Keywords ───────────────────────────────────────
# LOW checked FIRST to catch "no rush" before "rush"
LOW_PRIORITY = ["no rush", "flexible", "whenever", "low priority", "someday", "no hurry"]
HIGH_PRIORITY = ["urgent", "asap", "immediately", "rush", "deadline", "yesterday", "critical"]


class LeadParserSkill:
    """Parses raw text into structured lead data."""

    def __init__(self, llm_service=None):
        self._llm = llm_service

    def parse(self, raw_text: str) -> Dict[str, Any]:
        """
        Parse raw text into structured lead data.

        Args:
            raw_text: The raw input text.

        Returns:
            Structured lead dictionary.
        """
        if not raw_text or not raw_text.strip():
            return {
                "service": "unknown",
                "summary": "",
                "priority": "normal",
                "budget": None,
                "client_name": None,
                "confidence": 0.0,
                "raw_text": "",
            }

        text = raw_text.strip()

        # Try LLM first
        if self._llm:
            try:
                return self._parse_with_llm(text)
            except Exception:
                pass

        # Fallback: regex/keyword parsing
        return self._parse_with_rules(text)

    def _parse_with_rules(self, text: str) -> Dict[str, Any]:
        """Rule-based parsing fallback."""
        lower = text.lower()

        # Detect service (ordered dict: specific first)
        service = "unknown"
        confidence = 0.0
        for svc, keywords in SERVICE_KEYWORDS.items():
            for kw in keywords:
                if kw in lower:
                    service = svc
                    confidence = 0.7
                    break
            if service != "unknown":
                break

        # Detect budget
        budget = None
        for pattern in BUDGET_PATTERNS:
            match = re.search(pattern, lower)
            if match:
                budget = int(match.group(1).replace(",", ""))
                break

        # Detect priority (LOW first to catch "no rush" before "rush")
        priority = "normal"
        for kw in LOW_PRIORITY:
            if kw in lower:
                priority = "low"
                break
        if priority == "normal":
            for kw in HIGH_PRIORITY:
                if kw in lower:
                    priority = "high"
                    break

        # Extract summary (first 200 chars)
        summary = text[:200].strip()
        if len(text) > 200:
            summary += "..."

        return {
            "service": service,
            "summary": summary,
            "priority": priority,
            "budget": budget,
            "client_name": None,
            "confidence": confidence,
            "raw_text": text[:500],
        }

    def _parse_with_llm(self, text: str) -> Dict[str, Any]:
        """LLM-based parsing."""
        prompt = f"""Analyze this text and extract lead information.

Text:
{text[:1000]}

Return ONLY a JSON object with these fields:
- service: one of [logo_design, brand_identity, web_design, landing_page, presentation, illustration, social_media, social_media_pack, poster, brochure, video, motion_graphics, content_writing, translation, seo, unknown]
- summary: brief project description (max 200 chars)
- priority: "low", "normal", or "high"
- budget: integer or null
- client_name: string or null
- confidence: float 0.0 to 1.0

JSON only. No explanation."""

        response = self._llm.generate(prompt)

        try:
            start = response.find("{")
            end = response.rfind("}") + 1
            if start >= 0 and end > start:
                data = json.loads(response[start:end])
                return {
                    "service": data.get("service", "unknown"),
                    "summary": data.get("summary", ""),
                    "priority": data.get("priority", "normal"),
                    "budget": data.get("budget"),
                    "client_name": data.get("client_name"),
                    "confidence": data.get("confidence", 0.8),
                    "raw_text": text[:500],
                }
        except (json.JSONDecodeError, ValueError):
            pass

        return self._parse_with_rules(text)