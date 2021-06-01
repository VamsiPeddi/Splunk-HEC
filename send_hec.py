# import pyHEC
from pyHEC import PyHEC
from faker import Faker
from fakedata import FakeData

# from fakedatadict import gen_data, gen_data_slow
from datetime import datetime
import json
import decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)


faker = Faker()
my_data = []
num_records = 1000
fakedata = FakeData(num_records) 

# use your token (read how to get it here: http://blogs.splunk.com/2015/09/22/turbo-charging-modular-inputs-with-the-hec-http-event-collector-input/)
hec = PyHEC("<Your-HEC-Token_value>", "URI-Value")

# this is the event you want to send
print(datetime.now())
for data in fakedata.gen_data():
    response = hec.send(
        json.dumps(data, cls=DecimalEncoder), type="_json", source="<Any Source Name>"
    )
    print(response)
    
print("Data Geeration complete")

