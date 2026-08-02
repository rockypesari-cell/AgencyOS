"""
ServiceContainer - Central dependency management for AgencyOS.

Manages all service instances (LeadService, LLMService, etc.)
in one place. Enables dependency injection and loose coupling.

Architecture Decision:
    - Services are NOT required to inherit a base class.
    - Any object can be registered as a service (duck typing).
    - Container does NOT create services. It stores them.
    - Container does NOT contain business logic.

Usage:
    container = ServiceContainer()
    container.register("llm_service", LLMService())
    container.register("lead_service", LeadService(llm))

    llm = container.get("llm_service")
"""

from typing import Any, Dict, List


class ServiceContainer:
    """Central container for managing all service instances."""

    def __init__(self):
        self._services: Dict[str, Any] = {}

    def register(self, name: str, instance: Any) -> None:
        """
        Register a service instance.

        Args:
            name: Unique service identifier.
            instance: The service object.

        Raises:
            ValueError: If name is empty or already registered.
            TypeError: If instance is None.
        """
        if not name or not name.strip():
            raise ValueError("Service name cannot be empty.")

        if instance is None:
            raise TypeError("Service instance cannot be None.")

        name = name.strip()

        if name in self._services:
            raise ValueError(
                f"Service '{name}' is already registered."
            )

        self._services[name] = instance

    def get(self, name: str) -> Any:
        """
        Retrieve a service by name.

        Raises:
            KeyError: If service not found.
        """
        if name not in self._services:
            raise KeyError(f"Service '{name}' not found in container.")
        return self._services[name]

    def get_or_none(self, name: str) -> Any:
        """Retrieve a service or return None if not found."""
        return self._services.get(name)

    def exists(self, name: str) -> bool:
        return name in self._services

    def remove(self, name: str) -> None:
        if name not in self._services:
            raise KeyError(f"Service '{name}' not found in container.")
        del self._services[name]

    def list_services(self) -> List[str]:
        return sorted(self._services.keys())

    def count(self) -> int:
        return len(self._services)

    def clear(self) -> None:
        self._services.clear()

    def info(self) -> Dict[str, str]:
        """Return service names and their types."""
        return {
            name: type(inst).__name__
            for name, inst in self._services.items()
        }

    def __contains__(self, name: str) -> bool:
        return name in self._services

    def __len__(self) -> int:
        return len(self._services)

    def __repr__(self) -> str:
        return f"<ServiceContainer: {len(self._services)} services>"