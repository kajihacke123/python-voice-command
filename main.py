import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='th')
    tts.save("audio.mp3")
    os.system("mpg123 audio.mp3")

def recordAudio():
#Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
#    Speech recognition using Google Speech Recognition
    data = ""
    try:
#    Uses the default API key
#    To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio,language="th")
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    return data
 
def dekdoydev(data):
    if "เกจิ" in data:
        speak("ว่าไงครับ")

    if "สบายดีไหม" in data:
        speak("ตามสภาพค่ะ ช่วงฝนตก ต้องรักษาสุขภาพนะคะ")
    
    if "กี่โมงแล้ว" in data:
        speak(ctime())

    if "เปิดเพลงหน่อย" in data:
        speak("ได้เลยค่ะ sportify นะคะ")
        os.system("start https://music.youtube.com")

    if "เล่าเรื่องตลกให้ฟังหน่อย" in data:
        speak("ไม่ได้เป็นคนตลกค่ะ ถ้าจะฟังเรื่องละ 20 บาทค่ะ")

    if "เปิด Excel หน่อย" in data:
        speak("ได้เลยค่ะ Excel นะคะ")
        os.system("start Excel")

    if "แผนที่ประเทศไทย" in data:
        data = data.split(" ")
        speak("รอสักครู่คะพี่วรากร เดี๋ยวเปิดแผนที่ประเทศไทยให้ค่ะ")
        os.system("start https://www.google.co.th/maps/place/t...")
    
#Starting Conversation

time.sleep(2)
speak("สวัสดีค่ะพี่ที วันนี้มีอะไรให้ช่วยไหมคะ")

while 1:
    data = recordAudio()
    dekdoydev(data)