from speech_recognition import Microphone, Recognizer, exceptions

def SpeechRecognition():

    print("Listening!")

    speech_recognizer = Recognizer()

    with Microphone() as mic:

        try:

            speech_recognizer.adjust_for_ambient_noise(mic, duration=0.2)

            text = speech_recognizer.recognize_google(speech_recognizer.listen(mic), language="en-US")

            text = str(text).lower()

            return text

        except exceptions.UnknownValueError:

            return ""

        except Exception as e:

            return ""


print("You said: " + SpeechRecognition())
print("You said: " + SpeechRecognition())
