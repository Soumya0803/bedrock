# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.base import BasePage


class FirefoxWhatsNew113Page(BasePage):
    _URL_TEMPLATE = "/{locale}/firefox/113.0/whatsnew/"

    _get_vpn_button_locator = (By.CSS_SELECTOR, ".wnp-main-cta .mzp-c-button")

    @property
    def is_get_vpn_button_displayed(self):
        return self.is_element_displayed(*self._get_vpn_button_locator)
