from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

# Create your views here.

class PostListView(ListView):
	queryset = Post.published.all()
	context_object_name = 'posts'
	paginate_by = 6
	template_name = 'pages/blog-list.html'


def post_list(request):
	object_list = Post.published.all()
	paginator = Paginator(object_list, 3)# 3 posts in each page
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		#If page is not an integer deliver the first page
		posts = paginator.page(1)
	except EmptyPage:
		# If page is out of range deliver last page of results
		posts = paginator.page(paginator.num_pages)
	return render(request, 'pages/blog-list.html', {'page': page, 'posts': posts})

def post_detail(request, year, month, day, slug):
	post = get_object_or_404(Post, slug=slug, status='published', publish__year=year, publish__month=month, publish__day=day)
	return render(request, 'pages/blog-detail.html', {'post': post})


# def post_share(request, post_id):
# 	Retrieve post by id
# 	post = get_object_or_404(Post, id=post_id, status='published')
# 	sent = False
# 	if request.method == 'POST':
# 		#Form was submitted
# 		form = EmailPostForm(request.POST)
# 		if form.is_valid():
# 			cd = form.cleaned_data
# 			post_url = rewuest.build_absolute_uri(post.get_absolute_url())
# 			subject = '{}({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
# 			message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
# 			send_mail(subject, message, 'admin@xxxx.com', [cd['to']])
# 			sent = True
#  		else:
# 		    form = EmailPostForm()
# 		return render(request, 'blog/post/dhare.html', {'post': post, 'form': form, 'sent': sent})
