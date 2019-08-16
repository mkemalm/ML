import json
import ConfigParser
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

class connectapi:
    def __init__(self):
        config = ConfigParser.RawConfigParser()
        config.read('properties')
        apikey = config.get('API', 'api.key');
        apiver = config.get('API', 'api.ver');
    	self.visual_recognition = VisualRecognitionV3(apiver, api_key=apikey)
    def connect(self):
        return self.visual_recognition

