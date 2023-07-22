from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


GENDER_CHOICES  = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))

contact_validator = [
    RegexValidator(regex=r'^[6-9]{1}[0-9]{9}$', message="Please enter a valid 10-digit mobile number.")
]

def regex_validators(value):
    err = None
    for validator in contact_validator:
        try:
            validator(value)
            return value
        except ValidationError as exc:
            err = exc
    raise err

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    name    = models.CharField(('Full Name'),max_length=100, blank=True)
    email   = models.EmailField('Email Address', unique=True)
    mobile  = models.CharField(('Mobile'), max_length=10, validators=[regex_validators,])
    is_admin    = models.BooleanField("Is Admin", blank=True, null=True, default=False)
    is_verified = models.BooleanField("Is Verified",blank=True, null=True, default=False)
    dob = models.DateField(('Date of birth'), blank=True, null=True)
    avatar  = models.FileField(('Profile Picture'), blank=True, null=True)
    gender  = models.CharField(('Gender'), blank=True, max_length=1, choices=GENDER_CHOICES)
    state   = models.CharField(('State'),  blank=True, max_length=30)
    country = models.CharField(('Country'), max_length=200, blank=True, default="India")
    created_at = models.DateTimeField(auto_now=True, editable=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

