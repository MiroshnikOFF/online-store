import os
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify
from django.core.mail import send_mail
from dotenv import load_dotenv

from blog.models import Blog

load_dotenv()
EMAIL = os.getenv('EMAIL')
RECIPIENT_LIST = os.getenv('RECIPIENT_LIST').split(',')


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(published=True)
        return queryset


class BlogCreateView(CreateView):
    model = Blog
    fields = (
        'title',
        'body',
        'preview',
        'created_at',
        'published',
        'views',
    )
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
            return super().form_valid(form)


class BlogDitailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        if self.object.views == 100:
            subject = 'Поздравление'
            message = 'С ДОСТИЖЕНИЕМ !!!'
            from_email = EMAIL
            recipient_list = RECIPIENT_LIST
            send_mail(subject, message, from_email, recipient_list)
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = (
        'title',
        'body',
        'preview',
        'created_at',
        'published',
        'views',
    )

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
            return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
