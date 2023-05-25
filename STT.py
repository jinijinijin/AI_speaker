import speech_recognition as sr
from playsound import playsound

# 음성 인식 객체 생성
r = sr.Recognizer()

# 마이크로부터 오디오 입력 받기
with sr.Microphone() as source:
    print("음성 인식 대기 중...")

    while True:
        audio = r.listen(source)

        try:
            # 음성을 텍스트로 변환
            text = r.recognize_google(audio, language='ko-KR')

            # '다울아'를 감지하면 음성 입력 대기
            if '야' in text:
                playsound('ding.wav')  # 띠링 소리 재생
                print("다음 음성을 기다리는 중...")
                audio = r.listen(source, phrase_time_limit=5)
                text = r.recognize_google(audio, language='ko-KR')
                break

        except sr.UnknownValueError:
            print("음성을 인식할 수 없습니다.")
        except sr.RequestError:
            print("Google 음성 인식 서비스에 접근할 수 없습니다.")


    # '다울아'를 제외한 텍스트 결과 출력
    result_text = text.replace("야", "")
    print("인식 결과:", text.replace("야", ""))

    # 음성 인식 결과를 파일로 저장하는 코드 (UTF-8 인코딩 사용)
    result = result_text  # 음성 인식 결과
    filename = "STT_result.txt"  # 저장할 파일명

    with open(filename, "w", encoding="utf-8") as file:
        file.write(result)

    import subprocess
    import sys


    # 현재 파일 실행 완료 후 실행할 파일 경로
    next_file_path = './emotions.py'

    # 현재 파일 실행 완료 후 cmd 명령 실행
    def run_next_file():
        cmd_command = ['python', next_file_path]
        subprocess.Popen(cmd_command)

    # 현재 파일의 실행이 끝났을 때 호출되는 함수
    def on_file_completed():
        # 실행할 코드들...

        # 다음 파일 실행
        run_next_file()

    # 현재 파일의 실행이 끝났을 때 on_file_completed() 함수 호출
    if __name__ == '__main__':
        on_file_completed()


# import speech_recognition as sr
# import pyaudio
# from playsound import playsound
#
# # 음성 인식 객체 생성
# r = sr.Recognizer()
#
# # 마이크로부터 오디오 입력 받기
# with sr.Microphone() as source:
#     print("음성 인식 대기 중...")
#
#     while True:
#         audio = r.listen(source)
#
#         try:
#             # 음성을 텍스트로 변환
#             text = r.recognize_google(audio, language='ko-KR')
#
#             # '다울아'를 감지하면 띠링 소리 재생 및 음성 인식 시작
#             if '안녕' in text:
#                 playsound('ding.wav')  # 띠링 소리 재생
#                 audio = r.listen(source, phrase_time_limit=5)  # 최대 5초까지 입력 대기
#                 print("음성 인식 시작:", text)
#                 break
#
#         except sr.UnknownValueError:
#             print("음성을 인식할 수 없습니다.")
#         except sr.RequestError:
#             print("Google 음성 인식 서비스에 접근할 수 없습니다.")

