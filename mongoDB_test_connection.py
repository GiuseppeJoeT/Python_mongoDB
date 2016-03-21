import pymongo


def mongo_connect():
    try:
        conn = pymongo.MongoClient()
        print "Mongo is connected!"
        return conn
    except pymongo.errors.ConnectionFailure, e:
        print "Could not connect to MongoDb: %s" % e

# Add a document to the database
conn = mongo_connect()
db = conn['twitter_stream']
coll = db.my_collection
docs = [{"name": "Code", "surname": "Institute", "twitter": "@codersinstitute"},
       {"name": "Henry", "surname": "Moore", "twitter": "@henrymoore"},
       {"name": "Stephen", "surname": "Fry", "twitter": "@stephenfry"}]
coll.insert_many(docs)
results = coll.find()

for doc in results:
    print doc

'''
{ u'twitter': u'@codersinstitute',
 u'_id': ObjectId('5629264db1bae125ac446ba5'),
  u'surname': u'Institute',
  u'name': u'Code'}
'''


