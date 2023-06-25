from django.db import models


class Tag(models.Model):
    class Meta:
        db_table = 'OutsourcingTags'
        verbose_name = 'outsourcingTag'
        verbose_name_plural = 'outsourcingTags'
        ordering = ['id']


    outsourcing = models.ForeignKey(
        'outsourcing.Outsourcing',
        verbose_name='외주',
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    tag = models.CharField(
        verbose_name='외주태그',
        max_length=20,
        null=False,
        blank=False
    )


    def __str__(self):
        return self.portfolio
    