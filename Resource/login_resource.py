import datetime

from flask_restful import Resource, request
import json
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt)

# from lib.AppException import AppException
# from . import api
# from models.User import User, UserSchema


# class UserResource(Resource):
#
#     @jwt_required
#     def post(self):
#
#         # TODO: Create consumer account
#         user_data = request.json
#         user_schema = UserSchema()
#         user = user_schema.load(user_data).data
#         identity = get_jwt_identity()
#         user.created_by_id = identity['uid']
#         user.modified_by_id = identity['uid']
#         user.name = user_data['name']
#         user.description = user_data['description']
#         user.is_active = user_data['is_active']
#         user.default_tz = user_data['default_tz']
#         user.created_date = datetime.datetime.utcnow()
#         user.modified_date = datetime.datetime.utcnow()
#         user.uid = user_data['uid']
#         user.pwdhash = user_data['password']
#         res = user.save()
#         if res['success']:
#             return {
#                        "status": 200,
#                        "msg": "Consumer creation successful",
#                        "msg_code": "consumer_creation_success",
#                        "consumer_id": str(user._id)
#                    }, 200
#
#         return {
#                    "status": 400,
#                    "msg": "User creation failed due to error: " + res["msg"],
#                    "msg_code": "user_creation_failed",
#                }, 400
#
#     def delete(self, pk):
#         if request.endpoint == "api.consumer_single":
#             user = User()
#             res = user.delete_user(pk)
#             return {'msg': str(res) + ' records deleted'}
#
#     @jwt_required
#     def put(self, pk):
#         if request.endpoint == "api.consumer_single":
#             user = User()
#             newvalues = {"$set": request.get_json()}
#             res = user.update_user(pk, newvalues)
#             return {'msg': str(res) + ' records updated'}


class UserAuthResource(Resource):
    def post(self):
        # user_data = request.json
        # print("Auth data")
        # print(user_data)
        # print("----------")
        # if 'frontend_userid' not in user_data:
        #     raise AppException("front end user id is missing", 'validation_error', 400)
        # if user_data['frontend_userid'] == '':
        #     raise AppException("front end user id is missing", 'validation_error', 400)
        # user = User(username=user_data['uid'], password=user_data['password'])
        # res = user.login()
        # if res['success'] == True:
        #     loggedin_user = res['user']
        #     response_json = {
        #         "access_token": res['access_token'],
        #         "refresh_token": res['refresh_token'],
        #         "expires": str(2 * 60 * 60 * 1000)
        #     }
        #     if loggedin_user.to_document()['consumer_id'] != "":
        #         response_json['consumer_id'] = loggedin_user.to_document()['consumer_id']
        #     return response_json, 200
        #
        # else:
        #     return {
        #                "status": 401,
        #                "msg": "Authentication failed. Please check your UID and password",
        #                "msg_code": "auth_failed",
        #            }, 401
        pass


# class ConsumerListResource(Resource):
#
#     def get(self):
#         user_model = User()
#         consumers = user_model.get_consumers()
#         users_schema = UserSchema(many=True)
#         consumer_res = users_schema.dump(consumers)
#         return consumer_res


# api.add_resource(UserResource, '/users', endpoint="user")
api.add_resource(UserAuthResource, '/users/auth', endpoint="login")
