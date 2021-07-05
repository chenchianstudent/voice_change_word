# 文字轉聲音 參考影片:https://www.youtube.com/watch?v=xd_1rn89W2k
from gtts import gTTS
from pygame import mixer
import tempfile


a = input('請輸入文字或句子:')

def Speak(sentence):
    with tempfile.NamedTemporaryFile(delete = True) as fp:
         t = gTTS(text = sentence,lang = 'zh-TW')
         t.save('{}.mp3'.format(fp.name))
         mixer.init()
         mixer.music.load('{}.mp3'.format(fp.name))
         mixer.music.play()

Speak(a)
