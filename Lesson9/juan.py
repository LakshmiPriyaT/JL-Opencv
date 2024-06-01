import cv2, numpy, os


datasets="Lesson9/datasets"
face="Lesson9/haarcascade_frontalface_default.xml"

print("Recognizer has started")

(images, labels, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(datasets):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(datasets, subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath + '/' + filename
            label = id
            images.append(cv2.imread(path, 0))
            labels.append(int(label))
        id += 1
(width, height) = (130, 100)
print(images)
print(labels)

(images, labels) = [numpy.array(lis) for lis in [images, labels]]

#face recogniser model

model = cv2.face.LBPHFaceRecognizer_create()

model.train(images,labels)

facedetect=cv2.CascadeClassifier(face)

webcam=cv2.VideoCapture(1)

width,height=130,100

count=1

while count>0:
    ret, frame=webcam.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=facedetect.detectMultiScale(grey,1.3,4)
    print(faces)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)
        person=grey[y:y+h,x:x+w]
        person_resize=cv2.resize(person,(width,height))
        prediction=model.predict(person_resize)
        print(prediction[1])



    cv2.imshow("webcam",frame)
    k=cv2.waitKey(10)
    if k==27:
        break