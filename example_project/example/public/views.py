from django.conf import settings
from django.core.urlresolvers import reverse
from django.views.generic import RedirectView, TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class SignUpView(RedirectView):
    def get_redirect_url(self):
        return '{url}?next={next}'.format(
            url=settings.OIDC_RP_SIGNUP_URL,
            next=self.request.build_absolute_uri(reverse('oidc_auth_request')))