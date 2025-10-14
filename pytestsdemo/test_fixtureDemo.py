import pytest

@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureDemo(self):
        print("Execute steps in fixtureDemo method")

    def test_fixtureDemo1(self):
        print("Execute steps in fixtureDemo method")

    def test_fixtureDemo2(self):
        print("Execute steps in fixtureDemo method")

    def test_fixtureDemo3(self):
        print("Execute steps in fixtureDemo method")