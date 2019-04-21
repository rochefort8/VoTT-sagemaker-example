import os
from PIL import Image, ImageFilter
 
def main():
    data_dir_path = './out/'
    data_dir_path_in = './in/'
    file_list = os.listdir('./in/')
 
    count = 1
    for file_name in file_list:
        root, ext = os.path.splitext(file_name)
        if ext == '.png' or '.jpeg' or '.jpg':
            img = Image.open(data_dir_path_in + '/' + file_name) 
            tmp = img.transpose(Image.FLIP_LEFT_RIGHT)
            tmp.save(data_dir_path + '/' + '{0:04d}'.format(count) +'.jpg')
            count+=1
            tmp = img.transpose(Image.FLIP_TOP_BOTTOM)
            tmp.save(data_dir_path + '/' + '{0:04d}'.format(count) +'.jpg')
            count+=1
            tmp = img.transpose(Image.ROTATE_90)
            tmp.save(data_dir_path + '/' + '{0:04d}'.format(count) +'.jpg')
            count+=1
            tmp = img.transpose(Image.ROTATE_180)
            tmp.save(data_dir_path + '/' + '{0:04d}'.format(count) +'.jpg')
            count+=1
            tmp = img.transpose(Image.ROTATE_270)
            tmp.save(data_dir_path + '/' + '{0:04d}'.format(count) +'.jpg')
            count+=1
            tmp = img.rotate(15)
            tmp.save(data_dir_path + '/' + '{0:04d}'.format(count) +'.jpg')
            count+=1
            tmp = img.rotate(75)
            tmp.save(data_dir_path + '/' + '{0:04d}'.format(count) +'.jpg')
            count+=1
            tmp = img.rotate(135)
            tmp.save(data_dir_path + '/' + '{0:04d}'.format(count) +'.jpg')
            count+=1         
            tmp = img.rotate(195)
            tmp.save(data_dir_path + '/' + '{0:04d}'.format(count) +'.jpg')
            count+=1
            tmp = img.rotate(255)
            tmp.save(data_dir_path + '/' + '{0:04d}'.format(count) +'.jpg')
            count+=1
 
if __name__ == '__main__':
    main()