from django.conf.urls import url

from mysql.views import *
from . import views

urlpatterns = [
    url(r'^tools.html$', views.tools, name='tools'),
    url(r'^tools_todo.html$', views.tools_todo, name='tools_todo'),
    url(r'^tools_done.html$', views.tools_done, name='tools_done'),
    url(r'^tools-add.html$', views.tools_add, name='tools_add'),
    url(r'^tools-del.html$', views.tools_delete, name='tools_delete'),
    # url(r'^tools-bulk-del.html$', views.tools_bulk_delte, name='tools_bulk_delte'),
    url(r'^tools-update-(?P<nid>\d+).html$', views.tools_update, name='tools_update'),
    url(r'^tools/success/$', scripts_success, name='scripts_success'),
]
