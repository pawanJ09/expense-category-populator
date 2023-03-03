from boto3 import resource
from botocore.exceptions import ClientError

resource = resource('dynamodb', region_name='us-east-2')
table = resource.Table('expense-categories')


class ExpenseCategoriesModel:

    def __init__(self, category, val):
        self.category = category
        self.val = val

    def __repr__(self):
        return f"Category: {self.category}"

    @classmethod
    def fetch_all(cls):
        # This can be expensive if huge dynamo db table data exists
        try:
            response = table.scan()
            return response
        except ClientError as e:
            print(e.response['Error']['Message'])
