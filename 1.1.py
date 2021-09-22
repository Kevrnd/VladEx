import cv2
import math
# Поворот изображения
def rotation(image, angleInDegrees):
    h, w = image.shape[:2]
    img_c = (w / 2, h / 2)

    rot = cv2.getRotationMatrix2D(img_c, angleInDegrees, 1)

    rad = math.radians(angleInDegrees)
    sin = math.sin(rad)
    cos = math.cos(rad)
    b_w = int((h * abs(sin)) + (w * abs(cos)))
    b_h = int((h * abs(cos)) + (w * abs(sin)))

    rot[0, 2] += ((b_w / 2) - img_c[0])
    rot[1, 2] += ((b_h / 2) - img_c[1])

    outImg = cv2.warpAffine(image, rot, (b_w, b_h), flags=cv2.INTER_LINEAR)
    return outImg

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


# Поворачиваем все изображения

numImage = 0
while numImage <allFrames:
    fileName = str(numImage) + '.png'
    image = cv2.imread(fileName)
    ChangeImage =rotation (image, 0.05)
    fileName = str(fileName + 'C.png')
    cv2.imwrite(fileName,ChangeImage)
    numImage += 1

#Создаем видео
frameIns = 0
out = cv2.VideoWriter("video_new.mp4", cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, (480, 848)) #создаем видео, fps - расчитано Добавить разрешение видео
#cv2.VideoWriter_fourcc('M','J','P','G')  
while frameIns<=allFrames: 
    out.write(cv2.imread(str(frameIns)+'.png'))#добавляем картинки
    frameIns += 1
out.release() #генерируем

#Завершаем
cv2.destroyAllWindows()
video_capture.release()
print ("Ready")
