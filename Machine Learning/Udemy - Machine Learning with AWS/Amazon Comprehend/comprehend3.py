import boto3
import json

comprehend = boto3.client(service_name = 'comprehend',region_name = 'us-east-1')
text = 'It is raining today in Seattle'

print('Calling DetectKeyPhrases')
print(json.dumps(comprehend.detect_key_phrases(text=text,LaguageCode = 'en')))
print('End of DetectKeyPhrases')