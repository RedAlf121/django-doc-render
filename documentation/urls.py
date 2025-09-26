from django.urls import path, re_path
from .views import MarkDownRenderView
import re
urlpatterns = [
    path('',MarkDownRenderView.as_view(),name='docs'),
    re_path(r'^(?P<file>.+)$', MarkDownRenderView.as_view(), name='docs-link')

]