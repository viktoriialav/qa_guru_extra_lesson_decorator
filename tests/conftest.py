import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.timeout = 10.0

    yield

    browser.quit()
