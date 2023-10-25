import cv2
import numpy as np

# Inicializar la captura de video (0 para la cámara predeterminada)
cap = cv2.VideoCapture(0)

while True:
    # Capturar un fotograma de la cámara
    ret, frame = cap.read()

    # Convertir la imagen a escala de grises para mejorar el rendimiento
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Aplicar un aumento de brillo para mejorar la visión nocturna (puedes ajustar el valor según sea necesario)
    gray = cv2.add(gray, 50)

    # Aplicar un aumento de contraste para mejorar la visibilidad (puedes ajustar el valor según sea necesario)
    gray = cv2.convertScaleAbs(gray, alpha=1.2, beta=0)

    # Realizar operaciones de detección o reconocimiento aquí usando la imagen en escala de grises (gray)

    # Mostrar la imagen en una ventana
    cv2.imshow('Visión Nocturna', gray)

    # Romper el bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()
