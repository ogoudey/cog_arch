import human_language_decoder as hld

import threading

# Should have audio.py here...



class SoundInterface:
    def __init__(self):
        self.s = hld.Transcription()
    
    def listen_for_hl(hl_decoder):
        exhaust = hl_decoder.run()
        """
        if exhaust:
            print("Stopping listening due to: " + exhaust + " detected in: " + "".join(map(str, hl_decoder.composition.values())))
        else:
            print("How am I here?")
        """
    
    def activate(self):
        t = threading.Thread(target=self.listen_for_hl, args=[self.s])
        t.start()
        t.join() # blocks until decoder stops
        
if __name__ == "__main__":
    s = hld.Transcription()
    t = threading.Thread(target=listen_for_hl, args=[s])
    t.start()
    # bulk
    t.join()
