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


class RegisterViewTestCase(TestCase):

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
