from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Division
import urllib.parse

class DivisionViewTestCase(TestCase):
    """ division view tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Division.objects.create(division_name='division_1')
        # create user
        test_user = User.objects.create_user(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')

    def test_division_list_not_logged_in(self):
        """ test list view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/division/', safe='')
        # get response
        response = self.client.get('/division/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_division_list_logged_in(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')
        # get response
        response = self.client.get('/division/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_division_list_template(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')
        # get response
        response = self.client.get('/division/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/division/division_list.html')

    def test_division_list_get_user_context(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')
        # get response
        response = self.client.get('/division/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_division')

    def test_division_list_redirect(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')
        # create url
        destination = urllib.parse.quote('/division/', safe='/')
        # get response
        response = self.client.get('/division', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_division_detail_not_logged_in(self):
        """ test detail view """

        # get object
        division_1 = Division.objects.get(division_name='division_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/division/' + str(division_1.division_id) + '/', safe='')
        # get response
        response = self.client.get('/division/' + str(division_1.division_id) + '/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_division_detail_logged_in(self):
        """ test detail view """

        # get object
        division_1 = Division.objects.get(division_name='division_1')
        # login testuser
        login = self.client.login(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')
        # get response
        response = self.client.get('/division/' + str(division_1.division_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_division_detail_template(self):
        """ test detail view """

        # get object
        division_1 = Division.objects.get(division_name='division_1')
        # login testuser
        login = self.client.login(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')
        # get response
        response = self.client.get('/division/' + str(division_1.division_id) + '/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/division/division_detail.html')

    def test_division_detail_get_user_context(self):
        """ test detail view """

        # get object
        division_1 = Division.objects.get(division_name='division_1')
        # login testuser
        login = self.client.login(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')
        # get response
        response = self.client.get('/division/' + str(division_1.division_id) + '/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_division')

    def test_division_detail_redirect(self):
        """ test detail view """

        # get object
        division_1 = Division.objects.get(division_name='division_1')
        # login testuser
        login = self.client.login(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')
        # create url
        destination = urllib.parse.quote('/division/' + str(division_1.division_id) + '/', safe='/')
        # get response
        response = self.client.get('/division/' + str(division_1.division_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_division_add_not_logged_in(self):
        """ test add view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/division/add/', safe='')
        # get response
        response = self.client.get('/division/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_division_add_logged_in(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')
        # get response
        response = self.client.get('/division/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_division_add_template(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')
        # get response
        response = self.client.get('/division/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/division/division_add.html')

    def test_division_add_get_user_context(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')
        # get response
        response = self.client.get('/division/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_division')

    def test_division_add_redirect(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')
        # create url
        destination = urllib.parse.quote('/division/add/', safe='/')
        # get response
        response = self.client.get('/division/add', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_division_edit_not_logged_in(self):
        """ test edit view """

        # get object
        division_1 = Division.objects.get(division_name='division_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/division/' + str(division_1.division_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/division/' + str(division_1.division_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_division_edit_logged_in(self):
        """ test edit view """

        # get object
        division_1 = Division.objects.get(division_name='division_1')
        # login testuser
        login = self.client.login(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')
        # get response
        response = self.client.get('/division/' + str(division_1.division_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_division_edit_template(self):
        """ test edit view """

        # get object
        division_1 = Division.objects.get(division_name='division_1')
        # login testuser
        login = self.client.login(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')
        # get response
        response = self.client.get('/division/' + str(division_1.division_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/division/division_edit.html')

    def test_division_edit_get_user_context(self):
        """ test edit view """

        # get object
        division_1 = Division.objects.get(division_name='division_1')
        # login testuser
        login = self.client.login(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')
        # get response
        response = self.client.get('/division/' + str(division_1.division_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_division')

    def test_division_edit_redirect(self):
        """ test edit view """

        # get object
        division_1 = Division.objects.get(division_name='division_1')
        # login testuser
        login = self.client.login(username='testuser_division', password='tcrayKsMKw7T6SGBKYgA')
        # create url
        destination = urllib.parse.quote('/division/' + str(division_1.division_id) + '/edit/', safe='/')
        # get response
        response = self.client.get('/division/' + str(division_1.division_id) + '/edit', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
