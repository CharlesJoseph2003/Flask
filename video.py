from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

# Request parser allows you to parse and validate incoming request data and is good for handling data that
# have been sent as JSONs
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True) #sends us a message saying that the name is required, new video will
#not be created without the name string
video_put_args.add_argument("views", type=int, help="Views on the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video", required=True)

# dict of videos
videos = {}
def abort_if_video_id_doesnt_exist(video_id): #helper function
    if video_id not in videos:
        abort(404, message="Video ID is not valid") #will abort the operation and return a response back 

def abort_if_video_exists(video_id):
    if video_id in videos:
        abort(409, message="Video already exists with that ID")
#hello
class Video(Resource):
    def get(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]
    
    def put(self, video_id):
        abort_if_video_exists(video_id)
        args = video_put_args.parse_args()  # will automatically get all the arguments and if they are not sent, then it will send back an error message
        videos[video_id] = args #adds the video id as the key to the dict and the args as the value
        # return {video_id: args}
        return videos[video_id], 201 #sends status code of 201 to show that video was created, and returns the dict 
    
    def delete(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return '', 204 

    
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)