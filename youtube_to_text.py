import sys
from youtube_transcript_api import YouTubeTranscriptApi
import pyperclip

# Función para obtener la transcripción de un video de YouTube
def get_transcript(video_id):
    try:
        # Obtiene la lista de transcripciones disponibles para el video
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        try:
            # Intenta encontrar una transcripción en español o inglés
            transcript = transcript_list.find_transcript(['es', 'en'])
        except Exception as e:
            # Si no se encuentra, busca una transcripción generada automáticamente
            transcript = transcript_list.find_generated_transcript([])
        transcript_text = ""
        # Construye el texto de la transcripción a partir de los elementos de la lista
        for elem in transcript.fetch():
            transcript_text += elem['text'] + " "

        return transcript.language_code, transcript_text
    except Exception as e:
        print("Error al obtener la transcripción:", e)
        return None, None

# Función para obtener el ID del video a partir de la URL
def get_video_id(url):
    if "watch?v=" in url:
        return url.split("watch?v=")[1].strip()
    else:
        print("URL inválida")
        return None

def main():
    while True:
        url = input("Introduce el enlace de YouTube: ")
        video_id = get_video_id(url)

        if video_id:
            language_code, transcript = get_transcript(video_id)
            if transcript:
                print(f"\nTranscripción ({language_code}):")
                print(transcript)
                pyperclip.copy(transcript)  # Copia la transcripción al portapapeles
                print("\nLa transcripción se ha copiado al portapapeles.")

        otro = input("¿Quieres buscar otra transcripción? (s/n): ")
        if otro.lower() != 's':
            break

if __name__ == "__main__":
    main()