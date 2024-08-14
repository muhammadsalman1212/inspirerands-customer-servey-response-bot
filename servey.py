import time
import random
from playwright.sync_api import sync_playwright

def read_file_lines(file_path):
    """Reads the content of a file and returns it as a list of lines."""
    with open(file_path, "r") as file:
        return file.readlines()

def get_random_text(text_list):
    """Returns a random text from the given list."""
    return random.choice(text_list)

def get_link(file_path):
    """Reads the link from a file and returns it."""
    with open(file_path, 'r') as file:
        return file.read().strip()



all_text = read_file_lines("experience.txt")
random_text = get_random_text(all_text)
link = get_link('link.txt')


def automate_survey():
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(headless=False, user_data_dir="user_data_dir")
        page = browser.new_page()



        count = 1
        while True:
            page.goto(link)

            # next button
            page.click('//input[@id="NextButton"]', timeout=0)

            verysatisfied_button = page.click("//*[text()='Very Satisfied']", timeout=0)
            time.sleep(random.randint(4, 8))

            next_button = page.click('//input[@title="→"]', timeout=0)
            # page.click('//input[@id="NextButton"]', timeout=0) # next button

            time.sleep(1)
            describe_enperience_input = page.fill('//div[@class="ChoiceStructure"]//textarea', random_text, timeout=0)
            time.sleep(1)
            next_button = page.click('//input[@title="→"]', timeout=0)
            time.sleep(1)
            first_dot = page.click('//tr[@class="ChoiceRow  "]//td[@class="c8 last  "]//label', timeout=0)
            time.sleep(1)
            third_dot = page.click('(//tr[@class="ChoiceRow  "]//td[@class="c8 last  "]//label)[3]', timeout=0)
            time.sleep(1)
            second_dot = page.click('(//tr[@class="ChoiceRow ReadableAlt "]//td[@class="c8 last  "]//label)[1]', timeout=0)
            time.sleep(1)
            forth_dot = page.click('(//tr[@class="ChoiceRow ReadableAlt "]//td[@class="c8 last  "]//label)[3]', timeout=0)
            time.sleep(1)
            fifth_dot = page.click('(//tr[@class="ChoiceRow   bottom "]//td[@class="c8 last  "]//label)', timeout=0)
            time.sleep(1)
            next_button = page.click('//input[@title="→"]', timeout=0)
            time.sleep(1)
            all_location_button = page.click("//*[text()='At Location']", timeout=0)
            time.sleep(1)
            stall_button = page.click("//*[text()='Stall']", timeout=0)
            time.sleep(1)
            # next button
            next_button = page.click('//input[@title="→"]', timeout=0)
            time.sleep(1)
            # random date:
            time_list = ["4am – 11am", "11am – 2pm", "2pm – 5pm", "5pm – 8pm", "8pm – 4am"]

            random_time = random.choice(time_list)
            date_button = page.click(f"//*[text()='{random_time}']", timeout=0)

            # next button
            next_button = page.click('//input[@title="→"]', timeout=0)

            very_satisfied_dot = page.click('//tr[@class="ChoiceRow  "]//td[@class="c8 last  "]//label', timeout=0)

            last_very_satisfied_dot = page.click('//tr[@class="ChoiceRow ReadableAlt  bottom "]//td[@class="c8 last  "]//label', timeout=0)

            # next button
            next_button = page.click('//input[@title="→"]', timeout=0)

            very_likely_button = page.click("//*[text()='Very Likely']", timeout=0)

            next_button = page.click('//input[@title="→"]', timeout=0)

            second_option = page.click('//li[@class="Selection alt"]', timeout=0) # no i did't gave the grovy fries

            same_second_option = page.click('(//li[@class="Selection alt"])[2]', timeout=0) # same second option

            next_button = page.click('//input[@title="→"]', timeout=0)

            print(f"Done {count} times")

            count += 1

            # wait between 50 to 60 minuites
            page.reload()
            wait_time = random.randint(3000, 3600)
            # convert seconds to minutes
            minutes = wait_time // 60
            seconds = wait_time % 60
            print(f"Waiting for {minutes} minutes and {seconds} seconds")
            time.sleep(wait_time)



            page.reload()

if __name__ == "__main__":
    automate_survey()


