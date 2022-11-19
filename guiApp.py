# Importing GUI modules
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image


from keras.models import load_model
from keras.preprocessing.image import img_to_array
import cv2
import numpy as np


classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


model = load_model('trained_model.h5')


classes = ['Angry', 'Disgust','Fear','Happy','Neutral','Sad','Surprise']


def classifyImages(file_path):
  image = cv2.imread(file_path)
  grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  faces = classifier.detectMultiScale(grayImage, 1.2, 4)
 
  for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (231, 76, 60), 2)
    gray = grayImage[y:y+h, x:x+w]
    gray = cv2.resize(gray, (48, 48), interpolation=cv2.INTER_AREA)

    finalImage = gray.astype('float')/255.0
    finalImage = img_to_array(finalImage)
    finalImage = np.expand_dims(finalImage, axis=0)

    preds = model.predict(finalImage)[0]
    label = classes[preds.argmax()]
    label_position = (x, y)
    cv2.putText(image, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 2, (52, 152, 219), 2)
  

  im = Image.fromarray(image)
  imgtk = ImageTk.PhotoImage(image=im) 
  

  displayLabel.config(image=imgtk)
  displayLabel.image = imgtk

def uploadImage():
  fileName = filedialog.askopenfilename()
  uploadedImage = Image.open(fileName)
  uploadedImage.thumbnail((380, 500))
  imageFile = ImageTk.PhotoImage(uploadedImage)
  displayLabel.config(image=imageFile)
  displayLabel.image = imageFile
  # Using the image classification function
  classifyImages(fileName)


def closeApp():
  exit()


root = tk.Tk()

appFrame = tk.Frame(root)
appFrame.pack(side=tk.BOTTOM, padx=15, pady=15)


displayLabel = tk.Label(root)
displayLabel.pack(padx=15, pady=15)

uploadButton = tk.Button(appFrame, text="Upload an Image", command=uploadImage)
uploadButton.pack(side=tk.LEFT)

closeButton = tk.Button(appFrame, text="Close App", command=closeApp)
closeButton.pack(side=tk.LEFT, padx=10)

root.title("Facial Expression Image Classification")
root.geometry("400x580")
root.mainloop()
