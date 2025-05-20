from django.db import models

# Create your models here.

CLASSES = (
    ("Y9", "Y9"),
    ("Y8", "Y8"),
    ("Y7", "Y7"),
)

class Subject(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default="Maths 2025")
    image = models.ImageField(default='default.png')

    def __str__(self):
        return self.description
    
class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default="Atoms, Y9, 2025")
    date_field = models.DateTimeField(auto_now_add=True)
    classroom = models.CharField(max_length=255, choices=CLASSES, default="Y7")

    def __str__(self):
        return self.description
    
class Note(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    date_field = models.DateTimeField(auto_now_add=True)
    classroom = models.CharField(max_length=255, choices=CLASSES, default="Y7")

    def __str__(self):
        return self.name