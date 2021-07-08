from django.urls import path  # se importan las rutas de Django
# como las urls dependen de las vistas (views), se importan las views tambien
from .views import BlogPostCategoryView, BlogPostDetailView, BlogPostFeaturedView, BlogPostListView


# Se colocan las rutas dentro de 'urlpatterns', no se si es un keyword predefinida por django
urlpatterns = [
    path('', BlogPostListView.as_view()),
    path('featured', BlogPostFeaturedView.as_view()),
    path('category', BlogPostCategoryView.as_view()),
    path('<slug>', BlogPostDetailView.as_view()),
]
# '<int:pk>/' int es un valor entero y pk es la primary key de la base de datos
# Habrá una lista de todos las tareas '(todo)' en la cadena vacía, en otras palabras, en api/.
# Y cada tarea individual estará disponible en su prymary key,
# que es un valor que Django establece automáticamente en cada tabla de la base de datos.
# La primera entrada es 1, la segunda es 2 y así sucesivamente.
# Por lo tanto, nuestra primera tarea('todo') se ubicará eventualmente en el punto final de API api/1/.
