# -*- coding: utf-8 -*-
import requests
import simplejson as json
import sys


class Emotions:

    def __init__(self, subscription_key):
        self.key = subscription_key

    def getEmotionsSum(self,image_url):
        face_api_url = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/detect'
        headers = { 'Ocp-Apim-Subscription-Key': self.key }
        
        params = {
            'returnFaceId': 'true',
            'returnFaceLandmarks': 'false',
            'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
        }
    
        toHex = lambda x:"".join([hex(ord(c))[2:].zfill(2) for c in x])
    
        response = requests.post(face_api_url, params=params, headers=headers, json={"url": image_url})
        faces = response.json()
        i = 1
        SumaTotal = 0
        for face in faces:
            #print("Persona %s" %(i))
            SumaPersona = 0
            for emotion in face['faceAttributes']['emotion']:
                EmotionString = emotion
                PercentEmotion = face['faceAttributes']['emotion'][EmotionString]
                IntEmotion = int(toHex(EmotionString),16)
                CodecEmotion = IntEmotion * PercentEmotion
                SumaPersona += CodecEmotion
             #   print("%s %s = %s * %s = %s" % (emotion,PercentEmotion,IntEmotion,PercentEmotion,CodecEmotion))
            #print(SumaPersona)  
            SumaTotal+=SumaPersona
            i+=1
        return SumaTotal


