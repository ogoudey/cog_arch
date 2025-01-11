deaf = False # sync with args
if not deaf:
    import whisper

import datetime as dt
import time as t
import random
import os

import threading
import concurrent.futures
import queue

import audio # audio slicer with configuration
import play

from openai import OpenAI
client = OpenAI()

def transcribe(file_name, composition, index):
    str_index = str(index)
    print("Transcribing for index "+str_index+"...")
    a = t.time()
    model = whisper.load_model("tiny.en") # maybe all threads can use the same loaded model
    print("Model loaded for index "+str_index+". Inferencing...")
    result = model.transcribe(file_name)
    composition[index] = result["text"] # can multiple threads update a dict
    print("Finished Transcription in " + str(t.time() - a) + " seconds: " + result["text"] + "\n")
    print(composition)
    

def record(a, delay=False):
    a.record(delay)

def join_transcribers(transcribers, event):
    while True:
        try:
            transcriber = transcribers.get()
            print("Transcriber detected!")
            transcriber.join()
            print("Event set!")
            event.set()
        except Exception as e:
            print(e)
            print("No transciber in queue, waiting...")
            t.sleep(.1) # So this doesn't blow up... no rush...
  
    
class Transcription:
    def __init__(self):
        
        self.composition = dict()

# file to start transcribing; composition (dict); index (key) for where to put transcription (also in the name of the file)
# pass the transcription if all threads can use the sam emodel
    
    def run(self, event):
        now = dt.datetime.now()
        time_str = now.strftime("%H-%M")
        
        trial = "trials/" + time_str
        os.makedirs(trial, exist_ok=True)
        print("Made checkpoint directory " + trial)
        index = 0
        
        #transcribers = queue.Queue()
        #transcriber_joiner = threading.Thread(target=join_transcribers, args=[transcribers, event])
        #transcriber_joiner.start()
        
        t = None 
        while True:
            a = audio.Recorder(index)
            a.record()
            if t:
                t.join()
            this_file = "./" + trial + "/" + str(index) + ".wav"
            a.write(this_file)
               
            t = threading.Thread(target=transcribe, args=[this_file, self.composition, index])
            t.start()
            
            
            index += 1


        #transcriber_joiner.join()


if __name__ == "__main__":
    t = Transcription()
    t.run()
            

    
    
