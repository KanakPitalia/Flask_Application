from flask import Flask
# import inspect
# import ipdb
# ipdb.set_trace
# import pprint
# pp = pprint.PrettyPrinter(indent=2)
# pp.pprint("i'm in this function: {}".format(inspect.stack()))
app = Flask(__name__)
if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

print(f'ENV is set to: {app.config["ENV"]}')
from flask_application import views
from flask_application import admin_views

