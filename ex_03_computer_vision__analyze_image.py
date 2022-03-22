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

#url = "https://reisenexclusiv.com/wp-content/uploads/2019/04/Innsbruck-Panorama-Inn-Berge-Mariahilf.jpg"
#url = "https://i0.web.de/image/828/33631828%2cpd=2%2cf=size-l/lemmy-kilmister.webp"
url = "https://www.tagesspiegel.de/images/heprodimagesfotos86120140520brianduffy-jpg/9916500/3-format6001.jpg"
#image_analysis = client.analyze_image(url,visual_features=[VisualFeatureTypes.tags])

image_analysis = client.analyze_image_in_stream((open('./imgs/ibk.jpg', 'rb')),visual_features=[VisualFeatureTypes.tags])

for tag in image_analysis.tags:
    print(tag)

analysis = client.describe_image(url, 3, "en")  #max_descriptions=3, language
analysis = client.describe_image_in_stream(open('./imgs/ibk.jpg', 'rb'), 3, "en")

for caption in analysis.captions:
    print(caption.text)
    print(caption.confidence)