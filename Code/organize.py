import os
import shutil
import random

folder = "Data"
dest_folder = "Data_org/Complete"


def organize_data(folder, dest_folder):
    for image in os.listdir(folder):
        class_folder = image[-7::-1]
        class_folder = class_folder[::-1]
        # print(image)
        if class_folder not in os.listdir(dest_folder):
            folder_name = os.path.join(dest_folder, class_folder)
            os.mkdir(folder_name)
            print('Created folder for class {}'.format(class_folder))
        shutil.copy(folder + '\\' + image, dest_folder + '\\' + class_folder + '\\' + image)


def split_data(data_folder, train_folder, test_folder):
    a, b = random.sample(range(1, 9), 2)
    for folder in os.listdir(data_folder):
        if folder not in os.listdir(train_folder):
            folder_name = os.path.join(train_folder, folder)
            os.mkdir(folder_name)
            folder_name = os.path.join(test_folder, folder)
            os.mkdir(folder_name)
        for image in os.listdir(os.path.join(data_folder, folder)):
            # print(image)
            if int(image[-5]) == a or int(image[-5]) == b:
                shutil.copy(data_folder + '\\' + folder + '\\' + image, test_folder + '\\' + folder + '\\' + image)
            else:
                shutil.copy(data_folder + '\\' + folder + '\\' + image, train_folder + '\\' + folder + '\\' + image)


# organize_data(folder, dest_folder)

data_folder = 'Data_org/Complete'
train_folder = 'Data_org/Train'
test_folder = 'Data_org/Test'

# split_data(data_folder, train_folder, test_folder)