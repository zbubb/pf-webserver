from django.urls import path

from . import views

urlpatterns = [
    path('label', views.createLabel, name='createLabel'),
    path('labels', views.getLabels, name='getLabels'),
    path('month/<int:monthId>/year/<int:year>/entries', views.getMonthEntries, name='monthEntries'),
    path('month/<int:monthId>/year/<int:year>/overview', views.getMonthOverview, name='monthOverview'),
    path('month/entry/create', views.createMonthEntry, name='createMonthEntry'),
    path('month/entry/<int:entryId>', views.getMonthEntry, name='monthEntry'),
    path('month/entry/<int:entryId>/edit', views.editMonthEntry, name='editMonthEntry'),
]
