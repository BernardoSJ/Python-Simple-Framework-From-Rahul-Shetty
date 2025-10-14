import pytest


@pytest.fixture(scope="class")
def setup():
    print("It will execute first")
    yield
    print("Executed last")

@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Bernardo", "Salinas", "bernardo.com"]


@pytest.fixture(params=[("chrome", "Bernardo", "Salinas"), ("firefox", "SJ"), ("edge", "JJ")])
def crossBrowser(request):
    return request.param