from Glance_flaskBased.flask.flask_app import *



if __name__ == "__main__":
    app = creat_flask_app()
    # print(app.config)
    app.run(app.config["FLASK_HOST"], app.config["FLASK_PORT"],app.config["FLASK_DEBUG"])