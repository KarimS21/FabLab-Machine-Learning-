import cv2
import numpy as np
from naoqi import ALProxy
import vision_definitions
from PIL import Image
import time

def showNaoImage(IP, PORT):
    """
    Obtiene una imagen desde NAO, detecta rostros y muestra la cantidad detectada.
    """
    camProxy = ALProxy("ALVideoDevice", IP, PORT)
    resolution = vision_definitions.kVGA  # 640x480
    colorSpace = vision_definitions.kRGBColorSpace
    fps = 30

    videoClient = camProxy.subscribeCamera("python_client", 0, resolution, colorSpace, fps)

    t0 = time.time()
    naoImage = camProxy.getImageRemote(videoClient)
    t1 = time.time()
    print("Retraso en la adquisici:", t1 - t0)

    camProxy.releaseImage(videoClient)

    imageWidth = naoImage[0]
    imageHeight = naoImage[1]
    array = naoImage[6]
    pilImage = Image.frombytes("RGB", (imageWidth, imageHeight), array)

    # Convertir la imagen PIL a formato OpenCV
    open_cv_image = np.array(pilImage)
    open_cv_image = open_cv_image[:, :, ::-1].copy()  # Convertir RGB a BGR

    # Usar el clasificador Haar para deteccin de caras
    cascadePath = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cascadePath)

    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)

    # Detectar rostros en la imagen
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Dibujar rectgulos alrededor de las caras detectadas
    for (x, y, w, h) in faces:
        cv2.rectangle(open_cv_image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Mostrar la imagen
    cv2.imshow("Caras detectadas", open_cv_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Mostrar cantidad
    num_faces = len(faces)
    print("Cantidad de caras detectadas: {}".format(num_faces))
    tss = ALProxy("ALTextToSpeech", IP, PORT)
    tss.say("He detectado {} caras".format(num_faces))
    # Guardar imagen
    cv2.imwrite("nao_faces_detected.png", open_cv_image)

    # Cancelar suscripcin
    camProxy.unsubscribe(videoClient)

# Direccin IP y puerto del robot NAO
IP = "192.168.108.90"
PORT = 9559

showNaoImage(IP, PORT)
