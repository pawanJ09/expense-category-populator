from marshmallow import Schema, fields, INCLUDE


class ExpenseCategoriesSchema(Schema):
    class Meta:
        unknown = INCLUDE
    category = fields.Str()
    val = fields.List(fields.Str())

