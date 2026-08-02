"""Tests for ServiceContainer."""

import pytest
from core.service_container import ServiceContainer


class FakeService:
    def do_something(self):
        return "done"


@pytest.fixture
def container():
    return ServiceContainer()


@pytest.fixture
def service():
    return FakeService()


def test_register_and_get(container, service):
    container.register("fake", service)
    assert container.get("fake") is service


def test_register_duplicate_raises(container, service):
    container.register("fake", service)
    with pytest.raises(ValueError):
        container.register("fake", FakeService())


def test_register_empty_name_raises(container, service):
    with pytest.raises(ValueError):
        container.register("", service)


def test_register_none_raises(container):
    with pytest.raises(TypeError):
        container.register("fake", None)


def test_get_missing_raises(container):
    with pytest.raises(KeyError):
        container.get("ghost")


def test_get_or_none(container, service):
    assert container.get_or_none("ghost") is None
    container.register("fake", service)
    assert container.get_or_none("fake") is service


def test_exists(container, service):
    assert container.exists("fake") is False
    container.register("fake", service)
    assert container.exists("fake") is True


def test_remove(container, service):
    container.register("fake", service)
    container.remove("fake")
    assert container.exists("fake") is False


def test_remove_missing_raises(container):
    with pytest.raises(KeyError):
        container.remove("ghost")


def test_list_services(container):
    container.register("beta", FakeService())
    container.register("alpha", FakeService())
    assert container.list_services() == ["alpha", "beta"]


def test_count(container, service):
    assert container.count() == 0
    container.register("fake", service)
    assert container.count() == 1


def test_clear(container, service):
    container.register("fake", service)
    container.clear()
    assert container.count() == 0


def test_contains(container, service):
    container.register("fake", service)
    assert "fake" in container


def test_len(container, service):
    container.register("fake", service)
    assert len(container) == 1


def test_info(container, service):
    container.register("fake", service)
    info = container.info()
    assert info["fake"] == "FakeService"


def test_repr(container, service):
    container.register("fake", service)
    assert "1 services" in repr(container)