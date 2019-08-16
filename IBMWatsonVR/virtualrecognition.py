import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3
from connectapi import connectapi

class virtualrecognition:
	def __init__(self):
        	self.vr = connectapi().connect()

	def classify(self, file_path):
		with open(file_path, 'rb') as image_file:
    			text_results = self.vr.classify(images_file=image_file)
    			print(json.dumps(text_results, indent=2))
	
	def detectface(self, file_path):
		with open(file_path, 'rb') as image_file:
			text_results = self.vr.detect_faces(images_file=image_file)
			print(json.dumps(text_results, indent=2))
	
	def imagetotext(self, file_path):
                with open(file_path, 'rb') as image_file:
                        text_results = self.vr.recognize_text(images_file=image_file)
                        print(json.dumps(text_results, indent=2))
