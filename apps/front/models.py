from django.db import models


class Entrepreneur(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='entrepreneur/')
    slogan = models.TextField()
    mission = models.TextField()
    vision = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name


class Business(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Icon name (e.g., 'truck', 'package')")
    color = models.CharField(max_length=50, default="bg-sky-50 text-sky-700")

    def __str__(self):
        return self.name


class CoreValue(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class PortfolioItem(models.Model):
    CATEGORY_CHOICES = [
        ('Logistics', 'Logistics'),
        ('Manufacturing', 'Manufacturing'),
        ('Agriculture', 'Agriculture'),
        ('Storage', 'Storage'),
    ]

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='portfolio/')

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.created_at.strftime('%Y-%m-%d')})"
