from django.urls import path
from . import views

urlpatterns = [
    path('', views.WatchList.as_view(), name='api_home_view'),
    path('<int:pk>', views.WatchList_Details.as_view(), name='watchlist_details'),
    
    path('platforms/', views.StreamPlatformList.as_view(), name='stream_platforms'),
    path('platform/<int:pk>/', views.StreamPlatform_details.as_view(), name='stream_platform_details')
    
]
