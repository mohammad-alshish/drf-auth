from rest_framework import generics
from .models import Game
from .serializers import BookSerializer
from .permissions import IsOwnerOrReadOnly

class BookList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsOwnerOrReadOnly,)