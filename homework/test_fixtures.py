"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""

import allure
from selene import browser


def test_github_desktop(desktop_browser_resolution):
    with allure.step("Открыть страницу ГитХаб"):
        browser.open("https://github.com/")

    with allure.step("Нажать 'Sing in'"):
        browser.all('//a[@href= "/login"]')[1].click()


def test_github_mobile(mobile_browser_resolution):
    with allure.step("Открыть страницу ГитХаб"):
        browser.open("https://github.com/")

    with allure.step("Открыть меню в левой верхней части экрана"):
        browser.element(".Button-label").click()

    with allure.step("Нажать 'Sing up'"):
        browser.element('.HeaderMenu-link--sign-up').click()
