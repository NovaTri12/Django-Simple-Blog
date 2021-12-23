from django.db import models

# Create your models here.

class Post(models.Model):
    title           = models.CharField(max_length=225)
    content         = models.TextField()
    short_content   = models.TextField()
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'src_post'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content         = models.TextField()
    post            = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
