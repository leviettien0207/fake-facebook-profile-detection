# from marshmallow import Schema

# from share.exceptions.exception import ErrorCode1100
# from share.validate import Numeric

# class RequestSchema(Schema):
#     X1 = Numeric(
#         required=True,
#         error_messages={
#         "required": ErrorCode1100.to_json(),
#         "not_allow_string": ErrorCode1300.to_json(),
#         },
#     )