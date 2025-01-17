from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token


class UserService:

    def __init__(self, user_model):
        self.user_model = user_model

    def create_user(self, email: str, password: str):
        return self.user_model.create_user(email, password)

    def get_by_email(self, email: str):
        return self.user_model.get_by_email(email)

    def get_by_id(self, user_id: str):
        return self.user_model.get_by_id(user_id)

    @staticmethod
    def check_password(user, password: str):
        return check_password_hash(user["password"], password)

    def is_user_exist(self, email: str):
        return self.user_model.get_by_email(email) is not None

    def create_jwt(self, user):
        access_token = create_access_token(identity=str(user["_id"]))
        refresh_token = create_access_token(identity=str(user["_id"]))
        return access_token, refresh_token
