from django.db import models


class Member(models.Model):
    class Type:
        enabled = 1
        disabled = 2
        choices = [
            (enabled, "启用"),
            (disabled, "禁用"),
        ]

    class Meta:
        ordering = ('-id',)

    name = models.CharField("名称", max_length=100, )
    email = models.CharField("邮件", max_length=100)
    website = models.CharField("网址", max_length=100)
    address = models.CharField("地址", max_length=500, null=True)
    balance = models.FloatField("余额")
    status = models.SmallIntegerField("状态", choices=Type.choices, default=Type.enabled)
    birthday = models.DateField("生日", null=True)
    create_time = models.DateTimeField("加入时间", null=True)
    signature = models.TextField("个性签名", null=True)
    single = models.BooleanField("单身", default=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
