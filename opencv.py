import cv2

print("cc")
cap=cv2.VideoCapture(-1)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
# cap.set(cv2.CAP_PROP_FRAME_WEIGHT,480)
# cap.set(cv2.CAP_PROP_FPS,20)

while(True):
    ret, frame=cap.read()
    if(ret):
        print("a")
        cv2.imshow('frame',frame)
        if(cv2.waitKey(1)==ord('q')):
            break
        
cap.release()
cv2.destroyAllWindows()