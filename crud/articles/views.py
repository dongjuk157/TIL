from articles.models import Article,Comment
from articles.forms import ArticleForm, CommentForm
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods, require_safe

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.all()
    context={
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@require_http_methods(['GET','POST'])
def create(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html',context)

@require_safe
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context={
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)

@require_http_methods(['GET','POST'])
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:
        if request.method == "POST":
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article_pk)
        else:
            form = ArticleForm(instance=article)
        context={
            'form': form,
        }
        return render(request, 'articles/update.html', context)
    else:
        return redirect('articles:detail', article_pk)    

@require_POST
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    #article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:
        article.delete()
        return redirect('articles:index')
    # 삭제안된다는 알람
    return redirect('articles:detail', article_pk)


@require_POST
def comment(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
        return redirect('articles:detail', article_pk)
    else:
        return redirect('accounts:login')

@require_POST    
def comment_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()
        return redirect('articles:detail', article_pk)
    else:
        return redirect('accounts:login')
