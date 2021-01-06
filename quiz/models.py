from django.db import models
from django.utils.text import slugify

# Create your models here.

class QuizTitle(models.Model):
    title = models.CharField(max_length=108)
    slug = models.SlugField(null=True)
    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)


class Question(models.Model):

    title = models.ForeignKey(QuizTitle,related_name="questions",on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    option1 = models.CharField(max_length=108)
    option2 = models.CharField(max_length=108)
    option3 = models.CharField(max_length=108)
    option4 = models.CharField(max_length=108)
    answer = models.CharField(max_length=108)
    explanation = models.TextField(null=True,blank=True)
    def __str__(self):
        return f"{self.title} - {self.question}"