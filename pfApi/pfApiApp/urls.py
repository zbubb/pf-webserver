from django.urls import path

from . import views

urlpatterns = [
    path('labels', views.getLabels, name='labels'),
    path('month/<int:monthId>/year/<int:year>/entries', views.getMonthEntries, name='monthEntries'),
    path('month/<int:monthId>/year/<int:year>/overview', views.getMonthOverview, name='monthOverview')
]
