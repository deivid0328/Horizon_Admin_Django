from django.db import models

# Create your models here.
from django.db import models

class PQR(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(
    max_length=20,
    choices=[
    ('open','Abierto'),
    ('process','En proceso'),
    ('closed','Cerrado')
    ],
    default='open'
    )

    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.title