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
coll.drop()  # remove the collection
docs = [{"name": "Code", "surname": "Institute", "twitter": "@codersinstitute"},
        {"name": "Henry", "surname": "Moore", "twitter": "@henrymoore"},
        {"name": "Stephen", "surname": "Fry", "twitter": "@stephenfry"}]
coll.insert_many(docs)
results = coll.find({"name": "Stephen"})

# Get column and records count
# print results.count()
# print coll.count()

# Iterate through the cursor
for doc in results:
    print doc

