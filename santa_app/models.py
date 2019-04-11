from django.db import models
from django.contrib.auth.models import User


class Pair(models.Model):
    userOne = models.ForeignKey(User, related_name="pair_user_one")
    userTwo = models.ForeignKey(User, related_name="pair_user_two")
    mailed = models.BooleanField(default=False)