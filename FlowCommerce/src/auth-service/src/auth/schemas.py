from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    username = fields.Str(required=True, validate=validate.Length(min=4, max=80))
    password = fields.Str(required=True, validate=validate.Length(min=6))
