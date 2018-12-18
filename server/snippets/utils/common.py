import json
import os
import platform

from django.core.serializers.json import DjangoJSONEncoder

from .decorators import memorize


def to_json(data):
    return json.dumps(data, cls=DjangoJSONEncoder)


def first(l, default=None):
    return l[0] if l else default


def last(l, default=None):
    return l[len(l) - 1] if l else default


def is_windows() -> bool:
    return platform.system() == "Windows"

 