from gtts import gTTS
import os

# TTS를 생성할 텍스트
text = "안녕하세요. TTS 예제입니다."

# gTTS 객체 생성
tts = gTTS(text=text, lang='ko')

# MP3 파일로 변환
tts.save("output.mp3")

# MP3 파일 재생
os.system("start output.mp3")