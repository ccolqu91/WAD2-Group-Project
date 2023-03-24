from django.test import TestCase, Client,SimpleTestCase
from django.urls import reverse,resolve
from survey_server.models import User,Restaurant, Customer, Survey
from survey_server.views import *
from .score import CalculateScore
from .voucher import get_voucher




# Test for log in
class TestForLogin(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('survey_server:login')
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_valid_login(self):
        response = self.client.post(self.url, {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('survey_server:index'))

    def test_invalid_login(self):
        response = self.client.post(self.url, {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200) 
        self.assertContains(response, "Invalid login details supplied.")

    def tearDown(self):
        self.user.delete()


# Test for edit restaurant
def edit_restaurant_test(self):
    restaurant = Restaurant.objects.create(manager=self.user)
    form_data = {
        'name': 'New Restaurant Name',
        'about': 'New Restaurant Description',
        'voucher_value': 10,
    }
    form = restaurant(data=form_data, files={}, instance=restaurant)

    self.assertTrue(form.is_valid())
    form.save()

    restaurant.refresh_from_db()
    self.assertEqual(restaurant.name, 'New Restaurant Name')
    self.assertEqual(restaurant.about, 'New Restaurant Description')
    self.assertEqual(restaurant.voucher_value, 10)


class RegisterTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = '/register/'

    def test_register_with_valid_data(self):
        data = {
            'username': 'testuser',
            'password1': 'testpass123',
            'password2': 'testpass123',
            'user_type': 1,
        }
        response = self.client.post(self.url, data)
        self.assertFalse(User.objects.filter(username='testuser').exists())
        self.assertFalse(Customer.objects.filter(user__username='testuser').exists())

    def test_register_with_invalid_data(self):
        data = {}
        response = self.client.post(self.url, data)
        self.assertFalse(User.objects.filter(username='testuser').exists())
        self.assertFalse(Customer.objects.filter(user__username='testuser').exists())
    # Once you have successfully registered, you should be able to log in.
    def test_login_with_valid_data(self):
        User.objects.create_user(username='testuser', password='testpass123')
        response = self.client.post('/login/', {'username': 'testuser', 'password': 'testpass123'})
        self.assertEqual(response.status_code, 404)

class ScoreTestCase(TestCase):
    def test_negative_scores(self):
        
        manager_user = User.objects.create(username='test_manager', user_type=2)
        
        customer_user = User.objects.create(username='test_customer', user_type=1)
        
        restaurant = Restaurant.objects.create(name="test restaurant", manager=manager_user)
    
        survey = Survey.objects.create(
            restaurant=restaurant,
            customer=customer_user,
            time_starter="slow",
            size_starter="no",
            presentation_starter="No",
            variety_starter="No",
            time_maincourse="slow",
            size_maincourse="no",
            presentation_maincourse="No",
            variety_maincourse="No",
            time_dessert="slow",
            size_dessert="no",
            presentation_dessert="No",
            variety_dessert="No",
            time_drink="slow",
            size_drink="no",
            presentation_drink="No",
            variety_drink="No",
            greeting_entry="No",
            greeting_waiting="No",
            greeting_clean="No",
            greeting_order="no",
            restroom_clean="No",
            missing_restroom="no",
            clean_restaurant="very bad",
            pay_bill_restaurant="very bad",
            service_staff="No",
        )

        scores = CalculateScore(survey)

        self.assertEqual(scores[0], 0)
        self.assertEqual(scores[1], 0)
        self.assertEqual(scores[2], 0)
        self.assertEqual(scores[3], 0)
        self.assertEqual(scores[4], 0)

class GetVoucherTestCase(TestCase):
    def test_voucher_length(self):
        voucher = get_voucher()
        self.assertEqual(len(voucher), 7)


class LoginTemplateTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('survey_server:login')
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_login_page_loads_successfully(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'survey_server/login.html')

    def test_login_successful(self):
        data = {'username': 'testuser', 'password': 'testpass'}
        response = self.client.post(self.url, data=data)
        self.assertRedirects(response, reverse('survey_server:index'))

    def test_login_unsuccessful(self):
        data = {'username': 'wronguser', 'password': 'wrongpass'}
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 200)



class TestForCustomerTemplate(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.customer = Customer.objects.create(user=self.user)
        self.client.login(username='testuser', password='testpass')

    def test_dashboard_view(self):
        url = reverse('survey_server:customer')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)



# Test if index.html show correst navigation bar

class TestForIndex(TestCase):
    
    def test_navbar_display(self):
        client = Client()        
        response = client.get(reverse('survey_server:index'))        
        self.assertContains(response, 'Survey server')
        self.assertContains(response, 'Profile')
        self.assertContains(response, 'About')
        self.assertContains(response, 'Log in')
        self.assertContains(response, 'Register')



class RegisteTemplateTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        
    def test_register_view(self):
        response = self.client.get(reverse('survey_server:register'))
        self.assertTemplateUsed(response, 'survey_server/register.html')
        


class URLtest(SimpleTestCase):
    def test_index_url(self):
        url = reverse('survey_server:index')
        self.assertEqual(resolve(url).func, index)
        
    def test_customer_url(self):
        url = reverse('survey_server:customer')
        self.assertEqual(resolve(url).func, customer)
        
    def test_manager_url(self):
        url = reverse('survey_server:manager')
        self.assertEqual(resolve(url).func, manager)
        
    def test_profile_url(self):
        url = reverse('survey_server:profile')
        self.assertEqual(resolve(url).func, profile)
        
    def test_survey_url(self):
        url = reverse('survey_server:survey', args=['test-restaurant', 1])
        self.assertEqual(resolve(url).func, survey)
        
    def test_survey_success_url(self):
        url = reverse('survey_server:survey_success', args=['test-restaurant', 1])
        self.assertEqual(resolve(url).func, survey_success)
        
    def test_login_url(self):
        url = reverse('survey_server:login')
        self.assertEqual(resolve(url).func, user_login)
        
    def test_register_url(self):
        url = reverse('survey_server:register')
        self.assertEqual(resolve(url).func, register)
        
    def test_logout_url(self):
        url = reverse('survey_server:logout')
        self.assertEqual(resolve(url).func, user_logout)
        
    def test_select_restaurant_url(self):
        url = reverse('survey_server:select')
        self.assertEqual(resolve(url).func, select_restaurant)
        
    def test_about_url(self):
        url = reverse('survey_server:about')
        self.assertEqual(resolve(url).func, about)
        
    def test_add_restaurant_url(self):
        url = reverse('survey_server:add_restaurant')
        self.assertEqual(resolve(url).func, add_restaurant)
        
    def test_edit_restaurant_url(self):
        url = reverse('survey_server:edit_restaurant')
        self.assertEqual(resolve(url).func, edit_restaurant)