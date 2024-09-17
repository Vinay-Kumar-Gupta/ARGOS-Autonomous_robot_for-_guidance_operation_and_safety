# ================================== IMPORTS ==================================

import time
import pvporcupine
from pvrecorder import PvRecorder
import pvrhino
import random
import pygame

# ================================== DECLARATIONS =====================================

access_key = "tZd2lX4gcFDCnvykYlyl5gftK8dv9qZG8gaFO2ETkk7xwnxVpzvtLw=="


# ======================================= SOUNDS =======================================

follow_up_sounds = ["follow_1.mp3", "follow_2.mp3"]

welcome_sounds = ["start_up_lines_1.mp3","start_up_lines_2.mp3","start_up_lines_3.mp3","start_up_lines_4.mp3"]

again_sounds = ["didnt_get_1.mp3","didnt_get_2.mp3"]

oky_sounds = ["oky_1.mp3","oky_2.mp3"]

error_sounds = ["error_1.mp3","error_2.mp3","error_3.mp3"]

# =============================================== PYGAME SOUND FUNCTION ==========================================

def sound_func(variable_name,file_path):

    rand = random.choice(variable_name)

    pygame.mixer.init()# remember that i have added this for stopping the loop for some time
    pygame.mixer.music.load(f"sounds\{file_path}\{rand}") 
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)


# =============================================== REQUEST CONTROL ================================================

def control_appliance(appliance, number, status):
    try:
        

    except Exception as e:
        print(f"An error occurred: {e}")



# =============================================== WAKE WORD FUNCTION ================================================

def wake_word_func():
    
    
    
    wake_status = True
    room_no = ""
    try:

        sound_func(welcome_sounds,"welcome")
        porcupine = pvporcupine.create(access_key=access_key,
                                        keyword_paths=["ARGOS_en_windows_v3_0_0.ppn"])
        rhino = pvrhino.create(access_key=access_key,
                                        context_path="ARGOS_intents_en_windows_v3_0_0.rhn")

        
# =============================================== WAKE WORD ================================================

        recorder = PvRecorder(device_index=-1,frame_length=porcupine.frame_length)
        


        while True:
            if wake_status:
                print("Waiting for the wake-Word....")
                recorder.start()
                wake_status=False
            audio_frame = recorder.read()
            keyword_index = porcupine.process(audio_frame)

            if keyword_index == 0:
                flag=True
                print("Wake-word - Detected")

                recorder.stop() # i put this before, because I was delaying the loop

                sound_func(follow_up_sounds,"follow_up")
                
                
# =============================================== INTENTS ================================================

                try:

                    start_time = time.time()
                    print("Speak command : ")
                    recorder.start()
                    
                    while (flag==True and ((time.time()-start_time)<=4)):
                
                        audio_frame = recorder.read()
                        is_finalized = rhino.process(audio_frame)
           
                     
                        if is_finalized:                  
                            inference = rhino.get_inference()
                            
                            if inference.is_understood:
                                slots = inference.slots
                                print(slots)
                                sound_func(oky_sounds,"ok")

                                status = slots.get("status")
                                mode = slots.get("mode")
                                if slots.get("number_1") is not None:
                                    room_no = (slots.get("number_1")+slots.get("number_2")+slots.get("number_3"))

                                print(status,mode,room_no)
                                flag=False
                                recorder.stop()
                       
                        if int(time.time()-start_time)==4 and flag == True:
                                sound_func(again_sounds,"didnt_get")
                                recorder.stop()

                
                finally:
                    wake_status=True
                    print("TIME OVER")

    finally:
        porcupine.delete()
        rhino.delete()
        recorder.stop()
        recorder.delete()

wake_word_func()
