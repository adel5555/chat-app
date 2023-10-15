from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField( max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self) :
        return self.name

class Message(models.Model):
    content = models.TextField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) :
        return self.content