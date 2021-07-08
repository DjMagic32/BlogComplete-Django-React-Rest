from rest_framework import serializers
from .models import BlogPost


class TodoSerializers (serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__' #('id', 'title', 'body')
        lookup_field = 'slug'


# En la parte superior, hemos importado serializadores de Django REST Framework,
# así como nuestro archivo models.py. A continuación creamos una clase TodoSerializer.
# El formato aquí es muy similar a cómo creamos clases o formularios modelo en el propio Django.
# Estamos especificando qué modelo usar y los campos específicos que queremos exponer.
# Recuerde que la identificación es creada automáticamente por Django,
# por lo que no tuvimos que definirla en nuestro modelo Todo,
# pero la usaremos en nuestra vista detallada. Y eso es.
# Django REST Framework ahora transformará mágicamente nuestros datos en JSON exponiendo los campos de identificación,
# título y cuerpo de nuestro modelo Todo.
# Lo último que debemos hacer es configurar nuestro archivo views.py.