from django.db import models


class Portfolio(models.Model):
    class Meta:
        db_table = 'Portfolio'
        verbose_name = 'portfolioElement'
        verbose_name_plural = 'portfolioElements'
        ordering = ['id']
        
        
    user = models.OneToOneField(
        "user.User",
        verbose_name="유저정보",
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    
    representImage = models.URLField(
        verbose_name="대표이미지",
        max_length=200,
        null=False,
        blank=False
    )
    
    profileImage = models.URLField(
        verbose_name="프로필이미지",
        max_length=200,
        null=False,
        blank=False
    )
    
    saying = models.TextField(
        verbose_name="소개글",
        null=False,
        max_length=1000,
        blank=True
    )
    
    style = models.IntegerField(
        verbose_name="템플릿스타일",
        null=True,
        default=0
    )
    
    ceritificate = models.TextField(
        verbose_name="자격증",
        null=True,
        blank=True
    )
    
    career = models.TextField(
        verbose_name="공모전",
        null=True,
        blank=True
    )
    
    created_at = models.DateTimeField(
        verbose_name="생성일",
        auto_now_add=True,
        null=False
    )
    
    updated_at = models.DateTimeField(
        verbose_name="수정일",
        auto_now=True,
        null=True
    )
    
    
    def __str__(self):
        return self.user
    