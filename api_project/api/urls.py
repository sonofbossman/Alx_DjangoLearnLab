from django.urls import path
from api.views import BookList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
  path('books/', BookList.as_view(), name='book-list'), # Maps to the BookList view
#   path('<int:pk>', BookDetails.as_view(), name='book-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)