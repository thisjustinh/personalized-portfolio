from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import pandas as pd
import json
from . import cluster

recieved_json_data = []
#landing page - rohit made this
def index(request):
    return render(request, '../templates/index.html')

def results(request):
    return render(request, '../templates/results.html')

def styles(request):
    return render(request, '../templates/styles.css')
#this is called from the front-end app - gives back json file - read it in front end and display it elegantly
# def get_portfolio(request):
#     response = json.dumps(stock_recommender.getStocks())
#     return HttpResponse(response, content_type='text/json')

def readfiles():
    return pd.read_csv('C:/Users/sidiy/workspace/portfolio_api/portfolio/static/cluster.csv'), pd.read_csv('C:/Users/sidiy/workspace/portfolio_api/portfolio/static/historical.csv')

@csrf_exempt
def collect_user_data(request):
    if request.method == 'POST':
        kmeans, hist = readfiles()

        received_json_data=json.loads(request.body.decode("utf-8"))
        print(received_json_data)
        print(type(received_json_data))
        user_input = [received_json_data['risk'], received_json_data['amount'], received_json_data['time']]
        print(user_input)
        response = json.dumps(cluster.recommendations(received_json_data['risk'], received_json_data['amount'], received_json_data['time'], kmeans, hist))
        return HttpResponse(response, content_type='text/json')
# Create your views here.
