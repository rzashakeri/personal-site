from django.urls import path
from django.views.decorators.cache import cache_page

from pages.views import HomeView, AboutView, ContactUsView, ProjectsView, ProjectView, SkillsView

urlpatterns = [
    path('', cache_page(60*60)(HomeView.as_view()), name='index'),
    path('home/', cache_page(60*60)(HomeView.as_view()), name='home'),
    path('about-us/', cache_page(60*60)(AboutView.as_view()), name='about'),
    path('projects/', cache_page(60*60)(ProjectsView.as_view()), name='projects'),
    path('contact-us/', cache_page(60*60)(ContactUsView.as_view()), name='contact_us'),
    path('projects/<slug:slug>/', cache_page(60*60)(ProjectView.as_view()), name='project'),
    path('skills/', cache_page(60*60)(SkillsView.as_view()), name='skills'),
]
