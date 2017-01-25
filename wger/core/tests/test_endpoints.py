import json
from django.urls import reverse
from rest_framework import status
from wger.core.tests.base_testcase import WorkoutManagerTestCase
from django.contrib.auth.models import User


class UserEndpointTests(WorkoutManagerTestCase):
    def test_adds_user(self):
        """
Ensure we can create a new User object
        """
        url = reverse('core:user:add')
        data = {'name': 'Boniface'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, 'Boniface')

    def view_users(self):
        response = self.client.get('/user/1/')
        self.assertEqual(json.loads(response.content), {
                         'id': 1, 'username': "boniface"})
