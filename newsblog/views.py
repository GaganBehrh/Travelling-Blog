from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse
from .models import Post, Contact
from .forms import CommentForm, ContactForm
from django.urls import reverse_lazy
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import ModelFormMixin
from django.shortcuts import render
from django.views.generic.edit import FormView


class PostList(LoginRequiredMixin, generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6
    

class PostView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = "post_view.html"
    context_object_name = 'post_list'


class AddView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'add.html'
    fields = ['title', 'author', 'slug', 'featured_image', 'content', 'status','likes']
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('post_view')
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.title = "Gaganpreet"
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)


class TripCalculatorView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'tripcalculator.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('tripcalculator')


class EditView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('post_view')


class Delete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('post_view')


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
               
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )

    

class PostLike(LoginRequiredMixin, View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class contact_views(LoginRequiredMixin, FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/post_view/'

    def form_valid(self, form):
        form = form.save(commit=False)
        form.save()
        return super().form_valid(form)

    def contact_view(request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'add.html')
        form = ContactForm()
        context = {'form': form}
        return render(request, 'contact.html', context)
