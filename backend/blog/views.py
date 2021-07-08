from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import BlogPost
from .serializers import TodoSerializers
# Create your views here.

class BlogPostListView(ListAPIView):
    queryset = BlogPost.objects.order_by('-date_created')
    serializer_class = TodoSerializers
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class BlogPostDetailView(RetrieveAPIView):
    queryset = BlogPost.objects.order_by('-date_created')
    serializer_class = TodoSerializers
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class BlogPostFeaturedView(ListAPIView):
    queryset = BlogPost.objects.all().filter(featured=True)
    serializer_class = TodoSerializers
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class BlogPostCategoryView(APIView):
    serializer_class = TodoSerializers
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data
        category = data['category']
        queryset = BlogPost.objects.order_by('-date_created').filter(category__iexact=category)

        serializer = TodoSerializers(queryset, many=True)

        return Response(serializer.data)


# En la parte superior, importamos vistas genéricas de Django REST Framework
# y nuestros archivos models.py y serializers.py.
# Recuerde de nuestro archivo todos/urls.py que tenemos dos rutas y, por lo tanto, dos vistas distintas.
# Usaremos ListAPIView para mostrar todos los todos y RetrieveAPIView para mostrar una única instancia de modelo.
# Los lectores astutos notarán que hay un poco de redundancia en el código aquí.
# Básicamente, repetimos queryset y serializer_class para cada vista, aunque la vista genérica extendida es diferente.
# Más adelante en el libro aprenderemos sobre conjuntos de vistas y enrutadores que abordan este problema y nos permiten crear las mismas vistas de API y URL con mucho menos código.
# ¡Pero por ahora hemos terminado! Nuestra API está lista para consumir.
# Como puede ver, la única diferencia real entre Django REST Framework y Django es que con Django REST Framework necesitamos agregar un archivo serializers.py y no necesitamos un archivo de plantillas.
# De lo contrario, los archivos urls.py y views.py actúan de manera similar.
