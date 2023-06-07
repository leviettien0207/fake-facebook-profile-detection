import typing
from functools import wraps
from typing import Callable

from flask import request
from marshmallow import EXCLUDE, utils, validate
from marshmallow.exceptions import ValidationError
from marshmallow.fields import Field, Number

# from share.exceptions.exception import ErrorCode1100, ErrorCode1200, ErrorCode1300, ErrorCode1400


# class Numeric(Number):
#     num_type = float

#     #: Default error messages.
#     default_error_messages = {
#         "special": ErrorCode1300.to_json(),
#         "not_allow_string": ErrorCode1300.to_json(),
#         "length_value_large": ErrorCode1200.to_json(),
#         "invalid": ErrorCode1300.to_json(),
#         "too_large": ErrorCode1200.to_json(),
#         "required": ErrorCode1100.to_json(),
#         "null": ErrorCode1300.to_json(),
#         "validator_failed": ErrorCode1300.to_json(),
#     }

#     def __init__(self, *, allow_nan: bool = False, as_string: bool = False, **kwargs):
#         self.allow_nan = allow_nan
#         super().__init__(as_string=as_string, **kwargs)

#     def _validated(self, value):
#         num = super()._validated(value)
#         if self.allow_nan is False:
#             if math.isnan(num) or num == float("inf") or num == float("-inf"):
#                 raise self.make_error("special")
#         if isinstance(value, str):
#             raise self.make_error("not_allow_string")
#         if len(str(value)) > 15:
#             raise self.make_error("length_value_large")
#         return num


# class Unit(Field):
#     #: Default error messages.
#     default_error_messages = {
#         "invalid": ErrorCode1400.to_json(),
#         "invalid_utf8": ErrorCode1400.to_json(),
#         "required": ErrorCode1100.to_json(),
#         "null": ErrorCode1400.to_json(),
#         "validator_failed": ErrorCode1400.to_json(),
#     }

#     def _serialize(self, value, attr, obj, **kwargs):
#         if value is None:
#             return None
#         return utils.ensure_text_type(value)

#     def _deserialize(self, value, attr, data, **kwargs) -> typing.Any:
#         if not isinstance(value, (str, bytes)):
#             raise self.make_error("invalid")
#         try:
#             return utils.ensure_text_type(value)
#         except UnicodeDecodeError as error:
#             raise self.make_error("invalid_utf8") from error


class ValidateOneOf(validate.Validator):
    def __init__(self, choices: typing.Iterable, error: dict):
        self.choices = choices
        self.error = error

    def __call__(self, value: typing.Any) -> typing.Any:
        try:
            if value not in self.choices:
                raise ValidationError(self.error)
        except TypeError as error:
            raise ValidationError(self.error) from error

        return value


class ValidateRange(validate.Validator):
    def __init__(self, min=None, min_inclusive=False, max=None, max_inclusive=False, error=None):
        self.min = min
        self.min_inclusive = min_inclusive
        self.max = max
        self.max_inclusive = max_inclusive
        self.error = error or {}

    def __call__(self, value: typing.Any) -> typing.Any:
        if self.min is not None and (value < self.min if self.min_inclusive else value <= self.min):
            raise ValidationError(self.error)

        if self.max is not None and (value > self.max if self.max_inclusive else value >= self.max):
            raise ValidationError(self.error)

        return value


def validator(schema):
    def decorator(func: Callable):
        @wraps(func)
        def wrap_func(*args, **kwargs):
            data = request.get_json()
            schema(unknown=EXCLUDE).load(data)
            return func(*args, **kwargs)

        return wrap_func

    return decorator
