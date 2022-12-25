
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class AccountManager(BaseUserManager):
    """
    """
    def create_superuser(self, email, name, password, **extra_fields):
        """
            Create a superuser an defaulf it attributes
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff set to True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser set to True")

        return self.create_user(email, name, password, **extra_fields)


    def create_user(self, email, name, password, **extra_fields):
        
        if not email:
            raise ValueError(_("User must provide an email address"))

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    """
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    phone = models.CharField(max_length=32)
    image = models.ImageField(upload_to='user/profie/images/', default='user/profie/images/default.png')
    birthdate = models.DateField(blank=True, null=True)
    biography = models.TextField(_("Biography"), max_length=512, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone', 'address']


    def __str__(self):
        username = f"@{self.email.split('@')[-2]}"
        return username
