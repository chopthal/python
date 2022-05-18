import os
from flask import Blueprint, url_for, render_template, request
from werkzeug.utils import redirect, secure_filename

import cv2
import numpy as np

bp = Blueprint('main', __name__, url_prefix='/')

image_path = './counter/static/images'

min_radius_percent_default = 5
max_radius_percent_default = 15
min_distance_percent_default = 5
parameter1_default = 30
parameter2_default = 50

@bp.route('/hello')
def hello_counter():
    return 'Hello, Counter!'

@bp.route('/')
def index():
    return redirect(url_for('main.counter'))

@bp.route('/counter', methods=['GET', 'POST'])
def counter():
    if request.method == 'POST':
        file = request.files['file']
        # filename = secure_filename(file.filename)
        filename = file.filename
        if filename:
            os.makedirs(image_path, exist_ok=True)
            pathfile = os.path.join(image_path, filename)
            # print(pathfile)
            file.save(pathfile)
            return render_template('uploaded.html', filename = filename, min_radius_percent=min_radius_percent_default, max_radius_percent=max_radius_percent_default, min_distance_percent=min_distance_percent_default, parameter1=parameter1_default, parameter2=parameter2_default)
    return render_template('counter.html')

@bp.route('/count_circles/<filename>', methods=['GET', 'POST'])
def count_circles(filename):
    min_radius_percent = float(request.form["min_radius_percent"])
    max_radius_percent = float(request.form["max_radius_percent"])
    min_distance_percent = float(request.form["min_distance_percent"])
    parameter1 = float(request.form["parameter1"])
    parameter2 = float(request.form["parameter2"])

    # print(min_radius, max_radius)
    count_result, result_img = count_fcn(filename, min_radius_percent, max_radius_percent, min_distance_percent, parameter1, parameter2)
    return render_template('uploaded.html', count_result=count_result, filename=filename, result_img=result_img, min_radius_percent=min_radius_percent, max_radius_percent=max_radius_percent, min_distance_percent=min_distance_percent, parameter1=parameter1, parameter2=parameter2)

def count_fcn(filename, min_radius_percent=min_radius_percent_default, max_radius_percent=max_radius_percent_default, min_distance_percent=min_distance_percent_default, parameter1=parameter1_default, parameter2=parameter2_default):
    num_circles = 0
    out_file = 'result.png'

    if filename:
        path_file = os.path.join(image_path, filename)
        out_path_file = os.path.join(image_path, out_file)

    img = cv2.imread(path_file)
    output = img.copy()
    img = cv2.medianBlur(img,5)
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    min_radius = int(img.shape[1] * min_radius_percent/100)
    max_radius = int(img.shape[1] * max_radius_percent/100)
    min_distance = int(img.shape[1] * min_distance_percent/100)

    circles = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT,dp=1, minDist=min_distance,
                                param1=parameter1, param2=parameter2, minRadius=min_radius, maxRadius=max_radius)

    try:
        if circles == None:
            num_circles = 0
            out_file = filename
            return num_circles, out_file

    except:
        num_circles = len(circles[0, :])

        if circles is not None:
            circles = np.round(circles[0, :]).astype('int')

            for (x, y, r) in circles:
                cv2.circle(output, (x, y), r, (0, 0, 255), 2)

        cv2.imwrite(out_path_file, output)

        return num_circles, out_file

# No caching at all for API endpoints.
@bp.after_request
def add_header(response):
    response.cache_control.no_store = True
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response
