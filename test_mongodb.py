
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://weuzinho96:admin1234@cluster1-test.b2dnl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1-test"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)