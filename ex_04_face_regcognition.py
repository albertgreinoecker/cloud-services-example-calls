import os
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from ids import ex_04_subscription_key as subscription_key, ex_04_endpoint as endpoint

#Bitte durch eigene keys- und eigenen Endpoint ersetzen
face_client = FaceClient(endpoint, CognitiveServicesCredentials(subscription_key))

# Detect a face in an image that contains a single face
# from url
single_face_image_url = 'https://www.biography.com/.image/t_share/MTQ1MzAyNzYzOTgxNTE0NTEz/john-f-kennedy---mini-biography.jpg'
single_image_name = os.path.basename(single_face_image_url)
detected_faces = face_client.face.detect_with_url(url=single_face_image_url, detection_model='detection_03') # We use detection model 3 to get better performance.

# from stream
fname = './imgs/01.png'
single_image_name = os.path.basename(fname)
detected_faces = face_client.face.detect_with_stream(open(fname, 'rb'), detection_model='detection_03') # We use detection model 3 to get better performance.
print(detected_faces)

if not detected_faces:
    raise Exception('No face detected from image {}'.format(single_image_name))

print('Detected face ID from', single_image_name, ':')
for face in detected_faces:
    print (face.face_id)
    print (face.face_rectangle)
    print(face.face_attributes)
    print(face.face_landmarks)
print()

# Save this ID for use in Find Similar
first_image_face_ID = detected_faces[0].face_id