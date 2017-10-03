
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^accounts/', include("accounts.urls", namespace = "accounts")),
    url(r'^$', login_required(TemplateView.as_view(template_name="home.html"))),
]
