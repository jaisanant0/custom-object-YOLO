import glob, os


dataset_path = '/home/JAIS/Desktop/deep_learning/object_detect_yolo/custom-object/image'


percentage_test = 10

train_file = open('train.txt', 'a')  
test_file = open('test.txt', 'a')

c = 1  
i = 100 // percentage_test 

for file in glob.glob(dataset_path + '/' + "*.png"):

    t, e = os.path.splitext(os.path.basename(file))

    if c == i+1 :
        c = 1
        test_file.write(dataset_path + "/" + t + '.png' + "\n")
    else :
        train_file.write(dataset_path + "/" + t + '.png' + "\n")
        c = c + 1

