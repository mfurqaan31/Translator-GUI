import sys
from tkinter import*
from tkinter import ttk, messagebox, scrolledtext
import googletrans
from googletrans import Translator
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os


root=Tk()
root.title("Translator")
root.resizable(True,True)
root.geometry("1920x1080")
root.config(bg="black")


def Translating():

    translated_text.config(state=NORMAL)
    translated_text.delete(1.0,END)
    try:
        for key,value in languages.items():
            if(value==(translated_combo.get() ) ):
                translate_to=key

        data=primary_text.get(1.0,END)
        translated_data=Translator().translate(data,dest=translate_to)
        translated_text.insert(1.0,translated_data.text)
    
    except Exception :
        messagebox.showerror("Error","Something went wrong please try again")
    
    translated_text.config(state=DISABLED)


def clear():

    translated_text.config(state=NORMAL)
    translated_text.delete(1.0,END)
    primary_text.delete(1.0,END)
    translated_text.config(state=DISABLED)
    combo.place_forget()
    Label3.place_forget()
    Label6.place_forget()
    record_button.place_forget()
    translated_combo.set("")
    combo.set("")


def copying():

    root.clipboard_clear()
    translated_text.config(state=NORMAL)
    root.clipboard_append(translated_text.get(1.0,END))
    translated_text.config(state=DISABLED)


def Exit():

    sys.exit()


def ask_recording():

    Label3.place(x=10, y=350)
    combo.place(y=355,x=170)
    combo.state(["readonly"])
    record_button.place(y=390, x=10)


def Record():
    
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        for key,value in languages.items():
            if(value==( combo.get() ) ):
                translate_to=key
        
        try:
            audio = recognizer.listen(source, timeout=None, phrase_time_limit=None)

            text = recognizer.recognize_google(audio, language=translate_to)
            translated_text.config(state=NORMAL)
            translated_text.delete(1.0,END)
            primary_text.delete(1.0,END)
            primary_text.insert(1.0,text)
            translated_text.config(state=DISABLED)
            Label6.place(x=10, y=450)
        
        except Exception :
            messagebox.showerror("Error","Something went wrong please try again")

        


def Play_audio():

    try:
        translated_text.config(state=NORMAL)
        text=translated_text.get(1.0,END)
        
        for key,value in languages.items():
            if(value==( translated_combo.get() ) ):
                translate_to=key
        
        translated_text.config(state=DISABLED)
        audio=gTTS(text,lang=translate_to)
        audio.save("Translated_text_audio.mp3")
        playsound("Translated_text_audio.mp3")
        os.remove("Translated_text_audio.mp3")
    
    except Exception :
        messagebox.showerror("Error","Something went wrong please try later")

    




languages=googletrans.LANGUAGES
lang_list= list(languages.values())


Label1=Label(root, text="Auto Detect",bg="black",fg="#cfff04",font=30)
Label1.place(x=5,y=15)

primary_text=scrolledtext.ScrolledText(root, height=10, width=50, wrap=WORD, font=50)
primary_text.grid(row=1, column=0, pady=40, padx=10)

trans_button=Button(root, text="Translate", bg="black",fg="#cfff04",font=40, command=Translating)
trans_button.grid(row=0, column=1, pady=70, rowspan=2)

translated_text=scrolledtext.ScrolledText(root, height=10, width=50, wrap=WORD, state=DISABLED, font=50)
translated_text.grid(row=1, column=3, pady=40, padx=10)

Label2=Label(root, text="Translate to",bg="black",fg="#cfff04", font=40)
Label2.grid(row=4,column=3)


translated_combo=ttk.Combobox(root, width=20, value=lang_list)
translated_combo.grid(row=2, column=3)
translated_combo.state(["readonly"])

clear_button=Button(root, text="Clear", font=40, command=clear, fg="#cfff04", bg="black", )
clear_button.grid(row=1, column=1, pady=50,rowspan=40)

copy_op=Button(root, text="Copy text", font=40, command=copying, fg="#cfff04", bg="black")
copy_op.grid(row=1, column=15,padx=10)

exiting=Button(root, text="Quit",bg="black",fg="#cfff04", font=50, command=Exit, height=1, width=8)
exiting.grid(row=15, column=1)

askrecord_button=Button(root, text="Use voice to translate", bg="black", fg="#cfff04", height=1, width=20, font=50, command=ask_recording)
askrecord_button.place(y=300,x=10)

audio_button=Button(root, text="Audio", bg="black", fg="#cfff04", height=1, width=8, font=50, command=Play_audio)
audio_button.grid(row=1, column=25)

combo=ttk.Combobox(root, width=20, value=lang_list)

Label3=Label(root, text="Select Language",bg="black",fg="#cfff04",font=30)

record_button=Button(root, text="By voice", bg="black", fg="#cfff04", font=8,command=Record)

Label6=Label(root, text="Silence detected. Stopping.",bg="black",fg="#cfff04", font=40)

root.mainloop()
