import pytest

@pytest.mark.smoke
def test_firstProgram():
    print("Example")

@pytest.mark.xfail
def test_secondProgramCreditCard():
    print("Good day")
