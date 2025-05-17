"""
URL Configuration for Smart Irrigation System
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def api_root(request):
    """
    Root view that provides information about available API endpoints
    """
    api_info = {
        'name': 'Smart Irrigation System API',
        'version': '1.0',
        'endpoints': {
            'irrigation_decision': '/api/irrigation/decision/',
            'irrigation_history': '/api/irrigation/history/',
            'export_history_csv': '/api/irrigation/export-csv/',
            'crop_soil_data': '/api/crops/',
        },
        'documentation': 'See README.md for more details'
    }
    return JsonResponse(api_info)

urlpatterns = [
    path('', api_root, name='api_root'),  # Root URL now shows API information
    path('admin/', admin.site.urls),
    path('api/', include('sis.core.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='admin/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
]
