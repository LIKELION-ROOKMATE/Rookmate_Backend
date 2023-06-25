from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

class Usermanager(BaseUserManager):
    def create_user(self, name, age, phone, university, major, password, interest, job, **kwargs):
        if not name:
            raise ValueError('이름을 입력해주세요')
        
        if not age:
            raise ValueError('나이를 입력해주세요')
        
        if not phone:
            raise ValueError('휴대폰 번호를 입력해주세요')
        
        if not university:
            raise ValueError('대학을 입력해주세요')
        
        if not major:
            raise ValueError('학과를 입력해주세요')
        
        if not interest:
            raise ValueError('관심분야를 입력해주세요')
        
        if not job:
            raise ValueError('직업을 입력해주세요')
        
        user = self.model(
            name = name,
            age = age,
            phone = phone,
            university = university,
            major = major,
            interest = interest,
            job = job,
            **kwargs
            )
        user.set_password(password)
        user.save()
    
    def create_superuser(self, name, age, phone, university, major, password, **kwargs):
        user.is_admin = True
        user = self.create_user(name, age, phone, university, major, password, **kwargs)
        user.save()



class User(AbstractBaseUser):
    name = models.CharField(max_length=10)
    age = models.IntegerField(default=0, blank=False, null=False)
    phone = models.IntegerField(default=0, blank=True, null=False, unique=True)
    university = models.CharField(default='')
    major = models.CharField(default='')
    interest = models.CharField(null=False, blank=True, default='')
    job = models.CharField(null=False, blank=True, default='')
    

    @property
    def is_staff(self):
        return self.is_admin