import io
import os

from google.cloud import vision
from google.cloud.vision import types

def test_labels():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'google_vision/aqueous-camera-100822-fd232399e118.json'
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = os.path.join(
        os.path.dirname(__file__),
        'vods/facial_recognition/sypher1.png')

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    print('Labels:')
    for label in labels:
        print(label.description)


def test_facial():
    client = vision.ImageAnnotatorClient()

    image = get_image('sypher1.png')
    image = get_image('nickmercs1.png')

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    print('Faces:')

    for face in faces:
        print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                     for vertex in face.bounding_poly.vertices])

        print('face bounds: {}'.format(','.join(vertices)))


    # detect logs
    response = client.logo_detection(image=image)


def get_image(image_name):
    file_name = os.path.join(
        os.path.dirname(__file__),
        'vods/facial_recognition/{}'.format(image_name))
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    return image