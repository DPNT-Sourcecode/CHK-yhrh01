from lib.solutions.HLO.hello_solution import HelloSolution

class TestHello():
    def test_hello(self):
        names = ["David", "Sara", "Jane"]
        for name in names:
            assert HelloSolution().hello(name) == f"Hello, {name}"