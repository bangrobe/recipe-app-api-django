from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """ Create and saves a new user """
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(
            email=self.normalize_email(email), **extra_fields)

        # Tao new user model, **extra_fields la ca field them vao sau, chung ta go extra_fields để tượng trưng cho các field sẽ thêm vào
        # normalize_email là hàm nằm trong BaseUserManager
        user.set_password(password)  # Dùng set_password dể mã hoá password
        # using=self._db là ko cần thiết, nhưng là best practice với nhiều database
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """ Create and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    # Thay thế username field bằng email
    USERNAME_FIELD = 'email'
