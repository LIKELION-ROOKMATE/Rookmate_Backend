from django.db import models


class Comment(models.Model):
    class Meta:
        db_table = 'OutsourcingComment'
        verbose_name = 'outsourcingComment'
        verbose_name_plural = 'outsourcingComments'
        ordering = ['id']


    user = models.ForeignKey(
        'user.User',
        verbose_name='유저정보',
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    outsourcing = models.ForeignKey(
        'outsourcing.Outsourcing',
        verbose_name='외주정보',
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    comment = models.TextField(
        verbose_name='외주후기',
        null=True,
        blank=True
    )

    score = models.SmallIntegerField(
        verbose_name='외주평점',
        null=True,
        blank=True,
        default=5
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
    