# Custom - Object - Detectiom

## Dataset
For the custom images, i have used rubic cube as my custom object. The images are present [here](https://github.com/jaisanant0/custom-object-YOLO/tree/master/image).

## Traing-Test split 
Use this [script](https://github.com/jaisanant0/custom-object-YOLO/blob/master/split-data.py) to split and make train.txt and test.txt.
I have put random 10% of data for test.

NOTE : train.txt and test.txt is already provided for my dataset.

## Annotation
I have used [labelImg](https://github.com/tzutalin/labelImg) to create the desired bounding box, it saves the bounding boxes as xml file.
But YOLO model has the following format for bounding boxes 
```
<object class> <x-center> <y-center> <width> <height>
```

To convert the xml files into desired .txt file, one can use [this](https://github.com/Isabek/XmlToTxt).

## Training 
I have used forked version of [darknet](https://github.com/AlexeyAB/darknet) for the training purpose.

1. Download the [pre-trained model](https://pjreddie.com/media/files/darknet53.conv.74).
2. Create .data file as :
 ```
    classes = 1
    train  = <path to train.txt> 
    valid  = <path to test.txt>
    names = <path to object.names>
    backup = <path to save weights>
```
Here,
Classes : The number of classes we wan to detect(1 in my case).
names  : names of the class saved as <objects>.names

3. Edit the YOLO configuration file as per your hardware capability.

        a. [net]
           # Testing
           #batch=1
           #subdivisions=1
           #Training
           batch=64  (number of images to be used per batch)
           subdivisions=8 (used to create mini batch : 64//8 in my case)
        
        b. learning_rate=0.001
           burn_in=150 (to control training speed for 150 batches in my case)
           max_batches = 30000 ( maximun number batched to feed in network)
           policy=steps (to control how the leaning rate will decrease)
           steps=3500,16500 (at what steps the learning rate will decrease)
           scales=.1,.1 (with what rate the learning rate will decrease on mentioned steps).
         
        c. Data augmentation :
           angle=0
           saturation = 1.5
           exposure = 1.5
           hue=.1
        
        
4. Use the following command to train the netwrok.
  ```
  ./darknet detector train rubic-cube.data  yolov3-tiny.cfg ./darknet53.conv.74 > train_log.txt 
  ```
  - To monitor loss you can use 
   ```
   grep "avg" train_log.tx
   ```
  
  - To [stop the training](https://github.com/AlexeyAB/darknet#when-should-i-stop-training).
     
# Testing
 To test the model use :
 ```
 ./darknet detector test <rubic-cube.data> <yolov3-tiniy-test.cfg> ./<yolov3 weights>
 ```
 
 NOTE :
  I ahve provided my trained [weights](https://github.com/jaisanant0/custom-object-YOLO/tree/master/weights)
  
  ## Results
  
  ![result1](https://github.com/jaisanant0/custom-object-YOLO/blob/master/results/107.jpg).
  
  You can find more in results directory.
