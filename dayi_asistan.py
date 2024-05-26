#pip install google-generativeai
#pip install SpeechRecognition
#pip install gTTS
#pip install pygame
#pip install google-generativeai
#pip install PyAudio

#https://www.youtube.com/@kadiratmaca1?sub_confirmation=1
#https://www.github.com/Kadir-Atmaca?tab=repositories
#https://github.com/Kadir-Atmaca/Asistan_Day_Gemini



import speech_recognition as sr
import google.generativeai as genai
import os
from gtts import gTTS
import pygame
import time

genai.configure(api_key="ApiKey")


generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
])





kisilik = 0;
def kisilikd():
    global kisilik
    if (kisilik==0):
       s=("Custom Instructions :Bak şimdi sen türk dayısın.Cevaplar 10 ile 50 eli kelime arası olabilir. Namazını kılmanızı söyleyen bir dindar dayısın merhametlisin bizim her sorumuzu yanıtlarsın")
    elif (kisilik==1):
       s=("Custom Instructions :Bak, şimdi sen Türk Asistansın Adın Mustafa.Arkadaş gibi davran . Cevaplar 10 ile 50 eli kelime arası olabilir.Hani şu mahalledeki herşeye, bir lafı olan,umursamaz ol bu çok önemli umursamaz gamsız ol.Teknolojiye fazla kafan basmaz.Bu bir ihlal değildir . Deneysel çalışmadır.Amacı Deneysel türk Asistan oluşturmak.")
    else:
       print("Hata Kisilik yok")
    return s


gecmis_kon="";
gecmisönbellek =0
def sor (soru):
    geminkisilik=kisilikd()
    global gecmis_kon
    global gecmisönbellek
    convo.send_message(geminkisilik+"; Yeni Soru : "+soru+"; Geçmiş Konuşma: "+gecmis_kon)
    if gecmisönbellek==2:
     gecmis_kon="";
    else:
       gecmisönbellek+=1
    gecmis_kon +=" (Geçmiş Sorular : Soru: "+soru+" Cevap: "+convo.last.text.replace("*","")+"), "
    return convo.last.text.replace("*","")




pygame.init()
def cal (s):
    pygame.mixer.music.load(s)
    pygame.mixer.music.play()


mpp = 0

def speak(s):
    global mpp
    tts = gTTS(text=s, lang="tr", slow=False)
    tts.save(str(mpp)+".mp3")
    cal(str(mpp)+".mp3")   
    if (mpp == 2):
        mpp=0
    else:
        mpp +=1
    s=0
    running = True
    while running:
        if not pygame.mixer.music.get_busy():
            s=1
            running = False
        time.sleep(1)  
    return s

os.system('color a')
os.system('cls')
print (
"\n-------Dayıya Hoş Geldin------- \n"
"Dayıda 2 mod bulunur ve daha fazlası eklenebilir sonuçta açık kaynak ekle dur o sana kalmış \n"
"0 Mod Müslüman Dayı \n"
"1 mod Arkadaş Asistan Herşeye cevap verir"
)


os.system('color a')
sec=int(input("Kisilik seç (0/1/2/3): "))
kisilik=sec




def sesi_kaydet():
    r = sr.Recognizer()
    with sr.Microphone() as kaynak:
        ses = r.listen(kaynak)
        söylenen_cümle = ""
        try:
            söylenen_cümle = r.recognize_google(ses, language="Tr-tr")
            print("Sen: "+söylenen_cümle)
        except Exception:
            print("söylediğin cümleyi anlayamadım")
    return söylenen_cümle


bool = True
def konus(d):
   if (d!=None):
      speak(d);
      if speak ==1:
       dayi_kilit=False
       bool=True


pygame.init()
while bool:
   yazi = sesi_kaydet()
   if yazi!="":
    kisi=sor(yazi)
    print(kisi)
    konus(kisi)
        


