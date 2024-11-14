"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""

import allure
import pytest
from selene import browser


@pytest.mark.parametrize("desktop_browser_resolution", [(1600, 900)], indirect=True)
def test_github_desktop(desktop_browser_resolution):
    with allure.step("Открыть страницу ГитХаб"):
        browser.open("https://github.com/")

    with allure.step("Нажать 'Sing in'"):
        browser.all('//a[@href= "/login"]')[1].click()


@pytest.mark.parametrize("mobile_browser_resolution", [(414, 896)], indirect=True)
def test_github_mobile(mobile_browser_resolution):
    with allure.step("Открыть страницу ГитХаб"):
        browser.open("https://github.com/")

    with allure.step("Открыть меню в левой верхней части экрана"):
        browser.element(".Button-label").click()

    with allure.step("Нажать 'Sing up'"):
        browser.element('.HeaderMenu-link--sign-up').click()
