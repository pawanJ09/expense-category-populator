from boto3 import resource
from botocore.exceptions import ClientError

resource = resource('dynamodb', region_name='us-east-2')
table = resource.Table('expense-categories')


class ExpenseCategoriesModel:

    def __init__(self, category, val):
        self.category = category
        self.val = val
