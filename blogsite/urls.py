from django.urls import path
from .import views

app_name ='blogsite'
urlpatterns = [
    # path('',views.ArticleListView.as_view(),name='home'),
    path('',views.ArticleList,name='home'),
    path('category/<int:id>/<str:category>/',views.articleCategory,name='category'),
    path('detail/<slug:slug>/<int:id>/',views.articleDetail,name='detail'),
    path('search_article',views.search_article,name='search'),
    path('post_tags/<str:tags>/',views.tag_posts,name='post_tags'),
    path('author/<str:author>/',views.author_list,name='author_list'),
    path('<int:year>/<str:month>/', views.ArticleMonthArchiveView.as_view(), name="archive_month"),
    
]