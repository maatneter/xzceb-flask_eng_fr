"""uses os, json, watson, cloudsdk,  and dotenv"""

import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticor = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
     authenticator=authenticor
)

language_translator.set_service_url(url)

def englishtofrench(englishtext):
    """translates english to french"""
    if englishtext:
        translation = language_translator.translate(text = englishtext,
            model_id='en-fr').get_result()
        text = (json.loads(json.dumps(translation, indent=2)))
        frenchtext = text["translations"][0]["translation"]
    else:
        frenchtext = ""
    return frenchtext

def frenchtoenglish(frenchtext):
    """translates french to english"""
    if frenchtext:
        translation = language_translator.translate(text = frenchtext,
            model_id='fr-en').get_result()
        text = (json.loads(json.dumps(translation, indent=2)))
        englishtext = text["translations"][0]["translation"]
    else:
        englishtext = ""
    return englishtext
