import requests
from flask import jsonify, make_response, request
from flask_restx import Namespace, Resource

from app.src.utils.create_presigned_url import create_presigned_url

api = Namespace("pre-sign", description="route that creates a pre-signed url")

@api.route('/presign')
class Presign(Resource):
    def post(self):
        bucket_name = request.form['bucket_name']
        file = request.files['file']
        response = create_presigned_url(bucket_name, file.filename)
        r = requests.post(response['url'], data=response['fields'], files={'file': file.read()})
        
        if r.status_code == 400:
           return make_response("Error!", r.status_code)

        return make_response("Success!", r.status_code)
