from flask import jsonify
from app import app
from app.data import get_data


@app.route('/recovered')
def recovered():
    return jsonify({
        'source': 'https://github.com/ManjurHKhan/coronavirus-tracker-api',
        'comment': 'Forked from https://github.com/ExpDev07/coronavirus-tracker-api',
        'recovered' : get_data('recovered')
    })
