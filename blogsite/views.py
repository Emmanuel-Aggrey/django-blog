from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.views.generic import ListView,DetailView,TemplateView,CreateView
from django.views.generic.dates import MonthArchiveView
from  django.views.generic.dates import  MonthArchiveView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from  django.db.models import  Q
from .models import Category,Subcategory,Article,CustomUser
from datetime import datetime,timedelta
from django.utils import timezone

# Create your views here.



def ArticleList(request):
    navbar_items  = Category.objects.all()
   
    headlines = Article.objects.filter(active=True).order_by('-date_updated')
    latestnews = Article.objects.filter(date_updated__month=datetime.now().strftime('%m'))
 

    #  Article.objects.order_by('-date_updated')[0]
    # paginating
    paginator = Paginator(headlines, 2)
    page = request.GET.get('page')
    try:
        headlines_pag= paginator.page(page)
    except PageNotAnInteger:
        headlines_pag = paginator.page(1)
    except EmptyPage:
        headlines_pag = paginator.page(paginator.num_pages)
    context = {
    'navbar_items':navbar_items,
    'headlines_scroll':headlines,
    'headlines_pag':headlines_pag,
    'latestnews':latestnews,
    'trending':headlines.filter(total_views__gte=2).order_by('-total_views'),
    }

    return render(request,'blog/article_list.html',context)



def articleDetail(request,slug,id):
    article = get_object_or_404(Article,slug=slug)
    total_views = int(article.total_views )
    total_views +=1
    
    Article.objects.filter(id=id).update(total_views=total_views)

    navbar_items  = Category.objects.all()
    popular_post =  Article.objects.exclude(slug=slug).filter(total_views__gte=10)
    context = {
        'navbar_items':navbar_items,
        'articles':article,
        'popular_post':popular_post,
    }
    return render(request,'blog/article_datail.html',context)

def  articleCategory(request,category,id):
    navbar_items = Category.objects.all()
    category = get_object_or_404(Subcategory,id=id)

    articles = category.articles.order_by('-date_updated')
    popular_post = category.articles.filter(total_views__gte=10).order_by('-total_views')

     # paginating
    paginator = Paginator(articles, 10)
    page = request.GET.get('page')
    try:
        articles_pag= paginator.page(page)
    except PageNotAnInteger:
        articles_pag = paginator.page(1)
    except EmptyPage:
        articles_pag = paginator.page(paginator.num_pages)
    
    context = {
        'navbar_items':navbar_items,
        'article':articles_pag,
        'category':category,
        'popular_post':popular_post,
       
    }

    return render(request,'blog/article_category.html',context)
    

def search_article(request):
    navbar_items = Category.objects.all()
    article = Article.objects.order_by('-date_updated')

    q = request.GET.get('q')
    if q:

        article =article.filter(Q(subcategory__name__icontains=q)|Q(title__icontains=q))
    context = {
        'navbar_items':navbar_items,
        'article':article,
        'popular_post':Article.objects.filter(total_views__gte=2).order_by('-total_views')

    }
    return render(request,'blog/search.html',context)


# filters all posts with the specific tag
def tag_posts(request, tags):
    # posts = Post.objects.filter(tagged_items=tags)
    # url_tag = str(request.GET('tags')).lower
    # tag = get_object_or_404(Tag, tags)  # get the tags from the url
    article = Article.objects.filter(tags__name__in=[tags]).distinct()
    context = {
        'navbar_items': Category.objects.all(),
        'article': article,
        'post_tag': tags,
        'popular_post':Article.objects.filter(total_views__gte=2).order_by('-total_views')

    }
    return render(request, 'blog/tag_posts.html', context)

def author_list(request, author):
    author = get_object_or_404(CustomUser,username=author)
    author_writing = Article.objects.filter(created_by=author)
    
    # paginating
    paginator = Paginator(author_writing, 10)
    page = request.GET.get('page')
    try:
        author_writings= paginator.page(page)
    except PageNotAnInteger:
        author_writings = paginator.page(1)
    except EmptyPage:
        author_writings = paginator.page(paginator.num_pages)

    

    context = {
        'navbar_items': Category.objects.all(),
        'author_writings': author_writings,
        'created_by':author,
        'popular_post':Article.objects.filter(total_views__gte=2).order_by('-total_views')

    }
    return render(request, 'blog/author_articles.html', context)


class ArticleMonthArchiveView(MonthArchiveView):
    queryset = Article.objects.all()
    date_field = "date_updated"
    allow_future = True
    template_name = 'blog/month_archive.html'