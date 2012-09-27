from __future__ import division
import random

USERS = 1000
ITEMS = 200
RATE_PCT = .45

def jaccard(u1, u2):
  num = len(set(u1.ratings.items()) & set(u2.ratings.items()))
  denom = len(u1.ratings.items())
  return num/denom

# each user will have a dict of ratings (0,1)
class user:
  def __init__(self,items=ITEMS):
    self.ratings = dict(enumerate([random.randint(0,1) for x in xrange(items)]))

# have each user rate a certain percentage of items
users = [user(random.randint(ITEMS * RATE_PCT, ITEMS+1)) for x in xrange(USERS)]
