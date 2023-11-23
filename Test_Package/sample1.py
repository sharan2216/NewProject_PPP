import pytest


@pytest.mark.login
def test_regression():
    print("test_regression")


@pytest.mark.login
def test_sanity():
    print("test_sanity")


@pytest.mark.login
def test_functional():
    print("test_functional1")


@pytest.mark.settings
def test_api():
    print("test_api")


@pytest.mark.settings
def test_regression2():
    print("test_regression2")
