# Extract all frames from a video using Python (OpenCV)
import cv2

video_path = 'D:/A_PYTHON/ProgramasPython/Capturar Fotogramas_Video/video1.mp4'
cap = cv2.VideoCapture(video_path)

img_index = 0
while (cap.isOpened()):
    lectura, frame = cap.read()
    if lectura == False:
        break
    cv2.imwrite('Fotograma_' + str(img_index) + '.png', frame)
    img_index += 1

cap.release()
cv2.destroyAllWindows()
