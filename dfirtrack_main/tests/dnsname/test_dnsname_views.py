from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Dnsname
import urllib.parse

class DnsnameViewTestCase(TestCase):
    """ dnsname view tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Dnsname.objects.create(dnsname_name='dnsname_1')
        # create user
        test_user = User.objects.create_user(username='testuser_dnsname', password='TeWFLE2k6lqoC7c6xc0x')

    def test_dnsname_list_not_logged_in(self):
        """ test list view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/dnsname/', safe='')
        # get response
        response = self.client.get('/dnsname/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_dnsname_list_logged_in(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_dnsname', password='TeWFLE2k6lqoC7c6xc0x')
        # get response
        response = self.client.get('/dnsname/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_dnsname_list_template(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_dnsname', password='TeWFLE2k6lqoC7c6xc0x')
        # get response
        response = self.client.get('/dnsname/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/dnsname/dnsname_list.html')

    def test_dnsname_list_get_user_context(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_dnsname', password='TeWFLE2k6lqoC7c6xc0x')
        # get response
        response = self.client.get('/dnsname/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_dnsname')

    def test_dnsname_list_redirect(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_dnsname', password='TeWFLE2k6lqoC7c6xc0x')
        # create url
        destination = urllib.parse.quote('/dnsname/', safe='/')
        # get response
        response = self.client.get('/dnsname', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_dnsname_detail_not_logged_in(self):
        """ test detail view """

        # get object
        dnsname_1 = Dnsname.objects.get(dnsname_name='dnsname_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/dnsname/' + str(dnsname_1.dnsname_id) + '/', safe='')
        # get response
        response = self.client.get('/dnsname/' + str(dnsname_1.dnsname_id) + '/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_dnsname_detail_logged_in(self):
        """ test detail view """

        # get object
        dnsname_1 = Dnsname.objects.get(dnsname_name='dnsname_1')
        # login testuser
        login = self.client.login(username='testuser_dnsname', password='TeWFLE2k6lqoC7c6xc0x')
        # get response
        response = self.client.get('/dnsname/' + str(dnsname_1.dnsname_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_dnsname_detail_template(self):
        """ test detail view """

        # get object
        dnsname_1 = Dnsname.objects.get(dnsname_name='dnsname_1')
        # login testuser
        login = self.client.login(username='testuser_dnsname', password='TeWFLE2k6lqoC7c6xc0x')
        # get response
        response = self.client.get('/dnsname/' + str(dnsname_1.dnsname_id) + '/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/dnsname/dnsname_detail.html')

    def test_dnsname_detail_get_user_context(self):
        """ test detail view """

        # get object
        dnsname_1 = Dnsname.objects.get(dnsname_name='dnsname_1')
        # login testuser
        login = self.client.login(username='testuser_dnsname', password='TeWFLE2k6lqoC7c6xc0x')
        # get response
        response = self.client.get('/dnsname/' + str(dnsname_1.dnsname_id) + '/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_dnsname')

    def test_dnsname_detail_redirect(self):
        """ test detail view """

        # get object
        dnsname_1 = Dnsname.objects.get(dnsname_name='dnsname_1')
        # login testuser
        login = self.client.login(username='testuser_dnsname', password='TeWFLE2k6lqoC7c6xc0x')
        # create url
        destination = urllib.parse.quote('/dnsname/' + str(dnsname_1.dnsname_id) + '/', safe='/')
        # get response
        response = self.client.get('/dnsname/' + str(dnsname_1.dnsname_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_dnsname_add_not_logged_in(self):
        """ test add view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/dnsname/add/', safe='')
        # get response
        response = self.client.get('/dnsname/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_dnsname_add_logged_in(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_dnsname', password='TeWFLE2k6lqoC7c6xc0x')
        # get response
        response = self.client.get('/dnsname/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_dnsname_add_template(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_dnsname', password='TeWFLE2k6lqoC7c6xc0x')
        # get response
        response = self.client.get('/dnsname/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/dnsname/dnsname_add.html')

    def test_dnsname_add_get_user_context(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_dnsname', password='TeWFLE2k6lqoC7c6xc0x')
        # get response
        response = self.client.get('/dnsname/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_dnsname')

    def test_dnsname_add_redirect(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_dnsname', password='TeWFLE2k6lqoC7c6xc0x')
        # create url
        destination = urllib.parse.quote('/dnsname/add/', safe='/')
        # get response
        response = self.client.get('/dnsname/add', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_dnsname_edit_not_logged_in(self):
        """ test edit view """

        # get object
        dnsname_1 = Dnsname.objects.get(dnsname_name='dnsname_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/dnsname/' + str(dnsname_1.dnsname_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/dnsname/' + str(dnsname_1.dnsname_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_dnsname_edit_logged_in(self):
        """ test edit view """

        # get object
        dnsname_1 = Dnsname.objects.get(dnsname_name='dnsname_1')
        # login testuser
        login = self.client.login(username='testuser_dnsname', password='TeWFLE2k6lqoC7c6xc0x')
        # get response
        response = self.client.get('/dnsname/' + str(dnsname_1.dnsname_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_dnsname_edit_template(self):
        """ test edit view """

        # get object
        dnsname_1 = Dnsname.objects.get(dnsname_name='dnsname_1')
        # login testuser
        login = self.client.login(username='testuser_dnsname', password='TeWFLE2k6lqoC7c6xc0x')
        # get response
        response = self.client.get('/dnsname/' + str(dnsname_1.dnsname_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/dnsname/dnsname_edit.html')

    def test_dnsname_edit_get_user_context(self):
        """ test edit view """

        # get object
        dnsname_1 = Dnsname.objects.get(dnsname_name='dnsname_1')
        # login testuser
        login = self.client.login(username='testuser_dnsname', password='TeWFLE2k6lqoC7c6xc0x')
        # get response
        response = self.client.get('/dnsname/' + str(dnsname_1.dnsname_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_dnsname')

    def test_dnsname_edit_redirect(self):
        """ test edit view """

        # get object
        dnsname_1 = Dnsname.objects.get(dnsname_name='dnsname_1')
        # login testuser
        login = self.client.login(username='testuser_dnsname', password='TeWFLE2k6lqoC7c6xc0x')
        # create url
        destination = urllib.parse.quote('/dnsname/' + str(dnsname_1.dnsname_id) + '/edit/', safe='/')
        # get response
        response = self.client.get('/dnsname/' + str(dnsname_1.dnsname_id) + '/edit', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
