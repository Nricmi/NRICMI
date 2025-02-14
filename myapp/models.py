from django.db import models

class PageContent(models.Model):
    title = models.CharField(max_length=255)  # Title of the content
    body = models.TextField()  # Content description or body
    url = models.CharField(max_length=255, blank=True)  # Link to the corresponding page

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.url  # Return the link to the page
    

class Notification(models.Model):
    message = models.TextField()
    image = models.ImageField(upload_to='notifications/', blank=True, null=True)  # Optional image
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message[:50]  # Display first 50 characters in admin panel

