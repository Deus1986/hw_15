import pytest
from selene import browser


@pytest.fixture(params=[(1600, 900), (1366, 768), (1280, 1024)])
def desktop_browser_resolution(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.fixture(params=[(414, 896), (375, 812), (320, 480)])
def mobile_browser_resolution(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()
