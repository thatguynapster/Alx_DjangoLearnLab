from django.contrib import admin
from django.urls import path, include
from .relationship_app.views import list_books, libraryDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),
]