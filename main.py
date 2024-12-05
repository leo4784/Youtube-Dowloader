import yt_dlp

def baixar_video(url, output_path='.'):
    # Configurações de download
    ydl_opts = {
        'format': 'mp4',  # Baixar diretamente o formato MP4
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Definindo o nome do arquivo de saída
        'noplaylist': True,  # Evita baixar playlists
        'quiet': False,  # Mostra informações sobre o progresso
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == '__main__':
    url_video = input('Digite a URL do vídeo do YouTube: ')  # Ex: https://www.youtube.com/watch?v=abcd1234
    caminho = input('Digite o diretório de saída (deixe em branco para salvar na pasta atual): ')
    if not caminho:
        caminho = '.'
    baixar_video(url_video, caminho)
    print("Download concluído!")
