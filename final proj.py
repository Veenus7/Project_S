import cv2 as cv
import time as time
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
latest_result = None

def cam_setup():
    cap=cv.VideoCapture(0)
    cap.set(cv.CAP_PROP_FRAME_WIDTH,640)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT,480)
    return cap
def read_frame(cap):
            ret,frame=cap.read()
            if not ret:
                  return None
            frame=cv.flip(frame,1)
            return frame
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

def save_result(result, output_image, timestamp_ms):

    global latest_result
    latest_result = result

def mediapipe():
      base_options=python.BaseOptions(model_asset_path="E:\\VCODES\\Project_S\\model\\hand_landmarker.task")
      options = vision.HandLandmarkerOptions(
                  base_options=base_options,
                  running_mode=vision.RunningMode.LIVE_STREAM,
                  num_hands=1,
                  result_callback=save_result
                   )
      detector=vision.HandLandmarker.create_from_options(options)
      return detector

def detection(detector,frame):
      frame=mp_process(frame)
      timestamp_ms = int(time.time() * 1000)

      detector.detect_async(frame, timestamp_ms)    
      return latest_result

def result_process(result):
      if not result:
            return None,None
      landmarks=result.hand_landmarks
      handedness=result.handedness
      return landmarks,handedness


def mp_process(frame):
      rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
      rgb=cv.resize(rgb,(640,480))
      img =  mp.Image(image_format=mp.ImageFormat.SRGB,data=rgb)
      return img
cap=cam_setup()
p=fps_setup()
detector=mediapipe()
while(True):
    frame=read_frame(cap)
    print(type(frame))
    result=detection(detector,frame)
    landmarks,handedness=result_process(result)
    print(type(landmarks))
    print(landmarks)
    print(type(handedness))
    print(handedness)
#     input=mp_process(frame)
#     frame=ui(frame)
    p,fps=fps_counter(p)
    frame=fps_draw(fps,frame)
    frame=cv.resize(frame,(640,480))
    cv.imshow("img",frame)
    
    
    if cv.waitKey(1)==ord("q"):
          break
cam_release(cap)
