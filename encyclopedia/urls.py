from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entryPage, name="entry"),
    path("pageNotFound/", views.pageNotFound, name="pageNotFound"),
    path("search/", views.searchEntry, name="search"),
    path("newPage/", views.newPage, name="newPage"),
    path("editPage/<str:title>", views.editPage, name="editPage"),
    path("saveChanges/", views.saveChanges, name="saveChanges"),
    path("randomPage/", views.randomPage, name="randomPage")
]
