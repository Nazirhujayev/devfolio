from django.forms import ModelForm, Textarea
from common.models import BlogComment


class BlogCommentForm(ModelForm):
    class Meta:
        model = BlogComment
        fields = ('name', 'email','website', 'message')
        widgets = {
            'comment': Textarea(attrs={'cols': 35, 'rows':8})
        }
