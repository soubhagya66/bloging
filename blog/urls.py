from xml.dom.minidom import Document
from django.urls import path

from my_site.settings import MEDIA_PATH, MEDIA_URL
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path("",views.IndexView.as_view(),name="index"),
    path("post",views.AllBlogView.as_view(),name="all_blog"),
    path("post/<int:id>",views.BlogByNameView.as_view(),name="blog_by_name"),
    path("read-later",views.ReadLaterView.as_view(),name="read-later")

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)\
 +static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)