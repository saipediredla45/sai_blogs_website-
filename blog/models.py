from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Post(models.Model):
    """Single blog post"""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)        # used in URL
    excerpt = models.CharField(max_length=255, blank=True)  # short summary
    content = models.TextField()
    image = models.ImageField(
        upload_to="post_images/",
        blank=True,
        null=True,
    )  # thumbnail / icon image
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)    # set on create
    updated_at = models.DateTimeField(auto_now=True)        # set on update

    class Meta:
        ordering = ["-created_at"]  # newest first

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Auto-generate slug and excerpt if not provided"""
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            count = 1

            # make sure slug is unique
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"
                count += 1

            self.slug = slug

        # auto-generate excerpt from content if empty
        if not self.excerpt and self.content:
            text = self.content.strip()
            self.excerpt = (text[:150] + "...") if len(text) > 150 else text

        super().save(*args, **kwargs)

