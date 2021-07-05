# 語音翻譯成文字  參考影片:https://www.youtube.com/watch?v=31DZfkYRvI4
import speech_recognition
r = speech_recognition.Recognizer()
print("請對著麥克風說話")
with speech_recognition.Microphone() as source:
    audio = r.listen(source)

ans = r.recognize_google(audio, language='zh-TW')
print("輸出結果如下:")
print(ans)

