from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import *

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('historical/', HistoricalView.as_view(), name='historical'),
    path('rema/', RemaView.as_view(), name='rema'),
    path('rema/<str:measure>', RemaView.as_view(), name='rema'),
    path('rema/<str:measure>/<str:country>/<str:state>/<str:city>', RemaLocationView.as_view(), name='rema'),
    path("mapJson/", get_map_json, name="mapJson"),
    path("mapJson/<str:measure>", get_map_json, name="mapJson"),
    path("mapJson/<str:measure>/<str:country>/<str:state>/<str:city>", get_map_json_location, name="mapJson"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('historical/data',
         download_csv_data, name='historical-data'),
]
