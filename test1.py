#pip install pygame
import pygame

def play_audio(audio_file_path):
    pygame.init()
    pygame.mixer.init()
    
    try:
        pygame.mixer.music.load(audio_file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print("Error while playing audio:", e)
    finally:
        pygame.mixer.quit()

audio_file_path = 'question_audio.mp3'  # Replace with the path to your MP3 audio file
play_audio(audio_file_path)
