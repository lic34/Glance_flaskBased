class baseConfig:
    FLASK_DEBUG = True
    FLASK_HOST = '127.0.0.1'
    FLASK_PORT = 5000


class prodConfig(baseConfig):
    FLASK_DEBUG = False
    FLASK_PORT = 8080

class devConfig(baseConfig):
    pass