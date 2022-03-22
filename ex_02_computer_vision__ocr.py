# pip install --upgrade azure-cognitiveservices-vision-computervision
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import time
from ids import ex_02_subscription_key as subscription_key

endpoint = "germanywestcentral"
credentials = CognitiveServicesCredentials(subscription_key)
client = ComputerVisionClient(endpoint="https://" + endpoint + ".api.cognitive.microsoft.com/", credentials=credentials)

numberOfCharsInOperationId = 36

# url = "https://github.com/Azure-Samples/cognitive-services-python-sdk-samples/raw/master/samples/vision/images/make_things_happen.jpg"
# raw = True
# rawHttpResponse = client.read(url, language="en", raw=True)


rawHttpResponse = client.read_in_stream(open('./imgs/page.jpeg', 'rb'), language="en", raw=True)

# Get ID from returned headers
operationLocation = rawHttpResponse.headers["Operation-Location"]
idLocation = len(operationLocation) - numberOfCharsInOperationId
operationId = operationLocation[idLocation:]
time.sleep(10) #in SECONDS
# SDK call
result = client.get_read_result(operationId)
print (result)
# Get data
if result.status == OperationStatusCodes.succeeded:
    for line in result.analyze_result.read_results[0].lines:
        print(line.text)
        print(line.bounding_box)
