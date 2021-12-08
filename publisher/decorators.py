import functools
import json

from publisher.http import BadRequest, MethodNotAllowed


class allow:
    def __init__(self, *methods):
        self.allowed = tuple(m.upper() for m in methods)

    def __call__(self, view):
        @functools.wraps(view)
        def wrapper(request, *args, **kwargs):
            if request.method not in self.allowed:
                return MethodNotAllowed()

            return view(request, *args, **kwargs)

        return wrapper


class datarequired:
    def __init__(self, *params):
        self.params = tuple(params)

    def __call__(self, view):
        @functools.wraps(view)
        def wrapper(request, *args, **kwargs):
            try:
                params = json.loads(request.body)
                assert all(p in params for p in self.params)
            except AssertionError as e:
                return BadRequest('Bad request.')

            kwargs['params'] = params

            return view(request, *args, **kwargs)

        return wrapper
