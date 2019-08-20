from flask import Flask, jsonify, request, render_template
from db import sqliteDb
from flask_cors import CORS

from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/output/predictions')
def predictions():
    accept_header = request.headers.get('Accept')

    predictions = sqliteDb().get_predictions()

    if 'application/json' in accept_header:
        return jsonify(predictions)
    elif 'text/html' in accept_header:
        columns = list(predictions[0].keys())

        rows = []
        for prediction in predictions:
            rows.append([*prediction.values()])

        return render_template('predictions.html', predictions=predictions, columns=columns, rows=rows)
    else:
        return("I'm sorry but support for that content type has not been implemented yet.")


def get_now():
    return datetime.now()


def get_moment_last_spray():
    spray_moments = list(sqliteDb().get_spray_moments())

    # we assume the last record in the database is the latest
    moment_last_spray = spray_moments[len(spray_moments) - 1]

    format = '%Y-%m-%d %H:%M:%S'
    return(datetime.strptime(moment_last_spray, format))


def get_days_since_last_spray():
    time_since_last_spray = get_now() - get_moment_last_spray()

    days_since_last_spray = time_since_last_spray.days
    return days_since_last_spray


def get_last_prediction():
    predictions = sqliteDb().get_predictions()

    last_prediction = predictions[len(predictions) - 1]

    return last_prediction


@app.route('/spray')
def spray():
    # get query parameters
    prediction_percentage_threshold = int(
        request.args.get('predictionPercentageThreshold'))
    days_not_sprayed_threshold = int(
        request.args.get('daysNotSprayedThreshold'))

    # check if last prediction exceeds the prediction percentage
    last_prediction = get_last_prediction()

    prediction_over_threshold = True if last_prediction[
        'prediction_percentage'] > prediction_percentage_threshold else False

    # check if the vineyard was sprayed recently
    days_since_last_spray = get_days_since_last_spray()

    recently_sprayed = days_since_last_spray < days_not_sprayed_threshold

    # both requirements are checked
    return jsonify({'spray': prediction_over_threshold and not recently_sprayed,
                    'daysSinceLastSpray': days_since_last_spray,
                    'lastPredictionPercentage': last_prediction['prediction_percentage']})
