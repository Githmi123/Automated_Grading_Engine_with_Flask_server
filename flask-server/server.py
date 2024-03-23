from flask import Flask, jsonify, request
from flask_cors import CORS


from aws_utils import fetch_image_urls_from_s3

app = Flask(__name__)
CORS(app)

@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}


@app.route("/image_urls")
def get_image_urls():
    bucket_name = ''
    image_urls = fetch_image_urls_from_s3(bucket_name)
    return jsonify({"image_urls": image_urls})


@app.route("/grade", methods = ['POST'])
def grade_images():
    data = request.get_json()
    filename = data.get('filename')
    total_score = data.get('total_score')


    return jsonify({"message": "Grade received successfully", "filename": filename, "total_score": total_score})



if __name__ == "__main__":
    app.run(debug = True)