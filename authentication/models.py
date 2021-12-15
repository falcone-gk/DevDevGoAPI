from django.db import models

# Create your models here.

class PreRegister(models.Model):

    email = models.EmailField(unique=True ,max_length = 254)
    activated = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.email

    def is_activated(self):

        return self.activated
