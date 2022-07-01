from django.urls import re_path
from .views import SearchAPI, DetailSearchAPI

urlpatterns = [
    re_path(r"search/(?P<slug>[\w%20+]+)/$", SearchAPI.as_view(), name="search-detail"),
    re_path(r"search-detail/(?P<slug>[\w%20+]+)/$", DetailSearchAPI.as_view(), name="detail-music")
]
