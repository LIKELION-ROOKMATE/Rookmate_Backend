from django.db import models


class Outsourcing(models.Model):
    class Meta:
        db_table = 'Outsourcing'
        verbose_name = 'outsourcingElement'
        verbose_name_plural = 'outsourcingElements'
        ordering = ['id']


    portfolio = models.OneToOneField(
        'portfolio.Portfolio',
        verbose_name="포트폴리오",
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    field = models.ForeignKey(
        'outsourcing.Field',
        verbose_name="작업분야",
        on_delete=models.CASCADE,
        null=True
    )

    originalFile = models.BooleanField(
        verbose_name='원본파일제공여부',
        null=False,
        default=False,
        blank=False
    )

    commercialUse = models.BooleanField(
        verbose_name='상업적이용가능여부',
        null=False,
        default=False,
        blank=False
    )

    modeifiable = models.BooleanField(
        verbose_name='수정가능여부',
        null=False,
        default=False,
        blank=False
    )

    modeifiableTime = models.SmallIntegerField(
        verbose_name='수정가능횟수',
        null=True,
        default=0,
        blank=True
    )

    reprocessing = models.BooleanField(
        verbose_name='재가공여부',
        null=False,
        default=False,
        blank=False
    )

    workDays = models.SmallIntegerField(
        verbose_name='작업일',
        null=True,
        default=2,
        blank=True
    )

    workableThing = models.TextField(
        verbose_name='가능한작업',
        null=True,
        blank=True
    )

    price = models.IntegerField(
        verbose_name='작업금액',
        null=True,
        default=10000,
        blank=True
    )

    priceFluctuation = models.BooleanField(
        verbose_name='가격변동여부',
        null=False,
        default=False,
        blank=False
    )

    workMethod = models.TextField(
        verbose_name='작업방식',
        null=True,
        blank=True
    )
    
    promotionText = models.TextField(
        verbose_name='홍보글',
        null=False,
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
        return self.portfolio
    