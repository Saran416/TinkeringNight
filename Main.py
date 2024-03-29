import speech_recognition as sr
import pyttsx3
import TextRefiner
import NLP
import pyautogui
import cv2
import numpy as np

#initialize recognizer 
r = sr.Recognizer()

def record_text():
    #loop in case of erros
    while(1):
        try: 
            #use the microphone as source for input
            with sr.Microphone() as source1:
                r.adjust_for_ambient_noise(source1, duration=0.2)
                print("test2")
                audio1 = r.listen(source1,0,8)
                print("test")
                MyText = r.recognize_vosk(audio1)

                return MyText
        
        except sr.RequestError as e:
            print(f"Could no request results {e}")
        
        except sr.UnknownValueError:
            print("unknown value occured")
        
        except sr.WaitTimeoutError:
            print("Timeout waiting for audio")

    return


def output_text(text):
    f = open("output.txt","a");
    f.write(text)
    f.write("\n")
    f.close()
    return 


while(1):
    text = record_text()

    if(text!=None):
        output_text(text)
    print("wrote text")

    input_file = 'output.txt'
    output_file = 'final.txt'


    TextRefiner.remove_waste(input_file,output_file)

    if(NLP.isSimilar()):
        #take screenshot
        image = pyautogui.screenshot() 
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR) 
        # writing it to the disk using opencv 
        cv2.imwrite("image1.png", image)
    
    
