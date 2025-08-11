from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 10,unique = True)

    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null = True,
        blank = True,
        related_name='children',
        verbose_name="父分类"
    )
    
    class Meta:
        verbose_name= "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length = 10,unique = True)

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    last_change_time = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="分类")
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        verbose_name="标签"
        )

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return self.title

