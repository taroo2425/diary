import speech_recognition as speech_recog

# v1
def speech():
    mic = speech_recog.Microphone()
    recog = speech_recog.Recognizer()

    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
        return recog.recognize_google(audio, language="en-AU")
    
    
#v2 

mic = speech_recog.Microphone()
recog = speech_recog.Recognizer()

with mic as audio_file:
    print("silahkan bicaraa")
    recog.adjust_for_ambient_noise(audio_file)
    audio = recog.listen(audio_file)
    print("Mengkonversikan ucapan menjadi teks... :)")
    print("kamu ngomong giniii : " + recog.recognize_google(audio, language="en-AU"))

#inggris en-EN
#inggris Australia  en-AU
#indonesia id-ID
#jepang ja-JP
#france/prancis fr-FR
#china zh-CN
#spanyol es-ES