from . import imageRecognitionModule
from . import textToSpeechModule
from . import scrapModule
import os

def foo():
	scrapModule.getUrl()
	fname=os.listdir('C:\\Users\\dell\\Downloads')
	dirpath='C:\\Users\\dell\\Downloads'
	fname.pop(0)
	#print(fname)
	fname.sort(key=lambda p: os.stat(dirpath+'\\'+p).st_mtime, reverse=True)
	#print(fname)
	s=imageRecognitionModule.imageRecognition(dirpath+'\\'+fname[0])
	print(s)
	result=''
	for x in s:
		result+=(x+'. ')
	print(result)
	result=result.replace("'"," ",100000)
	result=result.replace('"'," ",100000)
	result=result.replace("["," ",100000)
	result=result.replace("]"," ",100000)
	result=result.replace("{"," ",100000)
	result=result.replace("}"," ",100000)
	#textToSpeechModule.textToSpeech(s)
	return result
	#textToSpeechModule.textToSpeech(s)


