import cv2
video_capture = cv2.VideoCapture("video.mp4")

# Создаем пакет фото из видео 
if video_capture.isOpened():
    currentFrame = 0
while True:
    # get frame by frame
    ret, frame = video_capture.read()
    if ret:
      name = str(currentFrame) +'.png'
      print ('Creating...' + name)
      cv2.imwrite(name,frame)
    else:
        break
    currentFrame += 1

# Расчет FPS и кол-во кадров в исходнике 
fps = video_capture.get(cv2.CAP_PROP_FPS)
allFrames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
print ("Frames per second using video.get(cv2.CAP_PROP_FPS) : ".format(fps))
print ("Frames " , allFrames)

#Создаем видео
frameIns = 0
out = cv2.VideoWriter("video_new.mp4", cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, (480, 848)) #создаем видео, fps - расчитано Добавить разрешение видео
#cv2.VideoWriter_fourcc('M','J','P','G')  - кодек AVI 
while frameIns<=allFrames: 
    out.write(cv2.imread(str(frameIns)+'.png'))#добавляем картинки
    frameIns += 1
out.release() #генерируем

#Завершаем
cv2.destroyAllWindows()
video_capture.release()
print ("Ready")
