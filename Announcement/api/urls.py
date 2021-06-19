from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="Api"),
    path('announcements/',views.AnnouncementList,name="All"),
    path('announcement-details/<str:pk>/',views.AnnouncementDetails,name="Details"),
    path('announcement-create/',views.AnnouncementCreate,name="Create"),
    path('announcement-update/<str:pk>/',views.AnnouncementUpdate,name="Update"),
    path('announcement-delete/<str:pk>/',views.AnnouncementDelete,name="Delete"),
]
