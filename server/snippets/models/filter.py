from collections import defaultdict

from django.db import models
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from filelock import FileLock

from snippets.utils import attr
from .base import BaseModel
from .contenttype import ContentType
from .field import Field
from .group import Group
from .user import User

lock = FileLock("filter.lock")
lock.release(force=True)

cache = defaultdict(lambda: defaultdict(list))


@receiver(post_save)
@receiver(post_delete)
def clear_filter(sender, **kwargs):
    if sender in [Group, User] or issubclass(sender, Filter):
        with lock:
            cache.clear()


def get_all_filters():
    if not cache:
        with lock:
            for f in GroupFilter.objects.all():
                for user in User.objects.filter(group=f.group).all():
                    cache[user][f.contenttype.get_model()].append(f)

            for f in UserFilter.objects.all():
                cache[f.user][f.contenttype.get_model()].append(f)

    return cache


class FilterValueType:
    constant = 10
    view_attribute = 5

    choices = [
        (constant, "固定值"),
        (view_attribute, "视图属性"),
    ]


class Filter(BaseModel):
    class Meta:
        abstract = True

    contenttype = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    name = models.CharField("过滤器名称", max_length=100)
    value_type = models.SmallIntegerField("值类型", choices=FilterValueType.choices)
    attribute = models.CharField("属性名", max_length=100)
    value = models.CharField("属性值", max_length=500)
    enabled = models.BooleanField("开通", default=True)

    @classmethod
    def get_filters_dict(cls, view, user, model):
        result = {}
        for f in get_all_filters()[user][model]:
            value = cls.parse_value(view, f)
            if value is not None:
                result[f.attribute] = value
        return result

    @classmethod
    def parse_value(cls, view, f):
        return attr(view, f.value) if f.value_type == FilterValueType.view_attribute else f.value

    @classmethod
    def filter(cls, query, view, model):
        if query:
            user = view.request.user
            filters = cls.get_filters_dict(view, user, model)
            for fields in Field.get_group_fields(user, model, has_contenttype=True, reverse=True):
                for field in fields:
                    for f in get_all_filters()[user][field.model]:
                        value = cls.parse_value(view, f)
                        if value is not None:
                            filters[f"{field.attribute.replace('.','__')}_{f.attribute}"] = value
            if filters:
                query = query.filter(**filters)
        return query


class GroupFilter(Filter):
    class Meta:
        verbose_name_plural = verbose_name = "过滤器(用户组)"

    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class UserFilter(Filter):
    class Meta:
        verbose_name_plural = verbose_name = "过滤器(用户)"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
