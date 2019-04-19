#!/usr/bin/env python
import os
from pocketsphinx import AudioFile, get_model_path, get_data_path
#import urllib.parse
import json

class STTEngine:
    
    def __init__(self,audio_file, model_path=None):

        self.text = None
        self.audio_file = audio_file
        if model_path:
            self.model_path = model_path
        else:
            self.model_path = get_model_path()
        self.roman_to_number = {
                                    "i":"1st",
                                    "ii":"2nd",
                                    "iii":"3rd",
                                    "iv":"4th",
                                    "v":"5th",
                                    "vi":"6th",
                                    "vii":"7th",
                                    "viii":"8th",
                                    "ix":"9th",
                                    "x":"10th",
                                    "xi":"11th",
                                    "xii":"12th",
                                    "xiii":"13th",
                                    "xiv":"14th",
                                    "xv":"15th",
                                    "xvi":"16th",
                                    "xvii":"17th",
                                    "xviii":"18th",
                                    "xix":"19th",
                                    "xx":"20th"
            }
                

    def get_sphinx_text(self, audio_file, sample_rate, lang):        

        text = ''
        try:
            
            config = {
                'verbose': False,
                'audio_file': audio_file,
                'buffer_size': 2048,
                'no_search': False,
                'full_utt': False,
                'hmm': os.path.join(self.model_path, 'en-us'),
                'lm': os.path.join(self.model_path, 'en-us.lm.bin'),
                'dict': os.path.join(self.model_path, 'cmudict-en-us.dict')
            }
            config_in = {
                'verbose': False,
                'audio_file': audio_file,
                'buffer_size': 2048,
                'no_search': False,
                'full_utt': False,
                'hmm': os.path.join(self.model_path, 'en_in'),
                'lm': os.path.join(self.model_path, 'en-in.lm.bin'),
                'dict': os.path.join(self.model_path, 'en-in.dict')
            }

            
            print(config_in)
            print(config)
            audio = AudioFile(**config)
            
            for phrase in audio:
                text += str(phrase)
                print('CMU text:'+text)
            
            del audio
        except Exception as e:
            print('Error processing sphinx:', str(e))

        print('processed sphinx STT')
        return text


    def run(self):
       stt_info = {}#stt_sphinx_req_queue.get()
       stt_info['file'] = self.audio_file
       stt_info['sample_rate'] = 16000
       stt_info['lang'] = "en-IN"
       #stt_info = json.loads(stt_info)

       self.text = self.get_sphinx_text(stt_info['file'], stt_info['sample_rate'], stt_info['lang'])
  

stt_obj = STTEngine("test1.wav",os.getcwd()+'/cmusphinx-en-in-8khz-5.2')
stt_obj = STTEngine("test1.wav")

stt_obj.run()
print(stt_obj.text)
	
