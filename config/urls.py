"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from django.conf import settings
# path는 url pattern을 단순화하여 작성하고, converter를 사용하는 함수
# re_path는 이전 버전의 url 함수와 같은데, url pattern을 작성할 때, reqexp 정규표현식을 사용해서 표현하는 함수이다.


urlpatterns = [
    path('site_config/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # S3 사용안할 때만 사용
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),

    path('', include('post.urls')),
]

# # 디버그 모드일 때만 작성
# from django.conf import settings
#
# if settings.DEBUG:
#     from django.conf.urls.static import static
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
