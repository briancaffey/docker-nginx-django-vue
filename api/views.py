import os

import datetime

import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from saturday.celery import debug_task


# Mongo

from pymongo import MongoClient

client = MongoClient('mongo', 27017)
db = client.data

# Create your views here.

def debug_view(request):
    debug_task.delay()
    print(db)
    visit = {
        'time': str(datetime.datetime.now()),
    }

    # add a visit record
    db.visits.insert_one(visit)

    # retrieve all visits
    all_visits = list(db.visits.find({}))

    return HttpResponse(all_visits)

def visits_view(request):
    return JsonResponse({"all": [1,2,3]})