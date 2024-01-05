import tkinter as tk
from tkinter import messagebox
import re
from pytube import YouTube

def obter_id_video(url):
    padrao = r"(?:v=|v\/|vi=|vi\/|youtu\.be\/|embed\/|\/shorts\/|\/embed\/|\/v\/|\/e\/|watch\?v=|watch\?.+&v=|watch\?.+&vi=|watch\?v=|watch\?vi=|z\/|\/videos\/|\/www\.)(([^\"\&\?\/\s]*))"
    match = re.search(padrao, url)
    if match:
        return match.group(1)
    else:
        return None

def converter():
    try:
        video_url = entry_video.get()
        video_id = obter_id_video(video_url)

        print("URL inserido:", video_url)
        print("ID do vídeo:", video_id)

        if video_id:
            youtube = YouTube(video_url)
            video = youtube.streams.first()
            video.download('.python/video')
            messagebox.showinfo("Sucesso", "Vídeo salvo com sucesso")
        else:
            messagebox.showerror("Erro", "Não foi possível extrair o ID do vídeo.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

root = tk.Tk()
root.title("Conversor de vídeo")

label_crit1 = tk.Label(root, text="*Coloque seu link aqui:")
label_crit1.pack()

entry_video = tk.Entry(root)
entry_video.pack()

btn_baixar = tk.Button(root, text="Baixar", command=converter)
btn_baixar.pack()

root.mainloop()
