from datetime import datetime
import os
import pyaudio 
import requests
import time
import urllib.parse
import wave
import wget

class LarynxFrontend:
    def __init__(self):
        pass 

    def play_sound(self, wave_file):
        wave_file = wave.open(wave_file, 'rb')
        chunk = 1024
        player = pyaudio.PyAudio() 

        stream = player.open(
            format = player.get_format_from_width(wave_file.getsampwidth()),
            channels = wave_file.getnchannels(), 
            rate = wave_file.getframerate(),
            output = True
        )

        data = wave_file.readframes(chunk) 

        while data != b'':
            stream.write(data)
            data = wave_file.readframes(chunk)
        
        stream.close()
        player.terminate()
    
    def say(self, input_text, url='http://localhost:5002', file_name='tts.wav', keep_file=False):
        input_text = urllib.parse.quote(input_text)
        url = f'{url}/api/tts?text={input_text}&voice=en-us/ljspeech-glow_tts&vocoder=hifi_gan/universal_large&lengtshScale=0.7'
        wget.download(url, filename)
        self.play_sound('tts.wav')
        if keep_file:
            pass
        else:
            os.remove('tts.wav')

if __name__ == '__main__':
    l = LarynxFrontend()
    l.say("Longer sentences may take longer time.")
    