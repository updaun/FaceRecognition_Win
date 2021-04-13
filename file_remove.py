import os
import shutil


def remove():
    dir_path = './dataset/'
    print('-'*70)
    print('[삭제한 폴더 및 사진]')
    file_list = os.listdir(dir_path)
    print(*file_list)
    for file in file_list:
        file_path = os.path.join(dir_path, file)
        if os.path.isdir(file_path):
            dir_path2 = file_path
            print(dir_path2)
            shutil.rmtree(dir_path2)
    print('='*70)
    file_list = os.listdir(dir_path)
    print(*file_list)

    #print('Remove Success!!!')
    print('-'*15 + '  체험자 이미지를 성공적으로 삭제 했습니다. ' + '-'*15)                
    
    print('='*70)

#os.rmdir('/home/pi/Face_Recognition/dataset/daun')