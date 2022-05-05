
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.views.generic.edit import UpdateView
from .models import Comment
from .forms import CommentForm
from .models import Items

# Create your views here.


class New_detail_view(DetailView):
    model = Items
    template_name = 'shop/detail_view.html'
    context_object_name = 'Items'


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
