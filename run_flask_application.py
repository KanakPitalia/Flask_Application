from flask_application import app
# import inspect
# print(inspect.stack()[0][3])
if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])
