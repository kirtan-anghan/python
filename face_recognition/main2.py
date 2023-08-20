import os
import sys
import face_recognition
import cv2

class FaceRecognition:
    def __init__(self, known_faces_path):
        self.known_face_encodings, self.known_face_names = self.encode_faces(known_faces_path)

    def encode_faces(self, known_faces_path):
        known_face_encodings = []
        known_face_names = []

        for image_name in os.listdir(known_faces_path):
            if image_name.endswith(".DS_Store"):
                continue

            image_path = os.path.join(known_faces_path, image_name)
            face_image = face_recognition.load_image_file(image_path)
            face_encoding = face_recognition.face_encodings(face_image)[0]

            known_face_encodings.append(face_encoding)
            known_face_names.append(image_name[:-4])  # Remove ".jpg" extension

        return known_face_encodings, known_face_names

    def run_recognition(self):
        video_capture = cv2.VideoCapture(0)

        if not video_capture.isOpened():
            sys.exit('Video source not found...')

        while True:
            ret, frame = video_capture.read()

            # Find all the faces in the current frame of video
            face_locations = face_recognition.face_locations(frame)
            face_encodings = face_recognition.face_encodings(frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                name = "Unknown"

                if True in matches:
                    matched_index = matches.index(True)
                    name = self.known_face_names[matched_index]

                face_names.append(name)

            # Display the results
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1)

            # Display the resulting image
            cv2.imshow('Face Recognition', frame)

            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) == ord('q'):
                break

        # Release handle to the webcam
        video_capture.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    known_faces_path = "/Users/kirtan/Desktop/code/python/face_recognition/faces"  # Replace with the actual path
    fr = FaceRecognition(known_faces_path)
    fr.run_recognition()
