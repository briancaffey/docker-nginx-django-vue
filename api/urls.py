from django.conf.urls import url, include

from .views import debug_view, visits_view

urlpatterns = [
    url(r'^test/$', debug_view, name="test_view"),
    url(r'^visits/$', visits_view, name="visits_view")
]