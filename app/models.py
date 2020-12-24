from django.db import models
from django.core import validators


class Item(models.Model):
    name = models.CharField(
        verbose_name="名前",
        max_length=200,
    )
    money = models.IntegerField(
        verbose_name="貸したお金",
        validators=[validators.MinValueValidator(0)]
    )
    memo = models.TextField(
        verbose_name="備考",
        max_length=300,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name="登録日",
        auto_now_add=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "アイテム",
        verbose_name_plural = "アイテム"
