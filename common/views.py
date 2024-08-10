from django.views.generic import DetailView
from django.views.generic.base import View
from django.db.models import Q, Count
from django.http import HttpResponseRedirect

from .forms import BlogCommentForm
from django.urls import reverse

from django.shortcuts import render, get_object_or_404
from common import models
from django.contrib import messages



class Home(View):
  def get(self, request):
    intro = models.Intro.objects.all()
    about = models.About.objects.all()
    skills = models.Skills.objects.all().prefetch_related("percentage")
    service = models.Service.objects.all()[:3]
    portfolio = models.Portfolio.objects.all()
    thoughts= models.Thoughts.objects.all()
    blog = models.Blog.objects.all().prefetch_related("category")
    contact = models.Contact_us.objects.all()

    context = {
      "intro": intro,
      "about": about,
      "skills": skills, 
      "service": service,
      "portfolio": portfolio, 
      "thoughts": thoughts,
      "blog":blog,
      "contact": contact
    }    
    # context["related_projects"] = models.Projects.objects.filter(~Q(slug = self.kwargs["slug"]), categories__in = self.get_object().categories.all())

    return render(request, "index.html", context)
  
  
class BlogDetails(DetailView):
    queryset = models.Blog.objects.all().annotate(count=Count("comments"))
    slug_field = "slug"
    context_object_name = "object"
    template_name = "blog-single.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_posts'] = models.Blog.objects.all()

        context["recent_posts"] = models.Blog.objects.exclude(slug = self.kwargs["slug"])
        # context["recent_posts"] = models.Blog.objects.filter(~Q(slug = self.kwargs["slug"]), category__in = self.get_object().category.all())
        context["category"] = models.BlogCategory.objects.all()
        context["comments"] = models.BlogComment.objects.filter(blog__slug = self.kwargs["slug"])
        return context

class AddComment(View):
    def post(self, request, blog_id):
        if request.method == 'POST':
            form = BlogCommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit = False)
                blog = get_object_or_404(models.Blog, id = blog_id)
                comment.blog = blog
                form.save()
                return HttpResponseRedirect(reverse("common:blog-single", kwargs = {"slug": blog.slug}))

            else:
                form = BlogCommentForm()

            return render(request, 'blog-single.html', {'form': form})  
        
class ContactView(View): 
    def get(self, request):
        return render(request,"index.html")
    
    def post(self, request):   
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        email = request.POST.get("email")
        message = request.POST.get("message")

        try:
            models.Contact.objects.create(name = name, email = email, subject = subject, message = message)
            messages.add_message(request, messages.SUCCESS, "Your Massage has been sent successfully!")
            return HttpResponseRedirect(reverse("common:contact"))
        
        except Exception as e:
            messages.add_message(request, messages.WARNING, 'Error occurred! Please try again! ')
            return HttpResponseRedirect(reverse("common:contact"))

