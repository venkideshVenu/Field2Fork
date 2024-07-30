from django.shortcuts import render,redirect
from healthinfo.models import Article

# Create your views here.
def add_blog(request):
    blogs=Article.objects.all()
    dict={
        'articlesdata':blogs
    }
    return render(request,'temp_healthinfo/add_blog.html',context=dict)

def article_view(request,article_id):
    singlearticle=Article.objects.get(pk=article_id)
    dict={
        'article':singlearticle
    }
    return render(request,'temp_healthinfo/article.html',context=dict)


def save_blog(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        date = request.POST['date']
        title = request.POST['title']
        article = request.POST['article']
        
        article=Article(
            subject=subject,
            date=date,
            title=title,
            article=article
        )
        article.save()
        return redirect('addblog')  # Redirect to a page showing all blog posts
    return render(request, 'temp_healthinfo/add_blog.html')