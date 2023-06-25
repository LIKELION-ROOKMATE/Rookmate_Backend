from django.db import models


class Field(models.Model):
    class Meta:
        db_table = 'Field'
        verbose_name = 'fieldElement'
        verbose_name_plural = 'fieldElements'
        ordering = ['id']


    field = models.CharField(
        verbose_name='작업분야',
        max_length=20,
        null=False,
        blank=False
    )


    def __str__(self):
        return self.field
    