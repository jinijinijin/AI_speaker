import cv2
import numpy as np
from keras.models import load_model
from statistics import mode
from utils.datasets import get_labels
from utils.inference import detect_faces
from utils.inference import draw_text
from utils.inference import draw_bounding_box
from utils.inference import apply_offsets
from utils.inference import load_detection_model
from utils.preprocessor import preprocess_input

# 링 버퍼 초기화
result_buffer = []

USE_WEBCAM = True  # If false, loads video file source

# parameters for loading data and images
emotion_model_path = './models/emotion_model.hdf5'
emotion_labels = get_labels('fer2013')

# hyper-parameters for bounding boxes shape
frame_window = 10
emotion_offsets = (20, 40)

# loading models
face_cascade = cv2.CascadeClassifier('./models/haarcascade_frontalface_default.xml')
emotion_classifier = load_model(emotion_model_path)

# getting input model shapes for inference
emotion_target_size = emotion_classifier.input_shape[1:3]

# starting lists for calculating modes
emotion_window = []

# starting video streaming

cv2.namedWindow('window_frame')
video_capture = cv2.VideoCapture(0)

# Select video or webcam feed
cap = None
if USE_WEBCAM:
    cap = cv2.VideoCapture(0)  # Webcam source
else:
    cap = cv2.VideoCapture('./demo/dinner.mp4')  # Video file source

while cap.isOpened():
    ret, bgr_image = cap.read()

    gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
    rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)

    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5,
                                          minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

    for face_coordinates in faces:
        x1, x2, y1, y2 = apply_offsets(face_coordinates, emotion_offsets)
        gray_face = gray_image[y1:y2, x1:x2]
        try:
            gray_face = cv2.resize(gray_face, (emotion_target_size))
        except:
            continue

        gray_face = preprocess_input(gray_face, True)
        gray_face = np.expand_dims(gray_face, 0)
        gray_face = np.expand_dims(gray_face, -1)
        emotion_prediction = emotion_classifier.predict(gray_face)
        emotion_probability = np.max(emotion_prediction)
        emotion_label_arg = np.argmax(emotion_prediction)
        emotion_text = emotion_labels[emotion_label_arg]
        emotion_window.append(emotion_text)

        if len(emotion_window) > frame_window:
            emotion_window.pop(0)
        try:
            emotion_mode = mode(emotion_window)
        except:
            continue

        if emotion_text == 'angry':
            color = emotion_probability * np.asarray((255, 0, 0))
            satisfaction = 'bad'
        elif emotion_text == 'sad':
            color = emotion_probability * np.asarray((0, 0, 255))
            satisfaction = 'bad'
        elif emotion_text == 'happy':
            color = emotion_probability * np.asarray((255, 255, 0))
            satisfaction = 'good'
        elif emotion_text == 'surprise':
            color = emotion_probability * np.asarray((0, 255, 255))
            satisfaction = 'not bad'
        else :
            color = emotion_probability * np.asarray((0, 255, 0))
            satisfaction = 'not bad'

        color = color.astype(int)
        color = color.tolist()

        draw_bounding_box(face_coordinates, rgb_image, color)
        draw_text(face_coordinates, rgb_image, emotion_mode,
                  color, 0, -45, 1, 1)

        # Display satisfaction in cmd
        print(f"표정: {emotion_text}")
        print(f"만족도: {satisfaction}")

        # 표정과 만족도 결과를 링 버퍼에 추가합니다
        result_buffer.append((emotion_text, satisfaction))

        # 링 버퍼 크기 유지
        if len(result_buffer) > 5:
            result_buffer.pop(0)

    bgr_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
    cv2.imshow('window_frame', bgr_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

# 캡처된 결과 출력
print("\n캡처된 결과:")
for emotion, satisfaction in result_buffer:
    print(f"표정: {emotion}, 만족도: {satisfaction}")

# 결과를 파일로 저장
with open('captured_results.txt', 'w') as f:
    for result in result_buffer:
        emotion_text, satisfaction = result
        f.write(f"Emotion: {emotion_text}\n")
        f.write(f"Satisfaction: {satisfaction}\n")

from collections import Counter

# 파일 읽기
with open('captured_results.txt', 'r') as f:
    lines = f.readlines()

    # 표정과 만족도 추출
    emotions = []
    satisfactions = []
    for i in range(0, len(lines), 2):
        emotion = lines[i].strip().split(': ')[1]
        satisfaction = lines[i+1].strip().split(': ')[1]
        emotions.append(emotion)
        satisfactions.append(satisfaction)

    # 등장 횟수 계산
    emotion_counts = Counter(emotions)
    satisfaction_counts = Counter(satisfactions)

    # 과반수인 표정과 만족도 출력
    majority_emotion = max(emotion_counts, key=emotion_counts.get)
    majority_satisfaction = max(satisfaction_counts, key=satisfaction_counts.get)

    print("\n과반수인 표정:", majority_emotion)
    print("과반수인 만족도:", majority_satisfaction)

    # 결과를 파일로 저장
    with open('emotion_result.txt', 'w') as f:
            f.write(f"표정: {majority_emotion}\n")
            f.write(f"만족도: {majority_satisfaction}\n")

import openai

# Set your OpenAI API key
openai.api_key = "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"

messages = []

# 다른 프로젝트에서 파일을 읽어 결과 사용하는 코드
filename = "emotion_result.txt"  # 음성 인식 결과가 저장된 파일명

with open(filename, "r") as file:
    result = file.read()

# result 변수에는 파일에서 읽어온 결과가 저장됨
print("\n사용자 표정 결과:", result)

emotion = result

if 'happy' in emotion:
    emotion = emotion.replace('happy', '행복해')
if 'angry' in emotion:
    emotion = emotion.replace('angry', '화가나')
if 'sad' in emotion:
    emotion = emotion.replace('sad', '우울해')
if 'surprise' in emotion:
    emotion = emotion.replace('surprise', '깜짝 놀라')
if 'neutral' in emotion:
    emotion = emotion.replace('neutral', '중립적이여')

content = "지금 표정이" + emotion + "보이는 사람에게 표정에 초점을 둬서 먼저 걸 수 있는 말 5개 생성해줘"
messages.append({"role": "user", "content": content})

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
)

chat_response = completion.choices[0].message.content
print(f'ChatGPT:\n{chat_response}')
messages.append({"role": "assistant", "content": chat_response})

# 결과를 파일로 저장
with open('chatGPT_result.txt', 'w', encoding="utf-8") as f:
    f.write(f"{chat_response}\n")

from gtts import gTTS
import os
import random

# File path of the GPT result file
filename = "chatGPT_result.txt"

# Read the contents of the file with UTF-8 encoding
with open(filename, "r", encoding="utf-8") as file:
    GPT = file.read()

# Split the text into lines
lines = GPT.splitlines()

# Randomly select a line from lines list
random_line = random.choice(lines)

# 1,2,3,4,5X
if '1.' in random_line:
    tts_text = random_line.replace("1.", "")
if '2.' in random_line:
    tts_text = random_line.replace("2.", "")
if '3.' in random_line:
    tts_text = random_line.replace("3.", "")
if '4.' in random_line:
    tts_text = random_line.replace("4.", "")
if '5.' in random_line:
    tts_text = random_line.replace("5.", "")



# # Print the selected line
# print(random_line)

# Create a gTTS object
tts = gTTS(text=tts_text, lang='ko')

# Output file path for the MP3 file
output_file = "output.mp3"

# Save the TTS as an MP3 file
tts.save(output_file)

# Play the MP3 file
os.system(f"start {output_file}")
