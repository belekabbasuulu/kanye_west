from django.contrib import admin
from django.urls import path

from quote.views import QuoteAPIViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kanye-sayings/', QuoteAPIViewSet.as_view())
]
