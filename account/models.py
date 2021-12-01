from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Profile(models.Model):

    # As mentioned, there is an inherent relationship between the Profile and
    # User models. By creating a one-to-one relationship between the two, we
    # are formalizing this relationship. Every user will have one -- and only
    # one -- related Profile model.
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )

    # Each user profile will have a field where they can tell other users
    # something about themselves. This field will be empty when the user
    # creates their account, so we specify `blank=True`.
    bio = models.TextField(blank=True)

    # In addition to the `bio` field, each user may have a profile image or
    # avatar. Similar to `bio`, this field is not required. It may be blank.
    image = models.URLField(blank=True)

    # This is an example of a Many-To-Many relationship where both sides of the
    # relationship are of the same model. In this case, the model is `Profile`.
    # As mentioned in the text, this relationship will be one-way. Just because
    # you are following mean does not mean that I am following you. This is
    # what `symmetrical=False` does for us.
    follows = models.ManyToManyField(
        'self',
        related_name='followed_by',
        symmetrical=False,
        default=None,
        blank=True,
    )

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.image = 'https://static.productionready.io/images/smiley-cyrus.jpg'
        return super().save(*args, **kwargs)

    def get_data(self):
        data = {
                'username': self.user.username,
                'bio': self.bio,
                'image': self.image
                }

        return data

