from src.sleepio_onboarding_page import SleepioPage
from selenium.webdriver.common.by import By
from uuid import uuid4
import requests


def test_happy_path(sleepio_page: SleepioPage):
    sleepio_page.visit_landing_page()
    sleepio_page.click_get_started()

    sleepio_page.click_label("Get to sleep more easily")
    sleepio_page.click_continue()

    sleepio_page.pick_from_select('[data-semantic-id="problem_sleep"] select', "A week or less")
    sleepio_page.click_continue()

    # Which of the following stops you from sleeping most often?
    sleepio_page.click_label("Worries about future events")
    sleepio_page.click_continue()

    # To what extent has sleep troubled you in general?
    sleepio_page.pick_from_select('[data-semantic-id="troubled_in_general"] select', "A little")
    sleepio_page.click_continue()

    # How many nights a week have you had a problem with your sleep?
    sleepio_page.pick_from_select('[data-semantic-id="problem_nights"] select', "1 night")
    sleepio_page.click_continue()

    # How often have you felt that you were unable to control the important things in your life?
    sleepio_page.pick_from_select('[data-semantic-id="unable_to_control"] select', "Almost never")
    sleepio_page.click_continue()

    # How likely is it that you would fall asleep during the day without intending to...
    sleepio_page.pick_from_select('[data-semantic-id="fall_asleep_stay_awake"] select', "Slight chance")
    sleepio_page.click_continue()

    # How would you describe your gender?
    sleepio_page.click_label("Male")
    sleepio_page.click_continue()

    # What is your date of birth?
    sleepio_page.pick_from_select("#select-month", "January")
    sleepio_page.pick_from_select("#select-day", "11")
    sleepio_page.pick_from_select("#select-year", "1999")
    sleepio_page.click_continue()

    # What is your employment status?
    sleepio_page.pick_from_select('[data-semantic-id="employment_status"] select', "Employed full-time")
    sleepio_page.click_continue()

    # How much did poor sleep affect your productivity while you were working?
    sleepio_page.pick_from_select('[data-semantic-id="affect_productivity"] select', "10%")
    sleepio_page.click_continue()

    # How many hours did you miss from your work per week because of problems...
    sleepio_page.send_keys_to_input('[data-semantic-id="hours_missed"] input', 1)
    sleepio_page.click_continue()

    # Which of the following expert guides might be of interest to you?
    sleepio_page.click_label("Dealing with jet lag")
    sleepio_page.click_continue()

    # Get Your Sleep Score
    fill_out_signup_page_fields(sleepio_page)
    sleepio_page.click_sign_up()

    sleepio_page.wait_for_display_text("h1", "YOUR SLEEP SCORE", timeout=20)
    sleepio_page.wait_for_display_text(".sl-score", "8.75 / 10")


def test_clicking_none_of_the_above_deselects_other_options(sleepio_page):
    # this should probably be done at the unit level
    # but for this exercise i dont have access to the source to write unit tests

    sleepio_page.visit_landing_page()
    sleepio_page.click_get_started()

    # Select all the items
    sleepio_page.click_label("Get to sleep more easily")
    sleepio_page.click_label("Sleep right through the night without waking up")
    sleepio_page.click_label("Stop waking up too early")
    sleepio_page.click_label("Wake up feeling refreshed")

    # They're all selected and None of the Above is not
    assert sleepio_page.label_item_is_selected("Get to sleep more easily")
    assert sleepio_page.label_item_is_selected("Sleep right through the night without waking up")
    assert sleepio_page.label_item_is_selected("Stop waking up too early")
    assert sleepio_page.label_item_is_selected("Wake up feeling refreshed")
    assert not sleepio_page.label_item_is_selected("None of the above")

    # Click none of the above...
    sleepio_page.click_label("None of the above")

    # ...and the other items are deselected
    assert not sleepio_page.label_item_is_selected("Get to sleep more easily")
    assert not sleepio_page.label_item_is_selected("Sleep right through the night without waking up")
    assert not sleepio_page.label_item_is_selected("Stop waking up too early")
    assert not sleepio_page.label_item_is_selected("Wake up feeling refreshed")
    assert sleepio_page.label_item_is_selected("None of the above")

    # Click one of the other ones again...
    sleepio_page.click_label("Stop waking up too early")

    # ...and None of the Above is unchecked again!
    assert sleepio_page.label_item_is_selected("Stop waking up too early")
    assert not sleepio_page.label_item_is_selected("Get to sleep more easily")
    assert not sleepio_page.label_item_is_selected("Sleep right through the night without waking up")
    assert not sleepio_page.label_item_is_selected("Wake up feeling refreshed")
    assert not sleepio_page.label_item_is_selected("None of the above")


def test_really_bad_sleep_situation(sleepio_page):
    sleepio_page.visit_landing_page()
    sleepio_page.click_get_started()

    sleepio_page.click_label("Get to sleep more easily")
    sleepio_page.click_label("Sleep right through the night without waking up")
    sleepio_page.click_label("Stop waking up too early")
    sleepio_page.click_label("Wake up feeling refreshed")
    sleepio_page.click_continue()

    sleepio_page.pick_from_select('[data-semantic-id="problem_sleep"] select', "11 or more years")
    sleepio_page.click_continue()

    sleepio_page.click_label("Bodily discomfort or pain")
    sleepio_page.click_continue()

    # To what extent has sleep troubled you in general?
    sleepio_page.pick_from_select('[data-semantic-id="troubled_in_general"] select', "Very much")
    sleepio_page.click_continue()

    # How many nights a week have you had a problem with your sleep?
    sleepio_page.pick_from_select('[data-semantic-id="problem_nights"] select', "7 nights")
    sleepio_page.click_continue()

    # How often have you felt that you were unable to control the important things in your life?
    sleepio_page.pick_from_select('[data-semantic-id="unable_to_control"] select', "Very often")
    sleepio_page.click_continue()

    # How likely is it that you would fall asleep during the day without intending to...
    sleepio_page.pick_from_select('[data-semantic-id="fall_asleep_stay_awake"] select', "High chance")
    sleepio_page.click_continue()

    # Has your snoring ever bothered other people?
    sleepio_page.click_label("Yes")
    sleepio_page.click_continue()

    # Has anyone noticed that you stop breathing during sleep?
    sleepio_page.click_label("Yes")
    sleepio_page.click_continue()

    # How would you describe your gender?
    sleepio_page.click_label("Male")
    sleepio_page.click_continue()

    # What is your date of birth?
    sleepio_page.pick_from_select("#select-month", "October")
    sleepio_page.pick_from_select("#select-day", "31")
    sleepio_page.pick_from_select("#select-year", "1924")
    sleepio_page.click_continue()

    # What is your employment status?
    sleepio_page.pick_from_select('[data-semantic-id="employment_status"] select', "Unemployed")
    sleepio_page.click_continue()

    # Which of the following expert guides might be of interest to you?
    sleepio_page.click_label("None of the above")
    sleepio_page.click_continue()

    fill_out_signup_page_fields(sleepio_page)
    sleepio_page.click_sign_up()

    sleepio_page.wait_for_display_text("h1", "YOUR SLEEP SCORE", timeout=20)
    sleepio_page.wait_for_display_text(".sl-score", "0.0 / 10")


def test_double_registration_fails():
    user_uuid = str(uuid4())
    first_name = uuid4().hex
    last_name = uuid4().hex
    email = f"{uuid4().hex}@example.com"
    password = f"{uuid4()}!"

    post_body = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "data_storing": True,
        "doctor_acknowledgement": True,
        "product_id": 1,
        "uuid": user_uuid,
        "organization_id": 2,
        "interactive_id": 26,
        "onboarding_vanity": "big-health",
        "onboarding_flow_id": 1,
        "answers": {},
    }

    first_raw = requests.post(
        "https://onboarding.sleepio.com/auth/check_eligibility_for_organization_and_sign_up/", json=post_body
    )

    # First registration succeeds
    assert first_raw.status_code == 200, f"Should get a 200, got {first_raw.status_code}"
    first_json = first_raw.json()
    assert first_json["status"] == "success"
    assert first_json["user_data"]["completed_flow"] is False

    # Second registration fails
    second_raw = requests.post(
        "https://onboarding.sleepio.com/auth/check_eligibility_for_organization_and_sign_up/", json=post_body
    )
    assert second_raw.status_code == 200, "Should get a 200 (but body should contain error=True)"
    second_json = second_raw.json()
    assert second_json["error"] is True
    assert "Your account could not be created" in second_json["message"]


def test_registration_errors_when_missing_interactive_id():
    post_body = {
        "uuid": str(uuid4()),
    }

    raw = requests.post(
        "https://onboarding.sleepio.com/auth/check_eligibility_for_organization_and_sign_up/", json=post_body
    )
    assert raw.status_code == 200, "Should fail successfully"
    json_res = raw.json()
    assert json_res["error"] is True
    assert json_res["message"] == "Missing parameter: interactive id"


def test_registration_succeeds_without_name_or_password_to_my_surprise():
    user_uuid = str(uuid4())

    post_body = {
        "data_storing": True,
        "doctor_acknowledgement": True,
        "product_id": 1,
        "uuid": user_uuid,
        "organization_id": 2,
        "interactive_id": 26,
        "onboarding_vanity": "big-health",
        "onboarding_flow_id": 1,
        "answers": {},
    }
    raw = requests.post(
        "https://onboarding.sleepio.com/auth/check_eligibility_for_organization_and_sign_up/", json=post_body
    )
    assert raw.status_code == 200
    json_res = raw.json()
    assert json_res["status"] == "success"
    assert json_res["user_data"]["first_name"] is None
    assert json_res["user_data"]["last_name"] is None
    assert json_res["user_data"]["email"] is None
    assert json_res["user_data"]["completed_flow"] is False


def fill_out_signup_page_fields(sleepio_page: SleepioPage) -> None:
    # todo return name etc if needed

    first_name = uuid4().hex
    last_name = uuid4().hex
    email = f"{uuid4().hex}@example.com"
    password = f"{uuid4()}!"
    sleepio_page.send_keys_to_input('[name="first_name"]', first_name)
    sleepio_page.send_keys_to_input('[name="last_name"]', last_name)
    sleepio_page.send_keys_to_input('[name="email"]', email)
    sleepio_page.send_keys_to_input('[name="password"]', password)
    checkboxes = sleepio_page.driver.find_elements(By.CSS_SELECTOR, ".sl-interactive--checkbox input")
    [box.click() for box in checkboxes]  # todo: better selector probably. probably move to page class
