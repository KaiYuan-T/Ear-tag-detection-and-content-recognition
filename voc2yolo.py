import xml.etree.ElementTree as ET
import shutil
import os

seal_VOC = "/home/tanky/dataset/seal_VOC/"
train_file = "/home/tanky/dataset/seal_VOC/train.txt"
val_file = "/home/tanky/dataset/seal_VOC/valid.txt"

def convert(xmin, ymin, xmax, ymax, width, height):
    x_center = (xmin + xmax) / 2.0
    y_center = (ymin + ymax) / 2.0
    w = (xmax - xmin) / width
    h = (ymax - ymin) / height
    x = x_center / width
    y = y_center / height
    
    return x, y, w, h

    """
dataset/
├── train/
│   ├── images/
│   └── labels/
└── val/
    ├── images/
    └── labels/
    """
def make_dir(root, mode):
    os.makedirs(root+mode+"/images/", exist_ok=True)
    os.makedirs(root+mode+"/labels/", exist_ok=True)

def voc2yolo(location, root, mode):
    
    make_dir(root, mode)
    
    with open(location, 'r', encoding='utf-8') as file:
        lines = file.readlines() # read all lines into list
        for line in lines:
            content = line.strip()
            image_file = content.split()[0] # this is image file location
            label_file = content.split()[1] # this is label file location
            image_name = image_file.split("/")[1]
            file_name = image_name.split(".")[0]
            
            # deal with labels
            
            with open(root+mode+"/labels/"+file_name+'.txt', 'w', encoding='utf-8') as current_txt:
                tree = ET.parse(root+label_file) # read xml file
                file_root = tree.getroot()
                size = file_root.find('size') # get size and bbox
                width = size.find('width').text
                height = size.find('height').text
                width = float(width)
                height = float(height)

                for obj in file_root.findall('object'):
                    current_txt.write("0 ") # since only one category, don't need to find the class number
                    bndbox = obj.find('bndbox')
                    xmin = float(bndbox.find('xmin').text)
                    ymin = float(bndbox.find('ymin').text)
                    xmax = float(bndbox.find('xmax').text)
                    ymax = float(bndbox.find('ymax').text)
                    labels = convert(xmin, ymin, xmax, ymax, width, height)
                    for number in labels:
                        current_txt.write(str(number))
                        current_txt.write(" ")
                    current_txt.write("\n")
            current_txt.close()
            
            #deal with images
            src = root+image_file
            dst_dir = root+mode+"/images/"
            dst = os.path.join(dst_dir, image_name)
            shutil.copy(src, dst)
    file.close()
    print("FINISH")
    
voc2yolo(val_file, seal_VOC,"val")
            
                

