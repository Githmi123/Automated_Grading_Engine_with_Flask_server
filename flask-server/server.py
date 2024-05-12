from flask import Flask, jsonify, request
from flask_cors import CORS
from image_downloader import download_images
from markingscheme_downloader import download_markingscheme
import sys
import importlib.util
import sys
import grader
import os
import json
import numpy as np
from delete_directory_contents import delete_directory_contents
import asyncio  


# from .aws.aws_utils import fetch_image_urls_from_s3

app = Flask(__name__)
CORS(app)

@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}


@app.route("/image_urls")  # This must be called inside this.
def get_image_urls():
    bucket_name = ''
    image_urls = fetch_image_urls_from_s3(bucket_name)
    return jsonify({"image_urls": image_urls})


@app.route("/grade", methods = ['POST'])
async def grade_images():
    print("Hi")
    data = request.get_json()
    
    # print(data)
    schemeurl = data.get('answerScript', "")
    student_answers_urls = data.get('studentAnswers', [])
    urls = []
    indexNos = []
    for obj in student_answers_urls:
        studentId = obj.get('studentId')
        url = obj.get('downloadUrl')
        indexNos.append(studentId)
        urls.append(url) # better to use a map here
    save_dir = 'downloaded_images'
    save_dir2 = 'downloaded_marking_scheme'

    await asyncio.gather(
        download_images(urls, indexNos, save_dir),
        download_markingscheme(schemeurl, save_dir2)
    )
    
    print("After downloading")
    directory = 'downloaded_images'
    images = os.listdir(directory)

    results = []
    for image in images:
        
        output = grader.grade(os.path.join(directory, image))
        print("After output")
        score = output.score
        studentAns = output.studentAns
        markingAns = output.markingAns
        print(score)

        results.append({
            'studentId': image.split('_')[1].split('.')[0],
            'score': score,
            'studentAns': studentAns,
            'markingAns': markingAns
        })

    results = json.loads(json.dumps(results, default=lambda x: int(x) if isinstance(x, np.int64) else x))
    delete_directory_contents("downloaded_images")
    delete_directory_contents("downloaded_marking_scheme")


    return jsonify(
        {
            "message": "Grade received successfully", 
            "results": results
        }
    )



if __name__ == "__main__":
    app.run(port = 5000, debug = True)