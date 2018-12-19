from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

class Member(models.Model):
    class Meta:
        ordering = ('-id',)

    name = models.CharField(max_length=100, )
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

 