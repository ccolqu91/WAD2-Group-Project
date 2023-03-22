from django.test import TestCase, Client
from django.urls import reverse
from survey_server.models import User,Restaurant, Customer



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
from django.test import TestCase
from .models import Survey, Restaurant, User
from .score import CalculateScore
from .voucher import get_voucher

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
