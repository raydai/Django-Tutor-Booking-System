from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
   # url(r'^search$', ListView.as_view(queryset=Tutor.objects.all(), template_name='mainApp/search.html')),
    url(r'^search$', views.search, name='search' ),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^bookings$', views.bookings, name='bookings'),
    url(r'^wallet$', views.wallet, name='wallet'),
    url(r'^book$', views.book, name='book'),
    url(r'^confirmation$', views.confirmation, name='confirmation'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)