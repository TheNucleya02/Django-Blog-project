from django.db import models

class About(models.Model):
    heading = models.CharField(max_length=50)
    body = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'about'

    def __str__(self):
        return self.heading
    
class Follow(models.Model):
    platform_name = models.CharField(max_length=20)
    platform_link = models.URLField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'follow'

    def __str__(self):
        return self.platform_name
