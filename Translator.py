import sys
from tkinter import*
from tkinter import ttk, messagebox, scrolledtext
import googletrans
from googletrans import Translator


root=Tk()
root.title("Translator")
root.resizable(False,False)
root.geometry("1200x550")
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

    
        

    except Exception as e:
        messagebox.showerror("Error",e)
    
    translated_text.config(state=DISABLED)

def clear():
    translated_text.config(state=NORMAL)
    translated_text.delete(1.0,END)
    primary_text.delete(1.0,END)
    translated_text.config(state=DISABLED)

def copying():
    root.clipboard_clear()
    translated_text.config(state=NORMAL)
    root.clipboard_append(translated_text.get(1.0,END))
    translated_text.config(state=DISABLED)

def Exit():
    sys.exit()

languages=googletrans.LANGUAGES
lang_list= list(languages.values())


Label1=Label(root, text="Auto Detect",bg="black",fg="#cfff04",font=30)
Label1.place(x=10, y=10)

primary_text=scrolledtext.ScrolledText(root, height=10, width=50, wrap=WORD, font=50)
primary_text.grid(row=1, column=0, pady=40, padx=10)

trans_button=Button(root, text="Translate", bg="black",fg="#cfff04",font=40, command=Translating)
trans_button.grid(row=1, column=1, padx=1)

translated_text=scrolledtext.ScrolledText(root, height=10, width=50, wrap=WORD, state=DISABLED, font=30)
translated_text.grid(row=1, column=3, pady=40, padx=10)

Label2=Label(root, text="Translate to",bg="black",fg="#cfff04", font=40)
Label2.place(y=263, x=650)


translated_combo=ttk.Combobox(root, width=20, value=lang_list)
translated_combo.grid(row=2, column=3)
translated_combo.state(["readonly"])

clear_button=Button(root, text="Clear", font=40, command=clear, fg="#cfff04", bg="black")
clear_button.place(y=180, x=503)

copy_op=Button(root, text="Copy text", font=40, command=copying, fg="#cfff04", bg="black")
copy_op.place(y=70, x=1070)

exiting=Button(root, text="Quit",bg="black",fg="#cfff04", font=50, command=Exit)
exiting.place(y=470, x=515)

root.mainloop()
