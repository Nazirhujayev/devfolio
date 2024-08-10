from django.db import models
from django_resized import ResizedImageField
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Intro(models.Model):
    name = models.CharField(max_length=256)
    job = models.CharField(max_length=256)
    
    class Meta:
        db_table = "intro"
        verbose_name = _("intro")
        verbose_name_plural = _("intro")

    def __str__(self) -> str:
        return self.name

class Skills_percent(models.Model):
    number = models.IntegerField()
    

class Skills(models.Model):
    language = models.CharField(max_length=256)
    percentage = models.ManyToManyField(Skills_percent, verbose_name=_("percent"))

    def __str__(self):
        return self.language
    
class About(models.Model):
    name = models.CharField(max_length=256)
    profile = models.CharField(max_length=256)
    email = models.EmailField()
    phone = models.CharField(max_length=256)
    content = RichTextField(_('content'))
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    # skills = models.ManyToManyField(Skills, verbose_name="skills", related_name="about")
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "about"
        verbose_name = _("about")
        verbose_name_plural = _("about")

class Service(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = "service"
        verbose_name = _("service")
        verbose_name_plural = _("services")

class Portfolio(models.Model):
    title = models.CharField(_("title"), max_length=150)
    category = models.CharField(max_length=256)
    image = ResizedImageField(size=[350, 219], upload_to=None)
    date= models.DateField(_("date"), auto_now=True, auto_now_add=False)

class Thoughts(models.Model):
    name = models.CharField(_("name"), max_length=250)
    text = models.TextField(_("text"))
    image = ResizedImageField(size=[150, 150], upload_to=None)

class BlogCategory(models.Model):
    category = models.CharField(_("category"), max_length=250)
    
    def __str__(self) -> str:
        return self.category


class Blog(models.Model):
    title = models.CharField(_("title"), max_length=250)
    text = models.TextField(_("text"))
    name = models.CharField(_("name"), max_length=250)
    category = models.ManyToManyField(BlogCategory, verbose_name=_("category"),related_name="projects")
    slug = models.SlugField(_("slug"))
    duration = models.CharField(_("duration"), max_length=256)
    image = ResizedImageField(size=[348, 232], upload_to=None)
    image_main = models.ImageField(_("image_main"), upload_to=None, height_field=None, width_field=None, max_length=None)
    content = RichTextField()

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ["-id"]

class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments", verbose_name=_("blog"))
    name = models.CharField(_("name"), max_length=250)
    email = models.EmailField(_("email"), max_length=254)
    website = models.CharField(_("website"), max_length=250)
    message = models.TextField(_("message"))
    date = models.DateField(_("date"), auto_now=True)

class Contact(models.Model):
    name = models.CharField(_("name"), max_length=50)
    email = models.EmailField(_("email"), max_length=254)
    subject = models.CharField(_("subject"), max_length=50)
    message = models.TextField(_("message"))

class Contact_us(models.Model):
    text = models.TextField(_("text"))
    location = models.CharField(_("location"), max_length=250)
    number = models.CharField(max_length=256)
    contact_email = models.EmailField(_("email"), max_length=254)