import re

from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest


class BaseValidationError(ValidationError):
    code: int
    description: str
    
    def __init__(self, field_name: str):
        self.field_name = field_name
        self.messages = {"error code": self.code, "message": self.description}

    def make_response(self):
        return self.normalized_messages()

    @classmethod
    def to_json(self):
        return {"error code": self.code, "message": self.description}

class BaseSpecialError(Exception):
    code: int
    description: str
    def __init__(self):
        self.messages = {"error code": self.code, "message": self.description}

    def make_response(self):
        return [self.messages]

    @classmethod
    def to_json(self):
        return {"error code": self.code, "message": self.description}
    
    
class ErrorCode1000(BaseSpecialError):
    code = 1000
    description = "A Unicode-related encoding or decoding error occurs."
    

class ErrorCode1001(BaseSpecialError):
    code = 1001
    description = "The url just received does not have the format of facebook account."
    

class ErrorCode1002(BaseSpecialError):
    code = 1002
    description = "The url just received does not have the information of the facebook account."


def handler_exception_error(err: Exception):
    errors = {"other": [{"error code": 9999, "message": "Unexpected error"}]}
    if isinstance(err, BaseSpecialError):
        errors = {"other": err.make_response()}
    elif isinstance(err, BaseValidationError):
        errors = {"validate": err.make_response()}
    elif isinstance(err, ValidationError):
        err_dict = {}
        for key, value in err.messages.items():
            if isinstance(value, list):
                err_dict[key] = value[0]
            else:
                err_dict[key] = value
        errors = {"validate": err_dict}
    elif isinstance(err, BadRequest):
        if re.search("Failed to decode JSON object", str(err)):
            errors = {"other": ErrorCode1000.to_json()}
    return {
        "code": 400,
        "errors": errors
    }