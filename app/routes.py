from app.control import queryOrdersByDate
from flask import Blueprint, request, render_template
import json

routes = Blueprint('routes', __name__)

@routes.route('/data')
def data():
    date = request.args.get('date')
    result = queryOrdersByDate(date)    
    response =  json.dumps(result,indent = 2)
    return render_template('response.html', response=response)