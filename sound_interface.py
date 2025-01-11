import human_language_decoder as hld

import threading

# Should have audio.py here...



class SoundInterface:
    def __init__(self):
        self.transcription = hld.Transcription()
    
    def listen_for_hl(self, hl_decoder, event):
        exhaust = hl_decoder.run(event)
        
        if exhaust:
            print("Stopping listening due to: " + exhaust + " detected in: " + "".join(map(str, hl_decoder.composition.values())))
        else:
            print("How am I here?")
    
    
    
     
    def mock_listen_for_hl(self, transcription, event): #not sure why we're passing this as an argument...
        index = 0
        while True:
            x = input("---type--->")
            self.transcription.composition[index] = x 
            event.set()  
            index += 1
     
     
            
    def activate(self):
        event = threading.Event()
        t = threading.Thread(target=self.listen_for_hl, args=[self.transcription, event])
        t.start()
        t.join() # blocks until decoder stops
        
if __name__ == "__main__":

    s = SoundInterface()
    event = threading.Event()
    t = threading.Thread(target=s.listen_for_hl, args=[s.transcription, event])
    t.start()
    
    text = ""
    while True:
        if event.is_set():
            
            
            latest_composition_index = max(s.transcription.composition.keys())
            
            message = s.transcription.composition[latest_composition_index]
            text = text + message
            print(">>>>>>>>>>>> Composition updated. Composition["+str(latest_composition_index)+"]: '" + message + "'")
            print("Text: " + text)
            
            event.clear()
        else:
            # mainloop room
            pass
    t.join()
    
    
    
    
    
    
    
"""

{0: '', 1: ' Hello', 2: '', 3: ' B.', 4: ' See.', 5: ' Thank you.', 6: ' F', 7: ' Thank you.', 8: ' H.', 9: ' get edits and you can see how it works for you.', 10: ' Okay.', 11: ' M.', 12: ' OP', 13: '', 14: ' R.', 15: ' S.', 16: ' T', 17: ' you.', 18: '', 19: '', 20: ' x', 21: ' Why?', 22: '', 23: ' No', 24: ' Bye.', 25: ' Bye!', 26: ' A', 27: ' See?', 28: '', 29: ' time.', 30: ' you.', 31: ' with.', 32: ' me.'}




"""
