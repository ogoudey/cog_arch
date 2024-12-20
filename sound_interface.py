import human_language_decoder as hld

import threading

# Should have audio.py here...

def listen_for_hl(hl_decoder):
    exhaust = hl_decoder.run()
    if exhaust:
        print("Stopping listening due to: " + exhaust + " detected in: " + "".join(map(str, hl_decoder.composition.values())))
    else:
        print("How am I here?")
        
if __name__ == "__main__":
    s = hld.Transcription()
    t = threading.Thread(target=listen_for_hl, args=[s])
    t.start()
    # bulk
    t.join()
