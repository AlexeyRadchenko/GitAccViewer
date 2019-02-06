from django.test import TestCase
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import User
from django.test import Client


class HomePageViewTestCase(TestCase):
    def setUp(self):
        testuser = User(id=1, username='AlexeyRadchenko', is_active=True)
        test_social_account = SocialAccount.objects.create(user_id=1, extra_data={
            "login": "AlexeyRadchenko",
            "repos_url": "https://api.github.com/users/AlexeyRadchenko/repos"
        })
        testuser.save()
        test_social_account.save()

    def test_home_page_anonymous(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.context.get('social_account_repos'))

    def test_home_page_auth_user(self):
        c = Client()
        user = User.objects.get(username='AlexeyRadchenko')
        c.force_login(user)
        response = c.get('/')
        self.assertIsNotNone(response.context.get('social_account_repos'))
