from pathlib import Path

import undetected_chromedriver as uc
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Browser:
    def __init__(self, headless=False):
        options = Options()
        options.add_argument(
            f'--user-data-dir={Path("default_user_data").absolute()}'
        )
        self.driver = uc.Chrome(
            headless=headless, use_subprocess=False, options=options
        )
        self.driver.get('https://youtube.com')

    def try_skip_ad(self):
        try:
            self.driver.execute_script(
                'arguments[0].click()',
                self.find_element('.ytp-ad-skip-button-modern'),
            )
        except TimeoutException:
            pass

    def find_element(self, selector, element=None, wait=10):
        return WebDriverWait(element or self.driver, wait).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )

    def __del__(self):
        self.driver.quit()
