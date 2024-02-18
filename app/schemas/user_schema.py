from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    email = fields.Str()
    password = fields.Str()
    confirm = fields.Str()