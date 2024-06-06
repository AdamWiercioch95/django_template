from django.contrib.auth.models import AbstractUser
from django.db import models


# model na potrzeby stworzenia gotowej, poprawnej tabeli. Z czasem będziemy ją rozszerzać ALTER-em
class CustomUser(AbstractUser):
    pass


