# Sending Fake Data Logs to Splunk HTTP Event Collector via Python

For this small project, I used a python Library named Faker to generte fake logs to send to Splunk using the Splunk HTTP Event Collector. Using the Logs from Splunk, I have also created a dashboard with analytics about the data. Keep in mind that the data is not meaningful as it has been generated using a python Library.

### Architecture

### Code Walkthrough 

1. fakedata.py - This class generates fake data with pre defined fields. It is initialized with number of fake records to be created.

2. pyHEC.py - This class is used to establish a connection between Splunk HEC and our main program. It is initialized with our respective Splunk token and has a send() method to establish the connection. 
```
def send(self, event, source, type, metadata=None):
        headers = {"Authorization": "Splunk " + self.token}

        payload = {
            "host": self.uri,
            "sourcetype": type,
            "source": source,
            "event": event,
        }
        if metadata:
            payload.update(metadata)
            
        r = requests.post(
            self.uri,
            data=json.dumps(payload),
            headers=headers,
            verify=False,
        )
```

3. send_hec.py - This is the main class and uses fakedata.py and pyHEC.py to create fake data and send it to our respective Splunk HEC. I've also used a Decimal Encoder since I have generated fake latitude and longitude values. 

```
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
    
```

### Dashboard

Here is an example Dashboard that was created with the fake data. 

![alt text](/Images/splunk-dashboard.JPG)
