from django.urls import path
from mptt_test.views import create_chapter, chapter_detail, show_chapter
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('chapters/', show_chapter),
    path('create_chapters/', create_chapter, name='create_chapters'),
    path('chapter_detail/<str:chapter_name>/', chapter_detail, name='chapter_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)