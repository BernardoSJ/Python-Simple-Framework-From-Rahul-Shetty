import pytest



@pytest.mark.smoke
def test_firstProgram(setup):
    print("Example")

@pytest.mark.xfail
def test_secondProgramCreditCard():
    print("Good day")

def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
