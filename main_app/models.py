from tkinter import CASCADE
from django.db import models
from django.urls import reverse

# Create your models here.

REVIEWS = (
    ('E','Excellent'),
    ('G', 'Good'),
    ('A', 'Average'),
    ('S', 'Subpar'),
    ('B', 'Bad')
)

class Tech(models.Model):
    name = models.CharField(max_length=500)
    processor = models.CharField(max_length=250)
    display = models.CharField(max_length=500)
    ram = models.CharField(max_length=100)
    storage = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.CharField(default=None, blank=True, null=True, max_length=2000)
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"tech_id": self.id})
    
    def __str__(self):
        return f"{self.name}"

class Review(models.Model):
    date = models.DateField()
    review = models.CharField(max_length=1, choices=REVIEWS, default=REVIEWS[1][0])
    tech = models.ForeignKey(Tech, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_review_display()} on {self.date}"
    
    class Meta:
        ordering = ['date', 'review']