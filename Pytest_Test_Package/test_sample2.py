import pytest


@pytest.mark.login
def test_regression():
    print("test_regression")


@pytest.mark.login
def test_sanity():
    print("test_sanity")


@pytest.mark.login
def test_functional():
    print("test_functional")


@pytest.mark.settings
def test_api():
    print("test_api")


@pytest.mark.settings
def test_regression():
    print("test_regression")
