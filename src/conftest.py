import pytest
from selenium import webdriver
from src.sleepio_onboarding_page import sleepio_page


@pytest.fixture
def driver() -> webdriver:
    d = webdriver.Chrome()
    yield d
    d.quit()
