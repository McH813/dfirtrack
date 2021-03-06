from django.contrib.auth.models import User
from django.test import TestCase
import urllib.parse

class SystemExporterSpreadsheetCsvConfigViewTestCase(TestCase):
    """ system exporter spreadsheet CSV config view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_system_exporter_spreadsheet_csv_config', password='ocTJgNdjZMafypl2FR43')

    def test_system_exporter_spreadsheet_csv_config_not_logged_in(self):
        """ test exporter view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/config/system/exporter/spreadsheet/csv/', safe='')
        # get response
        response = self.client.get('/config/system/exporter/spreadsheet/csv/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_exporter_spreadsheet_csv_config_logged_in(self):
        """ test view """

        # login testuser
        login = self.client.login(username='testuser_system_exporter_spreadsheet_csv_config', password='ocTJgNdjZMafypl2FR43')
        # get response
        response = self.client.get('/config/system/exporter/spreadsheet/csv/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_exporter_spreadsheet_csv_config_template(self):
        """ test exporter view """

        # login testuser
        login = self.client.login(username='testuser_system_exporter_spreadsheet_csv_config', password='ocTJgNdjZMafypl2FR43')
        # get response
        response = self.client.get('/config/system/exporter/spreadsheet/csv/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_config/system/system_exporter_spreadsheet_csv_config_popup.html')

    def test_system_exporter_spreadsheet_csv_config_get_user_context(self):
        """ test exporter view """

        # login testuser
        login = self.client.login(username='testuser_system_exporter_spreadsheet_csv_config', password='ocTJgNdjZMafypl2FR43')
        # get response
        response = self.client.get('/config/system/exporter/spreadsheet/csv/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system_exporter_spreadsheet_csv_config')

    def test_system_exporter_spreadsheet_csv_config_redirect(self):
        """ test view """

        # login testuser
        login = self.client.login(username='testuser_system_exporter_spreadsheet_csv_config', password='ocTJgNdjZMafypl2FR43')
        # create url
        destination = urllib.parse.quote('/config/system/exporter/spreadsheet/csv/', safe='/')
        # get response
        response = self.client.get('/config/system/exporter/spreadsheet/csv', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
