import requests, uuid, json
from ids import ex_01_subscription_key as subscription_key

# Add your subscription key and endpoint
endpoint = "https://api.cognitive.microsofttranslator.com"

# Add your location, also known as region. The default is global.
# This is required if using a Cognitive Services resource.
location = "westeurope"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': ['de', 'it']
}
constructed_url = endpoint + path

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
body = [{
    'text': 'The worldhood of the world (as such)!'
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()
print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))

print("Ergebnis:")
for t in response[0]["translations"]:
    print ("%s : %s" % (t["to"], t["text"]))

