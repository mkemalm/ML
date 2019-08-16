from virtualrecognition import virtualrecognition
from os.path import join, dirname

classify_example = join(dirname(__file__), 'resources/car.jpg')
facedetect_example = join(dirname(__file__), 'resources/obama.jpg')
imagetotext_example = join(dirname(__file__), 'resources/text.jpg')
vr = virtualrecognition()

###vr.classify(classify_example)
###vr.detectface(facedetect_example)
vr.imagetotext(imagetotext_example)
