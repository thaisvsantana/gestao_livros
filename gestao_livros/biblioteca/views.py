from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework import filters
from .models import Autor, Livro 
from .serializers import AutorSerializer, LivroSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, DjangoModelPermissions

class AutorViewSet (viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome']
    
    def create(self, request, *args, **kwargs):
        if Autor.objects.filter(nome=request.data.get('nome')).exists():
            return Response({"detail": "Autor já existe."}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)
    
class LivroViewSet (viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo', 'autor_nome']
    
    @action(detail=True, methods=['patch'])
    def atualizar_titulo(self, request, pk=None):
           livro = self.get_object()
           livro.titulo = request.data.get('titulo')
           livro.save()
           return Response({'status': 'Título atualizado!'})
            
    
