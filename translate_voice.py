import pandas as pd
import numpy as np

from ibm_watson import SpeechToTextV1 
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

url_s2t = "https://api.au-syd.speech-to-text.watson.cloud.ibm.com"
iam_apikey_s2t = "kdjfsa.kl"

authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
s2t

# !wget -O PolynomialRegressionandPipelines.mp3  https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/PolynomialRegressionandPipelines.mp3

filename='D:\github\python\PolynomialRegressionandPipelines.mp3'

with open(filename, mode="rb")  as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')

response.result

from pandas import json_normalize

json_normalize(response.result['results'],"alternatives")

print(response)
recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
type(recognized_text)