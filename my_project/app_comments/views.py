from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from app_comments.models import Comment

def index(request):
    comment_list = list(Comment.objects.order_by('text'))
    return render(request, 'comments.html', {
        'comments': comment_list,
    })

def addcomment(request):
	if request.method == 'POST':
		text = request.POST.get('comment')  
		author = request.POST.get('author')            
        comment = Comment(
            text = text,
            author = author
        )
        comment.save()
        return HttpResponseRedirect('/')
