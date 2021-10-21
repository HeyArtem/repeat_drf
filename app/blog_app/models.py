from django.db import models


class BlogPostCategory(models.Model):
    title = models.CharField(max_length=25)
    
    class Meta:
        verbose_name = 'Blog Post Category'
        verbose_name_plural = 'Blog Post Categories'
        
    def __str__(self) -> str:
        return self.title


class BlogPost(models.Model):
    STATUS_CHOISES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=100)
    # category = models.ForeignKey(BlogPostCategory, on_delete=models.SET_NULL, null=True)
    # img = models.ImageField(upload_to='blog_met1_app/', blank=True, null=True)
    description = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOISES, default='draft', max_length=15)
    
    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
        
    def __str__(self) -> str:
        return self.title
