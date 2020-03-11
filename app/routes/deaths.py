from flask import jsonify
from app import app
from app.data import get_data

@app.route('/deaths')
def deaths():
    return jsonify({
        'source': 'https://github.com/ManjurHKhan/coronavirus-tracker-api',
        'comment': 'Forked from https://github.com/ExpDev07/coronavirus-tracker-api',
        'deaths' : get_data('deaths')
    })
