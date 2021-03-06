"""
Sending data to Splunk's HTTP Event Collector (HEC)

Read how to setup HEC here: http://blogs.splunk.com/2015/09/22/turbo-charging-modular-inputs-with-the-hec-http-event-collector-input/

"""

import json
import requests


class PyHEC:
    def __init__(self, token, uri, port="8088"):
        if not "http" in uri:
            raise ("no http or https found in hostname")
        self.token = token
        self.uri = uri + ":" + port + "/services/collector/event"
        self.port = port

    """
    event data is the actual event data
    metadata are sourcetype, index, etc
    """

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

        return (
            r.status_code,
            r.text,
        )
