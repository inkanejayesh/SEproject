import json
import os
import wave
import pyglet
from watson_developer_cloud import TextToSpeechV1

def exit_callback(dt):
    pyglet.app.exit()


def textToSpeech(s):
	print(s)
	text_to_speech = TextToSpeechV1(
	  username= "8ba64380-55fa-48f3-ace3-5ff29c7c4c2d",
	  password= "kq1Kow2q3FCY",
	    x_watson_learning_opt_out=True)  # Optional flag
	path="C:\\Users\\dell\\Desktop\\seProject\\seProject\\media\\myapp\\"
	audio_file= open(path+'test1.wav','wb')#('/mnt/c/Users/dell/Desktop/Watson/test1.wav','wb') 
	audio_file.write(text_to_speech.synthesize( s[0], accept='audio/wav',voice="en-US_AllisonVoice"))
	audio_file.write(text_to_speech.synthesize( s[1], accept='audio/wav',voice="en-US_AllisonVoice"))
	audio_file.write(text_to_speech.synthesize( s[2], accept='audio/wav',voice="en-US_AllisonVoice"))
	audio_file.write(text_to_speech.synthesize( s[3], accept='audio/wav',voice="en-US_AllisonVoice"))
	audio_file.write(text_to_speech.synthesize( s[4], accept='audio/wav',voice="en-US_AllisonVoice"))


	for i in range(5,len(s)):
		audio_file.write(text_to_speech.synthesize( s[i], accept='audio/wav',voice="en-US_AllisonVoice"))		

	#sound = pyglet.media.load(path+'test1.wav', streaming=False)
	#sound.play()

	#pyglet.clock.schedule_once(exit_callback , sound.duration)
	#pyglet.app.run()

'''
s=['a','b','c','d','e','r']
textToSpeech(s)#'Say reply to reply to this tweet, retweet to retweet this tweet or like to like this tweet')
'''