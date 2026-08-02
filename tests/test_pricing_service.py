"""Tests for PricingService."""

import pytest
from services.pricing_service import PricingService


@pytest.fixture
def pricing():
    return PricingService()


def test_base_price(pricing):
    assert pricing.get_base_price("logo_design") == 150


def test_unknown_service_price(pricing):
    assert pricing.get_base_price("quantum_computing") == 200


def test_calculate_normal(pricing):
    result = pricing.calculate("logo_design")
    assert result["final_price"] == 150
    assert result["currency"] == "USD"
    assert "3-5 days" in result["timeline"]


def test_calculate_high_priority(pricing):
    result = pricing.calculate("logo_design", priority="high")
    assert result["final_price"] == 195  # 150 * 1.3


def test_calculate_low_priority(pricing):
    result = pricing.calculate("logo_design", priority="low")
    assert result["final_price"] == 135  # 150 * 0.9


def test_calculate_complex(pricing):
    result = pricing.calculate("logo_design", complexity="complex")
    assert result["final_price"] == 225  # 150 * 1.5


def test_calculate_enterprise(pricing):
    result = pricing.calculate("logo_design", complexity="enterprise")
    assert result["final_price"] == 375  # 150 * 2.5


def test_calculate_rush(pricing):
    result = pricing.calculate("logo_design", rush=True)
    assert result["final_price"] == 195  # 150 * 1.3
    assert "rush" in result["timeline"]


def test_calculate_high_plus_rush(pricing):
    result = pricing.calculate("logo_design", priority="high", rush=True)
    # 150 * 1.3 * 1.3 = 253.5 -> 254
    assert result["final_price"] == 254


def test_calculate_simple(pricing):
    result = pricing.calculate("logo_design", complexity="simple")
    assert result["final_price"] == 120  # 150 * 0.8


def test_breakdown_string(pricing):
    result = pricing.calculate("logo_design", complexity="complex")
    assert "150" in result["breakdown"]
    assert "1.5" in result["breakdown"]


def test_list_services(pricing):
    services = pricing.list_services()
    assert "logo_design" in services
    assert "web_design" in services
    assert len(services) > 10


def test_add_service(pricing):
    pricing.add_service("nft_art", 500)
    assert pricing.get_base_price("nft_art") == 500


def test_normalize_service(pricing):
    assert pricing.get_base_price("Logo Design") == 150
    assert pricing.get_base_price("LOGO-DESIGN") == 150


def test_custom_currency():
    pricing = PricingService(currency="EUR")
    result = pricing.calculate("logo_design")
    assert result["currency"] == "EUR"


def test_web_design_price(pricing):
    result = pricing.calculate("web_design")
    assert result["final_price"] == 600


def test_brand_identity_price(pricing):
    result = pricing.calculate("brand_identity")
    assert result["final_price"] == 400