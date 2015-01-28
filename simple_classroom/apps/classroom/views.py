from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import View
from site_news.models import NewsItem


class HomeView(View):
    template_name = 'classroom/home.html'

    def get(self, request, *args, **kwargs):
        site = request.site
        news = NewsItem.objects_published.get_latest_by_site(site=site)
        menu_name = site.extendedsite.menu.alias
        return render_to_response(
            self.template_name,
            RequestContext(self.request, {'site': site, 'news': news, 'menu_name': menu_name})
        )


class ProfileView(View):
    template_name = 'classroom/profile.html'

    def get(self, request, *args, **kwargs):
        site = request.site
        news = NewsItem.objects_published.get_latest_by_site(site=site)
        menu_name = site.extendedsite.menu.alias

        try:
            profile = request.user.studentprofile
            profile_type = 'student'
        except:
            try:
                profile = request.user.teacherprofile
                profile_type = 'teacher'
            except:
                profile = None
                profile_type = None

        return render_to_response(
            self.template_name,
            RequestContext(self.request, {'site': site, 'news': news, 'menu_name': menu_name, 'profile': profile, 'profile_type': profile_type})
        )

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileView, self).dispatch(*args, **kwargs)
