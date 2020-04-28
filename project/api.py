import json

from flask import Flask
from flask_restful import Api, Resource, reqparse

from db_exchange import MediaDB

app = Flask(__name__)
api = Api(app)


class APIMediaLib(Resource):
    def __init__(self):
        self.database = MediaDB()

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('video_id', type=str)
        parser.add_argument('category_id', type=str)

        video_id = parser.parse_args()['video_id']
        category_id = parser.parse_args()['category_id']

        if not video_id and not category_id:
            return self.database.get_videos()
        elif video_id:
            return self.database.get_video_info(video_id)
        elif category_id:
            return self.database.get_videos_by_category(category_id)

    def post(self):
        # TODO add categories
        pass

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('video_id', type=str)
        parser.add_argument('changes_str', type=str)

        video_id = parser.parse_args()['video_id']
        changes_str = parser.parse_args()['changes_str']
        changes_dict = json.loads(changes_str)

        return self.database.change_row(video_id, changes_dict)


api.add_resource(APIMediaLib, '/bar')
# api.add_resource(ApiV1, "/")
if __name__ == '__main__':
    app.run(debug=True)
