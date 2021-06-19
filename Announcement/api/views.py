from django.shortcuts import render
from django.http import JsonResponse
from .models import Announcement
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AnnouncementSerializer
# Create your views here.
@api_view(['GET'])
def index(request):
    url={
        'Announcements':'/announcements/',
        'Details View':'/announcement-details/<str:pk>/',
        'Create':'/announcement-create/',
        'Update':'/announcement-update/<str:pk>/',
        'Delete':'/announcement-delete/<str:pk>/'
    }
    return Response(url)
    
@api_view(['GET'])
def AnnouncementList(request):
    announcements=Announcement.objects.all()
    serializer=AnnouncementSerializer(announcements,many=True)  
    return Response(serializer.data)

@api_view(['GET'])
def AnnouncementDetails(request,pk):
    announcements=Announcement.objects.filter(id=pk)
    serializer=AnnouncementSerializer(announcements,many=True)  
    return Response(serializer.data)

@api_view(['POST'])
def AnnouncementCreate(request):
    
    serializer=AnnouncementSerializer(data=request.data)  
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def AnnouncementUpdate(request,pk):
    updatingAnnouncement=Announcement.objects.get(id=pk)
    serializer=AnnouncementSerializer(instance=updatingAnnouncement,data=request.data)  
    if serializer.is_valid():
        
        serializer.save()
    return Response(serializer.data)    
    
@api_view(['DELETE'])
def AnnouncementDelete(request,pk):
    deletingAnnouncement=Announcement.objects.get(id=pk)
    deletingAnnouncement.delete()
    
    return Response("Deleted")    