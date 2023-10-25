import cv2
# Esta línea de código inicializa el objeto `CascadeClassifier` `face_cascade` con el archivo XML
# `haarcascade_frontalface_default.xml`. Este archivo XML contiene el modelo previamente entrenado
# para detectar caras frontales utilizando el algoritmo de clasificadores en cascada basado en
# características de Haar.
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the webcam
# `video = cv2.VideoCapture(0)` inicializa la cámara web para capturar fotogramas de vídeo. El
# argumento `0` especifica el índice de la cámara que se utilizará. En este caso, "0" se refiere a la
# cámara predeterminada, que suele ser la cámara web integrada en la mayoría de los sistemas.
video = cv2.VideoCapture(0)  # Use index 0 for the default camera (usually the built-in webcam)

while True:
    # Read a frame from the webcam
    ret, frame = video.read()
    if not ret:
        break

    # Increase the contrast and brightness of the frame (adjust these values as needed)
    alpha = 1.5  # Contrast control
    beta = 50    # Brightness control
    frame = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame with face detection
    cv2.imshow('Face Detection', frame)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the OpenCV window
video.release()
cv2.destroyAllWindows()
