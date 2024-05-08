import cv2
import numpy as np


def video_to_stream(video_file):
    cap = cv2.VideoCapture(video_file)

    if not cap.isOpened():
        print("Error: Could not open video file")
        return

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            print("End of video")
            break


        cv2.imshow('Frame', frame)

    cap.release()
    cv2.destroyAllWindows()


# Example usage
video_to_stream('data/1.mp4')
