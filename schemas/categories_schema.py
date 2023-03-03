from marshmallow import Schema, fields, INCLUDE, post_load
from model.categories_model import ExpenseCategoriesModel


class ExpenseCategoriesSchema(Schema):
    class Meta:
        unknown = INCLUDE
    category = fields.Str()
    val = fields.List(fields.Str())

    @post_load
    def return_obj(self, data, **kwargs):
        return ExpenseCategoriesModel(**data)

