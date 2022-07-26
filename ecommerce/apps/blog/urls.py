from . import views
from django.urls import path

app_name = "blog"

urlpatterns =[

	path('/', views.blog_main, name='blog_main'),
	path('<slug:post>/', views.read_post, name='read_post'),
	path('category/<category>', views.CatListView.as_view(), name='category')

]