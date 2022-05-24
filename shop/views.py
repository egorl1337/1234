
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.views.generic.edit import UpdateView
from requests import request
from .models import Comment, Comments
from .forms import CommentForm, CommentsForm
from .models import Items

# Create your views here.


def New_detail_view(request, Items):
    class New_detail_view(DetailView):
        model = Items
        template_name = 'shop/detail_view.html'
        context_object_name = 'Items'
    items = get_object_or_404(Items, slug=items)
    comments = Items.Comments.filter(active=True)
    comments_form = CommentsForm(data=request.POST)
    
    if request.method == "POST":
        
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.items = items
            new_comment.author = request.user
            new_comment.save()
    else:
        form = CommentsForm()
    return render(request, 'shop/detail_view.html', {'items':items, 'comments':comments, 'comments_form':comments_form})



class comments_delete(DeleteView):
    model = Comment
    template_name = 'shop/comments_delete.html'
    success_url = '/shop/comments'
    context_object_name = 'Comment'



class comments_edit(UpdateView):
    model = Comment
    template_name = 'shop/comments_edit.html'
    success_url = '/shop/comments'
    #form_class = CommentForm
    fields = ['text']
    template_name_suffix = '_update_form'



    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.get(pk=self.kwargs['pk'])
        return context
    


def index_shop(request):
    items_dict = Items.objects.all()
    return render(request, 'shop\shop_home.html', {'items_dict':items_dict})

def comments(request):
    comment_dict = Comment.objects.order_by('-comment_date')[:2]
       
    error = ''
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'форма не правильная'
            form = CommentForm()
    else:
        form = CommentForm()
    return render(request, 'shop\comments_home.html', {'comment_dict':comment_dict, 'form':form, 'error':error})


# @login_required
# def makePost(request):
#     form = NewsContentForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             new_post = form.save(commit=False)
#             new_post.author = request.user
#             new_post.save()
#             return redirect('/news/')
#     return render(request, 'news/makePost.html', locals())
