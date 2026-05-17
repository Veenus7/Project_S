import cv2 as cv
import time as time
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
def cam_setup():
    cap=cv.VideoCapture(0)
    cap.set(cv.CAP_PROP_FRAME_WIDTH,640)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT,480)
    return cap
def read_frame(cap):
            ret,frame=cap.read()
            if not ret:
                  return None
            return cv.flip(frame,1)
def cam_release(cap):
    cap.release()
    cv.destroyAllWindows()
def fps_setup():
      previous=0
      return previous
def fps_counter(previous):
    
    current=time.time()
    diff=current-previous
    previous=current
    if diff>0:
          fps=1.0/diff
    return previous,int(fps)
def fps_draw(fps,frame):
      cv.putText(frame,f"fps : {fps}",(5,11),cv.FONT_HERSHEY_PLAIN,1,(255,255,255),1,cv.LINE_AA)
      return frame

def ui(frame):
      w,h,_=frame.shape
      cv.circle(frame,(w//2,h//2),6,(34,55,32),-1)
      cv.rectangle(frame,(0,0),(80,15),(0,255,0),-1)
      cv.putText(frame,"Gesture",(500,50),cv.FONT_HERSHEY_COMPLEX,2,(255,255,255),3,cv.LINE_AA)
      return frame

cap=cam_setup()
p=fps_setup()
while(True):
    frame=read_frame(cap)
    p,fps=fps_counter(p)
    frame=ui(frame)
    frame=fps_draw(fps,frame)
    cv.imshow("img",frame)
    
    
    if cv.waitKey(1)==ord("q"):
          break
cam_release(cap)
