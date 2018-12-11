import boto3

if __name__ == "__main__":
    image_file = 'input.jpg'
    client = boto3.client('rekognition')

    with open(image_file,'rb') as image:
        response = client.detect_labels(image = {'Bytes': image.read()})

    print('Detected labels in ' + image_file)

    for label in response['Labels']:
        print(label['Name'] + ' : ' + str(label['Confidence']))

    print('Done....')