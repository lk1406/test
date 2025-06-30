from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.utils import platform
import requests

if platform == 'android':
    from jnius import autoclass
    from android import activity

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.btn_mic = Button(
            text='🎤 Press to Speak',
            font_size=24,
            size_hint=(1, 0.3)
        )
        self.btn_mic.bind(on_release=self.start_speech)
        self.add_widget(self.btn_mic)

    def start_speech(self, instance):
        if platform == 'android':
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            RecognizerIntent = autoclass('android.speech.RecognizerIntent')

            intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH)
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL,
                            RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
            intent.putExtra(RecognizerIntent.EXTRA_PROMPT, "Speak now")

            activity.bind(on_activity_result=self.on_activity_result)
            currentActivity = PythonActivity.mActivity
            currentActivity.startActivityForResult(intent, 1001)

    def on_activity_result(self, request_code, result_code, intent):
        if request_code == 1001 and result_code == -1:
            results = intent.getStringArrayListExtra(
                autoclass('android.speech.RecognizerIntent').EXTRA_RESULTS)
            if results and results.size() > 0:
                text = results.get(0)
                print(f"[✔] You said: {text}")
                self.send_to_server(text)
        return True

    def send_to_server(self, command):
        url = "https://your-server.com/command"
        data = {"text": command}
        try:
            response = requests.post(url, json=data)
            print("[↑] Command sent:", response.status_code)
        except Exception as e:
            print("[×] Failed to send:", e)

class VoiceApp(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    VoiceApp().run()