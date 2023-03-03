from flask import Flask

app = Flask(__name__)

# Importing resources after initializing Flask
import resources.categories_resource
