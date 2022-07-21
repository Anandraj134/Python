import cv2 
cap = cv2.VideoCapture(0);
print("Choose your image preview from below options")
print("1. Color")
print("2. Grayscale")
choose = input("Enter you choice :- ")
if choose == '1':
    while(True):
            ret, frame = cap.read()
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
if choose == '2':
    while(True):
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
else:
    print("Please,Choose proper option.")
cap.release()
cv2.destroyAllWindows()