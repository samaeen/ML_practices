import json
import math
from collections import OrderedDict

def similarityIndex(movie1,movie2):
	sqrtDiff=sqrt(1)

with open('movies.json', 'r') as f:
    ratings = json.load(f)

name=[name['name'] for name in ratings['users']]
timeStamp=[timestamp['timestamp'] for timestamp in ratings['users']]
ratings=[list(name.values()) for name in ratings['users']]

print(timeStamp)