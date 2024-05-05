import os
from tkinter import Tk, Text, Button, END, Label
from gtts import gTTS

def save_text():
    '''Guarda el texto en un archivo'''
    text = text_area.get("1.0", END)
    with open ('user_input.txt', 'w', encoding='utf-8') as file:
        file.write(text)
    status_label.config(text="Texto guardado con éxito")

def text_to_speech():
    ''' Convierte el texto a voz y lo reproduce'''
    text = text_area.get("1.0", END)
    speech = gTTS(text=text, lang='es', slow=False)
    speech.save('speech_output.mp3')
    os.system('start speech_output.mp3')
    status_label.config(text="Reproduciendo audio.")

#Ventana principal
root = Tk()
root.title('Texto a voz')

#Area de texto entrada usuario
text_area = Text(root, height=10, width=50)
text_area.pack()

# Boton para guardar texto
save_button = Button(root, text="Guardar Texto", command=save_text)
save_button.pack()

#Boton convertir texto a voz
speak_button = Button ( root, text='Reproducir Texto', command=text_to_speech)
speak_button.pack()

#Etiqueta de estado pra mostrar mensajes al usuario
status_label = Label(root, text="", fg='green')
status_label.pack()

root.mainloop()