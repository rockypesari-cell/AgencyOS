import unittest

from src.core.agent_registry import AgentRegistry


class DummyAgent:
    pass


class TestAgentRegistry(unittest.TestCase):

    def setUp(self):
        self.registry = AgentRegistry()

    def test_register_agent(self):
        agent = DummyAgent()

        self.registry.register("dummy", agent)

        self.assertTrue(self.registry.exists("dummy"))

    def test_get_agent(self):
        agent = DummyAgent()

        self.registry.register("dummy", agent)

        self.assertIs(self.registry.get("dummy"), agent)

    def test_duplicate_registration(self):
        agent = DummyAgent()

        self.registry.register("dummy", agent)

        with self.assertRaises(ValueError):
            self.registry.register("dummy", agent)

    def test_remove_agent(self):
        agent = DummyAgent()

        self.registry.register("dummy", agent)

        self.registry.remove("dummy")

        self.assertFalse(self.registry.exists("dummy"))

    def test_remove_unknown_agent(self):
        with self.assertRaises(KeyError):
            self.registry.remove("unknown")

    def test_get_unknown_agent(self):
        with self.assertRaises(KeyError):
            self.registry.get("unknown")

    def test_list_agents(self):
        self.registry.register("b", DummyAgent())
        self.registry.register("a", DummyAgent())

        self.assertEqual(
            self.registry.list_agents(),
            ["a", "b"]
        )

    def test_clear(self):
        self.registry.register("a", DummyAgent())
        self.registry.register("b", DummyAgent())

        self.registry.clear()

        self.assertEqual(len(self.registry), 0)

    def test_count(self):
        self.registry.register("a", DummyAgent())
        self.registry.register("b", DummyAgent())

        self.assertEqual(self.registry.count(), 2)

    def test_contains(self):
        self.registry.register("dummy", DummyAgent())

        self.assertIn("dummy", self.registry)

    def test_len(self):
        self.registry.register("a", DummyAgent())
        self.registry.register("b", DummyAgent())

        self.assertEqual(len(self.registry), 2)


if __name__ == "__main__":
    unittest.main()