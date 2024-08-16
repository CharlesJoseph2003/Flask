from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

# Request parser allows you to parse and validate incoming request data and is good for handling data that
# have been sent as JSONs
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video")
video_put_args.add_argument("views", type=int, help="Views on the video")
video_put_args.add_argument("likes", type=int, help="Likes on the video")

# dict of videos
videos = {}

class Video(Resource):
    def get(self, video_id):
        return videos[video_id]
    
    def put(self, video_id):
        args = video_put_args.parse_args()  # will automatically get all the arguments and if they are not sent, then it will send back an error message
        videos[video_id] = args
        return {video_id: args}
    
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)