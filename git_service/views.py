from django.views.generic import TemplateView
from allauth.socialaccount.models import SocialAccount
from requests import get


class HomePage(TemplateView):
    template_name = 'home_page.html'
    social_account = None

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.social_account = SocialAccount.objects.get(user_id__exact=request.user.id).extra_data
            print(self.social_account)
        return super(HomePage, self).get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(HomePage, self).get_context_data(*args, **kwargs)
        if self.social_account:
            r = get(self.social_account.get('repos_url'))
            repos = r.json()
            context['social_account_repos'] = repos
        return context
