import requests
from pymongo import GEOSPHERE
import statistics
import json
from dotenv import load_dotenv
import os
import pandas as pd
from pymongo import MongoClient
from functools import reduce
import operator

def clean(list_):
    for n,seed in enumerate(list_):
        for i,office in enumerate(seed["offices"]):
            if office["latitude"] == None:
                del seed["offices"][i:]
            if len(seed["offices"])==0:
                del list_[n]
    return list_

def type_point(long,lat):
    return {"type": "Point", 
            "coordinates":[long,lat]}

def getFromDict(dic, map_):
    return reduce(operator.getitem,map_,dic)