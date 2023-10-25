import pygame
import os
from tkinter import Tk, filedialog, Button, Label

# Inicializar pygame
pygame.init()

# Configurar la ventana principal de tkinter
root = Tk()
root.title("Reproductor de Música")
root.geometry("300x100")

# Lista para almacenar la lista de reproducción y el índice de la canción actual
playlist = []
current_song_index = 0

# Función para añadir canciones a la lista de reproducción
def add_to_playlist():
    file = filedialog.askopenfilename(initialdir="~/", title="Selecciona una canción",
                                      filetypes=(("Archivos MP3", "*.mp3"), ("Todos los archivos", "*.*")))
    if file:
        playlist.append(file)
        playlist_label.config(text="Playlist: " + os.path.basename(file))

# Función para reproducir la siguiente canción en la lista de reproducción
def play_next_song():
    global current_song_index
    if len(playlist) > 0:
        current_song_index = (current_song_index + 1) % len(playlist)
        pygame.mixer.music.load(playlist[current_song_index])
        pygame.mixer.music.play()

# Función para reproducir la canción anterior en la lista de reproducción
def play_previous_song():
    global current_song_index
    if len(playlist) > 0:
        current_song_index = (current_song_index - 1) % len(playlist)
        pygame.mixer.music.load(playlist[current_song_index])
        pygame.mixer.music.play()

# Función para pausar o reanudar la reproducción
def toggle_pause():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

# Botón para añadir canciones a la lista de reproducción
add_button = Button(root, text="Agregar Canción", command=add_to_playlist)
add_button.pack()

# Etiqueta para mostrar la lista de reproducción
playlist_label = Label(root, text="Playlist: ")
playlist_label.pack()

# Botones para controlar la reproducción
previous_button = Button(root, text="Anterior", command=play_previous_song)
previous_button.pack(side="left")
pause_button = Button(root, text="Pausa/Reanudar", command=toggle_pause)
pause_button.pack(side="left")
next_button = Button(root, text="Siguiente", command=play_next_song)
next_button.pack(side="left")

# Función para iniciar el bucle principal de tkinter
def start():
    root.mainloop()

# Iniciar el bucle principal de tkinter
start()
