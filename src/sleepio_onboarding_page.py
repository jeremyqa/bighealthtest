# todo: split this into like a BasePage if we end up having more than one class like this

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from typing import Union
import pytest


class SleepioPage:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver

    def get_user_uuid_from_cookie(self) -> str:
        return self.driver.get_cookie("sl-user-uuid")["value"]

    def visit_landing_page(self) -> None:
        self.driver.get("https://onboarding.sleepio.com/sleepio/big-health")
        self.wait_for_display_text("h1", "Discover your Sleep Score and how to improve it")

    def click_get_started(self) -> None:
        self.wait_for_display_text("button", "Get started").click()

    def click_label(self, label_text: str) -> None:
        self.wait_for_display_text("label", label_text).click()

    def click_continue(self) -> None:
        self.wait_for_display_text("button", "Continue").click()

    def click_sign_up(self) -> None:
        self.wait_for_display_text("button", "Sign Up").click()

    def pick_from_select(self, css_selector: str, visible_text: str) -> None:
        # todo if these all use semantic-id maybe a sugar function to use that instead of the whole selector
        select = Select(self.driver.find_element(By.CSS_SELECTOR, css_selector))
        select.select_by_visible_text(visible_text)

    def send_keys_to_input(self, css_selector: str, text: Union[str, int]) -> None:
        self.driver.find_element(By.CSS_SELECTOR, css_selector).send_keys(text)

    def wait_for_display_text(self, selector: str, text: str, timeout: int = 5) -> WebElement:
        def _check_for_text(_):
            items = self.driver.find_elements(By.CSS_SELECTOR, selector)
            for item in items:
                if item.is_displayed() and item.text == text:
                    return item

        return WebDriverWait(self.driver, timeout, ignored_exceptions=(Exception,)).until(
            _check_for_text, message=f"Never found {text} in item selected by {selector}"
        )  # todo catch more narrow exception

    def label_item_is_selected(self, label_text: str) -> bool:
        # todo: better selector would be ideal
        return (
            self.wait_for_display_text("label", label_text)
            .find_element(By.CSS_SELECTOR, "input")
            .get_attribute("selected")
            == "true"
        )


@pytest.fixture
def sleepio_page(driver: WebDriver) -> SleepioPage:
    return SleepioPage(driver)
