import os
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
        data = r.recognize_google(audio, language="th")
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
        speak("ตามสภาพครับ ช่วงฝนตก ต้องรักษาสุขภาพนะครับ")
    
    if "กี่โมงแล้ว" in data:
        speak(ctime())

    if "เปิดเพลงหน่อย" in data:
        speak("ได้เลยครับ youtube music นะครับ")
        os.system("start https://music.youtube.com")

    if "เปิดเพลง" in data:
        speak("ได้เลยครับ youtube music นะครับ")
        os.system("start https://music.youtube.com")

    if "เล่าเรื่องตลกให้ฟังหน่อย" in data:
        speak("ไม่ได้เป็นคนตลกครับ ถ้าจะฟังเรื่องละ 20 บาทครับ")

    if "เปิด Excel หน่อย" in data:
        speak("ได้เลยครับ Excel นะครับ")
        os.system("start Excel")

    if "เปิด Excel" in data:
        speak("ได้เลยครับ Excel นะครับ")
        os.system("start Excel")

    if "แผนที่ประเทศไทย" in data:
        data = data.split(" ")
        speak("รอสักครู่ครับพี่เกจิ เดี๋ยวเปิดแผนที่ประเทศไทยให้ครับ")
        os.system("start https://www.google.co.th/maps/place/t...")

    if "เปิด Google" in data:
        speak("เปิด google ให้ครับ")
        os.system("start https://www.google.co.th/")

    if "เปิดกล้อง" in data:
        speak("เปิด camera ให้ครับ")
        os.system("start microsoft.windows.camera:")

    if "เปิด obs" in data:
        speak("เปิด obs ให้ครับ")
        current_dir = os.getcwd()  # Save the current working directory
        obs_path = r"C:\Program Files\obs-studio\bin\64bit"
        os.chdir(obs_path)  # Change to the OBS directory
        os.system("obs64.exe")
        os.chdir(current_dir)  # 

    if "เปิด Messenger" in data:
        speak("เปิด Messenger ให้ครับ")
        os.system("start https://www.messenger.com/")

    if "เปิดการตั้งค่าเสียง" in data:
        speak("เปิดการตั้งค่าเสียง ให้ครับ")
        os.system("start ms-settings:sound")

    if "ขอเพลงแจ๊ส" in data:
        speak("เปิดเพลง jazz ให้ครับ")
        os.system("start https://music.youtube.com/watch?v=eOrGawCeFRQ&list=RDATgy")

    if "ปิดคอม" in data:
        speak("ปิดคอม ให้ครับ")
        os.system("shutdown /s /t 1")

    if "เปิด tiktok" in data:
        speak("เปิด tiktok ให้ครับ")
        os.system("start https://www.tiktok.com/")

    if "ขอเพลงเพราะๆ" in data:
        speak("เปิดเพลงเพราะ ให้ครับ")
        os.system("start https://music.youtube.com/watch?v=JGwWNGJdvx8&list=RDAMVMJGwWNGJdvx8")

    if "เปิด YouTube" in data:
        speak("เปิด Youtube ให้ครับ")
        os.system("start https://www.youtube.com/")

    if "เปิดแชท gpt" in data:
        speak("เปิด chatgpt ให้ครับ")
        os.system("start https://chat.openai.com/")

    if "เปิด Steam" in data:
        speak("เปิด steam ให้ครับ")
        os.system("start steam")

    if "เปิด Discord" in data:
        speak("เปิด discord ให้ครับ")
        os.system("start discord")
#Starting Conversation

time.sleep(2)
speak("สวัสดีค่ะพี่เกจิ วันนี้มีอะไรให้ช่วยไหมคะ")

while 1:
    data = recordAudio()
    dekdoydev(data)