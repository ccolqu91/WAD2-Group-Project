from django.test import TestCase
from .models import Survey, Restaurant, User
from .score import CalculateScore

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
