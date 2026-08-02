"""
PricingService - Central pricing logic for AgencyOS.

Responsibilities:
    - Calculate project price based on service, priority, complexity
    - Apply rush fees
    - Apply volume discounts
    - Return price breakdown

Architecture:
    - This is a SERVICE. Contains business logic.
    - Agents call this. They do NOT contain pricing rules.
    - Later: LLM-assisted pricing, market data, freelancer rates.
"""

from typing import Any, Dict, Optional


# ─── Base Price Table (MVP) ──────────────────────────────────
BASE_PRICES = {
    "logo_design": 150,
    "brand_identity": 400,
    "web_design": 600,
    "landing_page": 350,
    "presentation": 200,
    "illustration": 250,
    "social_media": 180,
    "social_media_pack": 300,
    "poster": 120,
    "brochure": 250,
    "video": 500,
    "motion_graphics": 450,
    "content_writing": 200,
    "translation": 100,
    "seo": 350,
    "unknown": 200,
}

# ─── Timeline Table ──────────────────────────────────────────
TIMELINES = {
    "logo_design": "3-5 days",
    "brand_identity": "7-14 days",
    "web_design": "14-21 days",
    "landing_page": "7-10 days",
    "presentation": "3-5 days",
    "illustration": "5-7 days",
    "social_media": "3-5 days",
    "social_media_pack": "5-7 days",
    "poster": "2-3 days",
    "brochure": "5-7 days",
    "video": "7-14 days",
    "motion_graphics": "7-10 days",
    "content_writing": "5-7 days",
    "translation": "3-5 days",
    "seo": "14-21 days",
    "unknown": "5-7 days",
}

# ─── Multipliers ─────────────────────────────────────────────
RUSH_MULTIPLIER = 1.3
COMPLEXITY_MULTIPLIERS = {
    "simple": 0.8,
    "normal": 1.0,
    "complex": 1.5,
    "enterprise": 2.5,
}


class PricingService:
    """Calculates project pricing."""

    def __init__(
        self,
        base_prices: Optional[Dict[str, int]] = None,
        currency: str = "USD",
    ):
        self._prices = base_prices or dict(BASE_PRICES)
        self._currency = currency

    @property
    def currency(self) -> str:
        return self._currency

    def get_base_price(self, service: str) -> int:
        """Get base price for a service type."""
        key = self._normalize_service(service)
        return self._prices.get(key, self._prices["unknown"])

    def calculate(
        self,
        service: str,
        priority: str = "normal",
        complexity: str = "normal",
        rush: bool = False,
    ) -> Dict[str, Any]:
        """
        Calculate full price breakdown.

        Args:
            service: Service type (e.g., "logo_design")
            priority: "low", "normal", "high"
            complexity: "simple", "normal", "complex", "enterprise"
            rush: Apply rush fee?

        Returns:
            Price breakdown dictionary.
        """
        key = self._normalize_service(service)
        base = self._prices.get(key, self._prices["unknown"])

        # Complexity multiplier
        comp_mult = COMPLEXITY_MULTIPLIERS.get(complexity, 1.0)
        price = base * comp_mult

        # Priority multiplier
        if priority == "high":
            price *= RUSH_MULTIPLIER
        elif priority == "low":
            price *= 0.9

        # Rush fee (stacks with priority)
        if rush:
            price *= RUSH_MULTIPLIER

        final_price = int(round(price))

        timeline = TIMELINES.get(key, TIMELINES["unknown"])
        if rush or priority == "high":
            timeline += " (rush)"

        return {
            "service": key,
            "base_price": base,
            "complexity": complexity,
            "complexity_multiplier": comp_mult,
            "priority": priority,
            "rush": rush,
            "final_price": final_price,
            "currency": self._currency,
            "timeline": timeline,
            "breakdown": f"${base} base × {comp_mult} complexity"
            + (f" × {RUSH_MULTIPLIER} priority" if priority == "high" else "")
            + (f" × {RUSH_MULTIPLIER} rush" if rush else "")
            + f" = ${final_price}",
        }

    def list_services(self) -> Dict[str, int]:
        """Return all available services and base prices."""
        return dict(self._prices)

    def add_service(self, name: str, price: int) -> None:
        """Add or update a service price."""
        self._prices[self._normalize_service(name)] = price

    def _normalize_service(self, service: str) -> str:
        """Normalize service name to key format."""
        return service.lower().strip().replace(" ", "_").replace("-", "_")