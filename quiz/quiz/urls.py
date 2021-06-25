"""quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from exam.views import AnswersAPI, OptionsAPI, QuestionsAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('questions', QuestionsAPI.as_view()),
    path('options', OptionsAPI.as_view()),
    path('answers', AnswersAPI.as_view())

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
