"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import allure
import pytest
from selene import browser


@pytest.fixture(params=[(1600, 900), (1366, 768), (1280, 1024), (414, 896), (375, 812), (320, 480)],
                ids=["1600x900", "1366x768", "1280x1024", "414x896", "375x812", "320x480"])
def setup_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    if width > 640:
        yield "desktop"
    else:
        yield "mobile"
    browser.quit()


def test_github_desktop(setup_browser):
    if setup_browser == "mobile":
        pytest.skip(reason="Это тест для десктопа")
    with allure.step("Открыть страницу ГитХаб"):
        browser.open("https://github.com/")

    with allure.step("Нажать 'Sing in'"):
        browser.all('//a[@href= "/login"]')[1].click()


def test_github_mobile(setup_browser):
    if setup_browser == "desktop":
        pytest.skip(reason="Это тест для мобильной версии")
    with allure.step("Открыть страницу ГитХаб"):
        browser.open("https://github.com/")

    with allure.step("Открыть меню в левой верхней части экрана"):
        browser.element(".Button-label").click()

    with allure.step("Нажать 'Sing up'"):
        browser.element('.HeaderMenu-link--sign-up').click()
