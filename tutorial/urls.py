from django.urls import path, include

urlpatterns = [
    # path('admin/', include('django.contrib.admin')),
    path('', include('snippets.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
