import abc
import json
from datetime import datetime
from http import HTTPStatus
from json import JSONDecoder

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse

DEFAULT_CT = 'application/json'


class MyResponse(HttpResponse):
    def __init__(self, *args, **kwargs):
        headers = kwargs.setdefault('headers', {})
        if 'Content-Type' not in headers:
            headers['Content-Type'] = DEFAULT_CT

        super(MyResponse, self).__init__(*args, **kwargs)


class MethodNotAllowed(MyResponse):
    status_code = HTTPStatus.METHOD_NOT_ALLOWED

    def __init__(self, *args, **kwargs):
        super(MethodNotAllowed, self).__init__(
            HTTPStatus.METHOD_NOT_ALLOWED.description,
            *args, **kwargs
        )


class BadRequest(MyResponse):
    status_code = HTTPStatus.BAD_REQUEST


class Created(MyResponse):
    status_code = HTTPStatus.CREATED


class NotFound(MyResponse):
    status_code = HTTPStatus.NOT_FOUND


class NoContent(MyResponse):
    status_code = HTTPStatus.NO_CONTENT


class Ok(MyResponse):
    pass


def serialize(obj):
    return json.dumps(obj, cls=MyJSONEncoder)


class MyJSONEncoder(DjangoJSONEncoder):
    def encode(self, obj):
        if isinstance(obj, IMySerializable):
            obj = obj.vars()
        return super().encode(obj)


class IMySerializable(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasscheck__(cls, subclass):
        return hasattr(subclass, 'vars') and callable(subclass.vars)

    @abc.abstractmethod
    def vars(self):
        pass


class MyJSONDecoder(JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.hook, *args, **kwargs)

    @staticmethod
    def hook(source):
        d = {}
        for k, v in source.items():
            if isinstance(v, str) and not v.isdigit():
                try:
                    d[k] = datetime.fromisoformat(v)
                except (ValueError, TypeError):
                    d[k] = v
            else:
                d[k] = v

        return d
