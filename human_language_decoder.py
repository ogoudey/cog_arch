import whisper

import datetime as dt
import time as t
import random
import os


import audio # audio slicer with configuration
import play



class Transcriber:
    def __init__(self):
        self.model = whisper.load_model("turbo")
        
        self.composition = dict()


if __name__ == "__main__":
    now = dt.datetime.now()
    time_str = now.strftime("%H-%M")
    
    trial = "trials/" + time_str
    os.makedirs(trial, exist_ok=True)
    print("Made checkpoint directory " + trial)
    me = Transcriber()
    index = 0
    a = audio.Recorder()
    a.record()
    while True:
        this_file = "./" + trial + "/" + str(index) + ".wav"
        a.write(this_file)
        #start_time = t.time()
        # hit checkpoint
        result = me.model.transcribe(this_file)
        me.composition[this_file] = result["text"]
        
        index += 1
        a = audio.Recorder()
        #stop_time = t.time()
        #print(str(stop_time - start_time) + " second lag.")
        a.record()
        print(*me.composition.values())

    
    
