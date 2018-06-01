from django.conf.urls import url
from django. contrib import admin

from bookmark.views import BookmarkLV, BookmarkDV

urlpatterns = [
        url(r'^$', BookmarkLV.as_view(), name='index'),
        url(r'^(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),
        ]

