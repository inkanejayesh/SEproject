import json
import os
import wave
import pyglet
from watson_developer_cloud import TextToSpeechV1

def exit_callback(dt):
    pyglet.app.exit()


def wait(s):		
	sound = pyglet.media.load('C:\\Users\\dell\\Desktop\\Watson\\'+s, streaming=False)
	sound.play()
	pyglet.clock.schedule_once(exit_callback , sound.duration)
	pyglet.app.run()

#wait('options.wav')


