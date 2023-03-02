# Expense Category Populator

This app will populate the expense categories in AWS DynamoDB by exposing API endpoints. These 
expense categories will then be referenced by the Expense Report generator project to calculate 
and diversify the expenses.

## Requirements

For building and running the application you need:

- [Python3](https://www.python.org/downloads/)

```shell
pip3 install -r requirements.txt
```
OR
```shell
pip install -r requirements.txt
```

## Running the application locally

You can run the main.py program to get started. This file has the __main__ method.

```shell
python3 ./src/main.py
```
OR
```shell
python ./src/main.py
```

