from flask_sqlalchemy import SQLAlchemy


class DB:
    def __init__(self, app) -> None:
        connection_string = "mysql+pymysql://developer:rootcodigo@db:3306/alerts"
        app.config["SQLALCHEMY_DATABASE_URI"] = connection_string
        self.db = SQLAlchemy(app)


