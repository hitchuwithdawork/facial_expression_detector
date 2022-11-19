import numpy as np
import cv2


# 영상 촬영 장치와 연결하기
capture = cv2.VideoCapture(0)

# 영상의 Width와 Height 크기조절
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)


while True:
    if cv2.waitKey(10) > 0: 
        break

    ret, frame = capture.read()
    # 영상을 한 프레임씩 읽어온다. 
    # ret:프레임 제대로 읽었는지 확인,정상이면 True이 출력된다.
    # frame: 읽은 프레임이 출력됨(이미지)

    cv2.putText(frame,'test',(0,25), cv2.FONT_HERSHEY_PLAIN,1,(255,255,255))
    #영상에 텍스트를 삽입한다.(넣을영상,넣을텍스트,텍스트위치(x,y),폰트명,폰트크기,색상(R,G,B))
    cv2.imshow("camera test", frame)
    #영상을 출력한다.
