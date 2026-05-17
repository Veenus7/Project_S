import cv2 as cv
import time as time
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
      cv.putText(frame,f"fps : {fps}",(5,10),cv.FONT_HERSHEY_PLAIN,1,(255,255,255),1,cv.LINE_AA)
      return frame
cap=cam_setup()
p=fps_setup()
while(True):
    frame=read_frame(cap)
    p,fps=fps_counter(p)
    frame=fps_draw(fps,frame)
    cv.imshow("img",frame)
    
    
    if cv.waitKey(1)==ord("q"):
          break
cam_release(cap)
