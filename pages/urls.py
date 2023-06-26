from django.urls import path

from portfolio.pages.views import HomeView, AboutView, ContactUsView, ProjectsView, ProjectView, SkillsView

urlpatterns = [
    path('home/', HomeView.as_view()),
    path('', HomeView.as_view(), name='home'),
    path('about-us/', AboutView.as_view(), name='about'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('contact-us/', ContactUsView.as_view(), name='contact_us'),
    path('projects/<slug:slug>/', ProjectView.as_view(), name='project'),
    path('skills/', SkillsView.as_view(), name='skills'),
]
