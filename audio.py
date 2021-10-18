from moviepy.editor import VideoFileClip


def converttomp3(mp4file, mp3file):
    video = VideoFileClip(mp4file)
    # получаем аудиодорожку
    audio = video.audio
    # сохраняем аудио файл
    audio.write_audiofile(mp3file)
    # уничтожаем объекты 
    audio.close()
    video.close()


my_clip = VideoFileClip(r'video_new.mp4')
my_clip.write_videofile(r'result_video.mp4', audio='audio.mp3')
