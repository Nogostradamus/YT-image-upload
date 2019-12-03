from rest_framework import viewsets
from django.http import HttpResponse
from .serializers import BookSerializer
from .models import Book

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        cover = request.data['cover']
        title = request.data['title']
        Book.objects.create(title=title, cover=cover)
        return HttpResponse({'message': 'Book created'}, status=200)