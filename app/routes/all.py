from flask import jsonify
from app import app
from app.data import get_data

@app.route('/all')
def all():
    # Get all the categories.
    confirmed = get_data('confirmed')
    deaths    = get_data('deaths')
    recovered = get_data('recovered')

    return jsonify({
        # Data.
        'confirmed': confirmed,
        'deaths':    deaths,
        'recovered': recovered,
        'source': 'https://github.com/ManjurHKhan/coronavirus-tracker-api',
        'comment': 'Forked from https://github.com/ExpDev07/coronavirus-tracker-api',
        # Latest.
        'latest': {
            'confirmed': confirmed['latest'],
            'deaths':    deaths['latest'],
            'recovered': recovered['latest'],
        }
    })
