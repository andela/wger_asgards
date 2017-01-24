from selenium import webdriver
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.utils.decorators import classonlymethod


class LogoTestCase(StaticLiveServerTestCase):
    """ Tests Website Logo Redirects to Home Page"""

    @classonlymethod
    def setUpClass(cls):
        super(StaticLiveServerTestCase, cls).setUpClass()
        cls.browser = webdriver.PhantomJS()
        cls.browser.implicitly_wait(10)

    @classonlymethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(StaticLiveServerTestCase, cls).tearDownClass()

    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def test_logo_redirects_to_homepage(self):
        # get the dashboard page
        self.browser.get(self.get_full_url('exercise:exercise:overview'))
        logo = self.browser.find_element_by_css_selector('span.name')
        # Get the link
        logo_link = logo.find_element_by_link_text(
                        'wger').get_attribute('href')

        # assert logo link is the link to homepage
        self.assertEqual(logo_link, self.get_full_url('core:dashboard'))
