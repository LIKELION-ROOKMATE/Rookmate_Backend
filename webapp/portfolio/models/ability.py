from django.db import models


class Ability(models.Model):
    class Meta:
        db_table = 'Ability'
        verbose_name = 'ability'
        verbose_name_plural = 'abilites'
        ordering = ['id']
        
    portfolio = models.ForeignKey(
        "portfolio.Portfolio",
        verbose_name="활용능력",
        on_delete=models.CASCADE,
        null=True
    )
    
    ability = models.CharField(
        verbose_name="활용능력명",
        max_length=20,
        null=True,
        blank=True
    )
    
    mastery = models.IntegerField(
        verbose_name="활용능력치",
        null=True,
        default=100
    )
    
    def __str__(self):
        return self.portfolio
    