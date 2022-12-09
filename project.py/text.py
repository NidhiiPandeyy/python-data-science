import cv2

video = cv2.VideoCapture(0)
a = 0
img_counter = 0
videoNpArr = cv2.imread("test-image.jpg")

while True:

    a = a + 1
    check, frame = video.read()

    print(check)
    print(frame)

    cv2.putText(frame, "Hello World!!!", (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))

    cv2.imshow("Main frame thing", frame)

    # cv2.waitKey(0)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break
    elif key == ord('i'):
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
    print(a)

video.release()
cv2.destroyAllWindows()