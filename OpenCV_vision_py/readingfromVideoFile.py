import cv2

# videoFile = 'videos/Armbot.mp4'
videoFile = 'videos/output.avi'
cap = cv2.VideoCapture(videoFile)
while not cap.isOpened():
    cap = cv2.VideoCapture(videoFile)
    cv2.waitKey(1000)
    print ("Wait for the header")

pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# cap.set(cv2.CAP_PROP_FPS, 50)

while True:
    flag, frame = cap.read()
    if flag:
        # The frame is ready and already captured
        cv2.imshow('video', frame)
        pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
        print (str(pos_frame)," frames")
    else:
        # The next frame is not ready, so we try to read it again
        cap.set(cv2.CAP_PROP_POS_FRAMES, pos_frame-1)
        print ("frame is not ready")
        # It is better to wait for a while for the next frame to be ready
        cv2.waitKey(1000)

    if cv2.waitKey(50) == 27:
        break
    if pos_frame == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        # If the number of captured frames is equal to the total number of frames,
        # we stop
        break