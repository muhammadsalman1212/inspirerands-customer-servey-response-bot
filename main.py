import time
import random
from playwright.sync_api import sync_playwright

all_text = []
with open("experience.txt", "r") as file:
    for line in file:
        all_text.append(line)
random_text = random.choice(all_text)



with open('link.txt', 'r') as file:
    link = file.read().strip()

print("Read link:", link)


def automate_survey():
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(headless=False, user_data_dir="user_data_dir")
        page = browser.new_page()

        count = 1
        while True:
            page.goto(link)
            page.click('//input[@id="NextButton"]', timeout=0)

            verysatisfied_button = page.click("//*[text()='Very Satisfied']", timeout=0)
            time.sleep(random.randint(1, 3))

            next_button = page.click('//input[@id="NextButton"]', timeout=0)

            describe_enperience_input = page.fill('//div[@class="ChoiceStructure"]//textarea', random_text, timeout=0)

            page.click('//input[@id="NextButton"]', timeout=0) # next button

            first_dot = page.click('//tr[@class="ChoiceRow  "]//td[@class="c8 last  "]//label', timeout=0)

            third_dot = page.click('(//tr[@class="ChoiceRow  "]//td[@class="c8 last  "]//label)[3]', timeout=0)

            second_dot = page.click('(//tr[@class="ChoiceRow ReadableAlt "]//td[@class="c8 last  "]//label)[1]', timeout=0)

            forth_dot = page.click('(//tr[@class="ChoiceRow ReadableAlt "]//td[@class="c8 last  "]//label)[3]', timeout=0)

            fifth_dot = page.click('(//tr[@class="ChoiceRow   bottom "]//td[@class="c8 last  "]//label)', timeout=0)

            page.click('//input[@id="NextButton"]', timeout=0) # next button

            all_location_button = page.click("//*[text()='At Location']", timeout=0)

            stall_button = page.click("//*[text()='Stall']", timeout=0)

            # next button
            page.click('//input[@id="NextButton"]', timeout=0)

            # random date:
            time_list = ["4am – 11am", "11am – 2pm", "2pm – 5pm", "5pm – 8pm", "8pm – 4am"]

            random_time = random.choice(time_list)
            date_button = page.click(f"//*[text()='{random_time}']", timeout=0)

            # next button
            page.click('//input[@id="NextButton"]', timeout=0)

            very_satisfied_dot = page.click('//tr[@class="ChoiceRow  "]//td[@class="c8 last  "]//label', timeout=0)

            last_very_satisfied_dot = page.click('//tr[@class="ChoiceRow ReadableAlt  bottom "]//td[@class="c8 last  "]//label', timeout=0)

            # next button
            page.click('//input[@id="NextButton"]', timeout=0)

            very_likely_button = page.click("//*[text()='Very Likely']", timeout=0)

            page.click('//input[@id="NextButton"]', timeout=0)

            second_option = page.click('//li[@class="Selection alt"]', timeout=0) # no i did't gave the grovy fries

            same_second_option = page.click('(//li[@class="Selection alt"])[2]', timeout=0) # same second option

            page.click('//input[@id="NextButton"]', timeout=0) # next button

            print(f"Done {count} times")

            count += 1

            time.sleep(10)
            page.reload()

            # i want to wait for between 50 to 60 minuites

            time.sleep(random.randint(3000, 3600))

if __name__ == "__main__":
    automate_survey()

