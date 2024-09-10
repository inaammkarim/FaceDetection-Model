import cv2
import face_recognition

# Load known face encodings and names
known_face_encodings = []
known_face_names = []

# Load known faces and their names here
known_person1_image = face_recognition.load_image_file(r"C:\Users\Meherban karim\Desktop\ann\img\inam (2).jpg")
known_person2_image = face_recognition.load_image_file(r"C:\Users\Meherban karim\Desktop\ann\img\imsha.jpg")
known_person3_image = face_recognition.load_image_file(r"C:\Users\Meherban karim\Desktop\ann\img\sonum.jpg")
known_person4_image = face_recognition.load_image_file(r"C:\Users\Meherban karim\Desktop\ann\img\danii.jpg")
known_person5_image = face_recognition.load_image_file(r"C:\Users\Meherban karim\Desktop\ann\img\junaid.jpg")
known_person6_image = face_recognition.load_image_file(r"C:\Users\Meherban karim\Desktop\ann\img\shakabhai.jpg")
known_person7_image = face_recognition.load_image_file(r"C:\Users\Meherban karim\Desktop\ann\img\jiya.jpg")

known_person1_encoding = face_recognition.face_encodings(known_person1_image)[0]
known_person2_encoding = face_recognition.face_encodings(known_person2_image)[0]
known_person3_encoding = face_recognition.face_encodings(known_person3_image)[0]
known_person4_encoding = face_recognition.face_encodings(known_person4_image)[0]
known_person5_encoding = face_recognition.face_encodings(known_person5_image)[0]
known_person6_encoding = face_recognition.face_encodings(known_person6_image)[0]
known_person7_encoding = face_recognition.face_encodings(known_person7_image)[0]

known_face_encodings.append(known_person1_encoding)
known_face_encodings.append(known_person2_encoding)
known_face_encodings.append(known_person3_encoding)
known_face_encodings.append(known_person4_encoding)
known_face_encodings.append(known_person5_encoding)
known_face_encodings.append(known_person6_encoding)
known_face_encodings.append(known_person7_encoding)

known_face_names.append("Inaamm barcha")
known_face_names.append("Imsha")
known_face_names.append("sonum bajwa")
known_face_names.append("Dani bhai")
known_face_names.append("Junaid JD")
known_face_names.append("Shaka bhai")
known_face_names.append("Jiya")


# Initialize the webcam
video_capture = cv2.VideoCapture(0)

# Check if the webcam is opened successfully
if not video_capture.isOpened():
    print("Error: Failed to open webcam.")
    exit()

while True:
    # Capture frame by frame
    ret, frame = video_capture.read()

    # Check if frame is captured successfully
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Find all face recognition in current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Debugging: Print face locations and encodings
    print("Face Locations:", face_locations)
    print("Face Encodings:", face_encodings)

    # Loop through each face found in the frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Check if face matches any known face
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "User Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw a box and label the name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow("Video", frame)

    # Break the loop when 'n' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('n'):
        break

# Release the webcam and close the OpenCV window
video_capture.release()
cv2.destroyAllWindows()
