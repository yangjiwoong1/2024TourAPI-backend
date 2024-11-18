from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


def check_required_fields(**fields):
    for field_name, value in fields.items():
        if not value:
            raise ValueError(f"{field_name} must be set")

class UserManager(BaseUserManager):
    def create_user(self, username, nation, nickname, password=None):

        check_required_fields(username=username, nation=nation, nickname=nickname)

        user = self.model(
            username=username,
            nation=nation,
            nickname=nickname,
        )

        # 비밀번호는 해시를 통해 암호화 후 저장
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, nickname, password=None):

        user = self.create_user(username, 'global', nickname, password)
        user.is_staff=True
        user.is_superuser=True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    nation = models.CharField(max_length=30)
    nickname = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["nickname"]

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Admin always
        return self.is_staff

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
