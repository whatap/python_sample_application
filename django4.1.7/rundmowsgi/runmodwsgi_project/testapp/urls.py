from django.urls import path
from . import views

urlpatterns = [
    ##f0
    # path("", views.app_main, name='app_main'),
    # path("test", views.test, name="test"),
    path("url1", views.url1, name="url1"),
    path("url2", views.url2, name="url2"),
    # path(path_config.f0_example, views.example, name='f0_example'),
    ##f7
    # path(path_config.f7_transaction_detail, views.f7_transaction_detail, name='f7_transaction_detail'),
]

