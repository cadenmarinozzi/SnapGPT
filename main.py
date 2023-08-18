import keyboard
import subprocess
import openai
import dotenv
import os
import pytesseract
import threading
import time
import rumps
from PIL import Image


dotenv.load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HAS_GPT4 = os.getenv("HAS_GPT4")
KEYBIND = os.getenv("KEYBIND")

openai.api_key = OPENAI_API_KEY


def takeScreenshot():
    subprocess.run(["screencapture", "-i", "/tmp/tesseract.png"])


def recognizeText():
    text = pytesseract.image_to_string(Image.open("/tmp/tesseract.png"))

    return text.strip()


def createChatCompletion(text):
    messages = [{"role": "user", "content": text}]

    completion = openai.ChatCompletion.create(
        model=HAS_GPT4 and "gpt-4" or "gpt-3.5-turbo", messages=messages
    )

    return completion.choices[0].message.content


def copyToClipboard(text):
    subprocess.run("pbcopy", text=True, input=text)


def screenshotAndRecognize(statusBar):
    threading.Thread(
        target=statusBar.updateTitle, args=("Taking Screenshot...",)
    ).start()

    takeScreenshot()

    threading.Thread(
        target=statusBar.updateTitle, args=("Recognizing Text...",)
    ).start()

    text = recognizeText()

    threading.Thread(
        target=statusBar.updateTitle, args=("Generating Response...",)
    ).start()

    completion = createChatCompletion(text)

    threading.Thread(target=statusBar.updateTitle, args=("Copying...",)).start()

    copyToClipboard(completion)

    threading.Thread(target=statusBar.updateTitle, args=("Copied!",)).start()

    time.sleep(2)
    statusBar.title = f"SnapGPT ({KEYBIND})"


class StatusBar(rumps.App):
    def __init__(self):
        super(StatusBar, self).__init__(f"SnapGPT ({KEYBIND})")
        self.menu = ["Take Screenshot", f"Keybind ({KEYBIND})"]

    def updateTitle(self, title):
        self.title = title

    @rumps.clicked("Take Screenshot")
    def screenshot(self, _):
        screenshotAndRecognize(self)


if __name__ == "__main__":
    statusBar = StatusBar()

    keyboard.add_hotkey(KEYBIND, screenshotAndRecognize, args=(statusBar,))

    statusBar.run()
    keyboard.wait()
