from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class account_manager(BaseUserManager):
    def create_user(self, email, username, phone_no, name, password):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        if not phone_no:
            raise ValueError('Users must have a phone no')
        if not name:
            raise ValueError('Users must have a name')
        if not password:
            raise ValueError('pls enter a password')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone_no=phone_no,
            name=name,
            password=password,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, phone_no, name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            phone_no=phone_no,
            name=name,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class create_account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)

    username = models.CharField(max_length=30, unique=True)

    name = models.CharField(max_length=30, unique=False)

    phone_no = models.CharField(max_length=10, unique=True)

    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)

    last_login = models.DateTimeField(
        verbose_name='last login', auto_now=True)

    is_admin = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)

    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username', 'email', 'phone_no', 'name']

    objects = account_manager()

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
