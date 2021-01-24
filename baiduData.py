import json
import os
import random
import time

import pygame
import requests
from aip import AipSpeech
import speech_recognition as sr

APP_ID = '22065396'
API_KEY = 'ByGQGXyIeqG6dCTsgMLLOdtw'
SECRET_KEY = 'MyqPjj588fsNhXI166L9PhpaaHFuNk0w'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
TURING_KEY = '53fe09a108f1459d9400a1200b361363'
API_URL = 'http://openapi.tuling123.com/openapi/api/v2'
file_name = ''
# 录音
def rec(rate=16000):
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=rate) as source:
        print('please say something')
        audio = r.listen(source)

    with open("recording.wav", "wb") as f:
        f.write(audio.get_wav_data())

# 百度语音转文字
def listen():
    with open('recording.wav', 'rb') as f:
        audio_data = f.read()

    result = client.asr(audio_data, 'wav', 16000, {
        'dev_pid': 1537
    })
    text_input = result['result'][0]
    print('我说：' + text_input)
    Robot_think(text_input)

#图灵根据文字返回对话
def Robot_think(text_input):
    req = {
        "perception": {
            "inputText": {
                "text": text_input
            },
            "selfInfo": {
                "location":{
                    "city": "福州",
                    "province": "福建",
                    "street": "永丰佳园"
                }
            }
        },
        "userInfo": {
            "apiKey": TURING_KEY,
            "userId": "656453"
        }
    }
    req = json.dumps(req).encode('utf')
    response = requests.post(API_URL, data=req, headers={'content-type': 'application/json'})
    response_dic = json.loads(response.text)
    response_text = response_dic['results'][0]['values']['text']
    print(response_dic['results'][0]['values']['text'])
    du_say(response_text)

# 百度文字转语音
def du_say(results_text):
    result = client.synthesis(results_text, 'zh', 1, {
        'vol': 5,
        'per': 4,
        'spd': 4
    })
    # print(result)
    if not isinstance(result, dict):
        # if os.path.exists(file_name):
        #     os.remove(file_name)
        # global file_name
        delete_mp3()
        file_name = 'robot' + str(random.randint(10, 99999999)) + '.mp3'
        with open(file_name, 'wb') as f:
            f.write(result)
            f.close()
        play_mp3(file_name)

# pygame播放语音
def play_mp3(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)
    pygame.mixer.music.stop()
    pygame.mixer.quit()

# 读取语音文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 删除目录下的mp3文件
def delete_mp3():
    g = os.walk(os.getcwd())
    for path, d, files in g:
        for file_item in files:
            if 'mp3' in file_item:
                try:
                    os.remove(file_item)
                except Exception as e:
                    print(e)
                    continue
                finally:
                    pass

if __name__ == '__main__':
    # Robot_think('你是谁')
    # du_say('你是谁')
    # play_mp3('robot.mp3')
    pass
    # result = client.asr(get_file_content('recording.wav'), 'wav', 16000, {
    #     'dev_pid': 1537
    # })
    # print(result)
    # rec()
    # old_file1 = os.path.dirname(os.path.abspath(__file__)) + '/robot5279016.mp3'
    # old_file2 = os.getcwd() + '/robot5279016.mp3'
    # old_file3 = 'robot5279016.mp3'
    # print(old_file1)
    # print(old_file2)
    # print(os.path.exists(old_file1))
    # print(os.path.exists(old_file2))
    # print(os.path.exists(old_file3))
    # os.remove(old_file3)
    # print(os.path.dirname(os.path.abspath(__file__)))
    while True:
        rec()
        listen()

    # delete_mp3()