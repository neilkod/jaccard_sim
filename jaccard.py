from __future__ import division
import random

def jaccard(u1, u2):
  num = len(set(u1.ratings.items()) & set(u2.ratings.items()))
  denom = len(u1.ratings.items())
  return num/denom

USERS = 10
ITEMS = 20

items = range(ITEMS)

class user:
  def __init__(self,items=ITEMS):
    self.ratings = dict(enumerate([random.randint(0,1) for x in range(items)]))

users = [user(ITEMS) for x in range(USERS)]
