import webbrowser
import time

import pyautogui
import speech_recognition as sr

import helpers.helpers as helpers


def parse_episode(command: list) -> list:
    numbers_from_input = [word for word in command if helpers.is_int(word)]
    first_number = int(numbers_from_input[0])
    return first_number

def full_screen(width, height):
    pyautogui.moveTo(width * (1475 / 1920), height * (927 / 1080))
    pyautogui.click()


def main():
    width, height = pyautogui.size()
    r = sr.Recognizer()
    lookup = {"episode": 0}
    while True:
        try:
            with sr.Microphone(device_index=1) as audio_source:
                r.adjust_for_ambient_noise(audio_source, duration=.5)
                print("ready to accept audio")
                audio = r.listen(audio_source)
                text = r.recognize_google(audio)
                text = [word.lower() for word in str(text).split(" ")]
                if "case" in text and "closed" in text:
                    lookup["episode"] = parse_episode(text)
                    url = f"https://animekisa.tv/case-closed-dubbed-episode-{lookup['episode']}"
                    webbrowser.open(url)
                    time.sleep(1)
                    pyautogui.moveTo(width * 3 / 4, height / 3, duration=5)
                    pyautogui.click()
                    full_screen(width, height)
                elif "next" in text:
                    pyautogui.moveTo(width - 10, 0, duration=.5)
                    pyautogui.click()
                    lookup['episode'] = lookup['episode'] + 1
                    url = f"https://animekisa.tv/case-closed-dubbed-episode-{lookup['episode']}"
                    webbrowser.open(url)
                    time.sleep(1)
                    pyautogui.moveTo(width * 3 / 4, height / 3, duration=5)
                    pyautogui.click()
                    full_screen(width, height)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
