from django.urls import URLPattern, path
from . import views


urlpatterns =[
    path('getmt-<int:met>:<int:se>', views.perEvent),
    path('save-<int:met>', views.update),
    path('delete-<int:met>:<int:id>',views.delete),
    path('session',views.sess),
]