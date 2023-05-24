from gtts import gTTS
import os

# TTS를 생성할 텍스트
text = "오늘은 기분이 좋아보이시네요 좋은일 있으신가요?"

# gTTS 객체 생성
tts = gTTS(text=text, lang='ko')

# MP3 파일로 변환
tts.save("output.mp3")

# MP3 파일 재생
os.system("start output.mp3")