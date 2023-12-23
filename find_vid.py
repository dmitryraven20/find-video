import cv2

cap = cv2.VideoCapture("output.avi")
img = cv2.imread("img.png")

counter = 0

                
while cap.isOpened():
    _, frame = cap.read()
    
    img = cv2.resize(img, (640, 480), interpolation=cv2.INTER_AREA)

    grayvid = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, threshvid = cv2.threshold(grayvid,0,255,cv2.THRESH_BINARY)
    _, threshimg = cv2.threshold(grayimg,0,255,cv2.THRESH_BINARY)

    compare = cv2.matchTemplate(threshvid,threshimg,cv2.TM_CCOEFF)
    if compare > 0.9:
        counter += 1
        print("Совпадение есть")

cap.release
print(f"Итого {counter}")
