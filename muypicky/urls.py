#from django.conf.urls import url, include
from django.urls import include, path
from django.contrib import admin
from django.views.generic import TemplateView


from django.contrib.auth.views import LoginView, LogoutView

from menus.views import HomeView, AllUserRecentItemListView
from profiles.views import ProfileFollowToggle, RegisterView, activate_user_view

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',HomeView.as_view(),name='home'),
    path('recent/',AllUserRecentItemListView.as_view(),name='recent'),
    path('register/',RegisterView.as_view(),name='register'),
    path('activate/<int:code>/', activate_user_view, name='activate'),

    #path('activate/(?P<code>[a-z0-9].*)/', activate_user_view, name='activate'),

    # url(r'^recent/$', AllUserRecentItemListView.as_view(), name='recent'),
    # url(r'^register/$', RegisterView.as_view(), name='register'),
    # url(r'^activate/(?P<code>[a-z0-9].*)/$', activate_user_view, name='activate'),

    # url(r'^u/', include('profiles.urls', namespace='profiles')),
    # url(r'^items/', include('menus.urls', namespace='menus')),
    # url(r'^restaurants/', include('restaurants.urls', namespace='restaurants')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile-follow/', ProfileFollowToggle.as_view(), name='follow'),
    path('u/', include('profiles.urls',namespace='profiles')),
    path('items/', include('menus.urls', namespace='menus')),
    path('restaurants/', include('restaurants.urls',namespace='restaurants')),
    path('about/',TemplateView.as_view(template_name='about.html'),name='about'),
    path('contact/',TemplateView.as_view(template_name='contact.html'),name='contact'),

#    url(r'^admin/', admin.site.urls),
    # url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^recent/$', AllUserRecentItemListView.as_view(), name='recent'),
    # url(r'^register/$', RegisterView.as_view(), name='register'),
    # url(r'^activate/(?P<code>[a-z0-9].*)/$', activate_user_view, name='activate'),
    # url(r'^login/$', LoginView.as_view(), name='login'),
    # url(r'^logout/$', LogoutView.as_view(), name='logout'),
    # url(r'^profile-follow/$', ProfileFollowToggle.as_view(), name='follow'),
    # url(r'^u/', include('profiles.urls', namespace='profiles')),
    # url(r'^items/', include('menus.urls', namespace='menus')),
    # url(r'^restaurants/', include('restaurants.urls', namespace='restaurants')),
    # url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    # url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
]
