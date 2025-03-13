from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.adapter import DefaultAccountAdapter
from django.shortcuts import reverse
import logging
from .views import *
logger = logging.getLogger(__name__)


class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request, sociallogin):
        """Prevent new users from signing up via Google."""
        return False  # Only existing users can link their account

    def get_connect_redirect_url(self, request, socialaccount):
        """Redirect users to the quiz page after linking Google."""
        return reverse('submit_quiz')

    def get_login_redirect_url(self, request):
        """Ensure users go directly to the quiz after login."""
        return reverse('dashboard')


class MyAccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        """Allow signup only via the normal form, not Google."""
        return True

    def get_login_redirect_url(self, request):
        user = request.user
        if user.is_authenticated and user.last_login is None:
            return reverse('submit_quiz')  # First-time login → quiz
        return reverse('dashboard')  # Returning users → dashboard

