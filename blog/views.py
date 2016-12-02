from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import post
from .forms import PostForm

# Create your views here.
def post_list(request):
	posts = post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#	posts = post.objects.all()
	return render(request, 'blog/post_list.html', {'posts': posts})
	
def post_detail(request, pk):
    prost = get_object_or_404(post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': prost})
    
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})
	
def post_edit(request, pk):
	prost = get_object_or_404(post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=prost)
		if form.is_valid():
			prost = form.save(commit=False)
			prost.author = request.user
			prost.published_date = timezone.now()
			prost.save()
			return redirect('post_detail', pk=prost.pk)
	else:
		form = PostForm(instance=prost)
	return render(request, 'blog/post_edit.html', {'form': form})