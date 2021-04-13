import cv2
#from name import inputname
def shot(path):
    #print(inputname())
    
    #name = 'daun' #replace with your name
    #name = inputname()

    cam = cv2.VideoCapture(0)

    cv2.namedWindow("press SPACE to take a photo for training", cv2.WINDOW_NORMAL)
    cv2.moveWindow("press SPACE to take a photo for training", 500, 0)
    cv2.resizeWindow("press SPACE to take a photo for training", 500, 500)

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("press SPACE to take a photo for training", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            #print("Escape hit, closing...")
            #print("----- 사진 촬영을 종료합니다. -----")
            print('-'*15 + '  체험자 [ ' + path + ' ] 의 사진 촬영을 종료합니다. ' + '-'*15)
            print('='*70)

            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "dataset/"+ path +"/image_{}.jpg".format(img_counter)
            #img_name = "dataset/image_{}.jpg".format(img_counter)
            cv2.imwrite(img_name, frame)
            #print("{} written!".format(img_name))
            #print("{} 사진이 촬영 되었습니다.".format(img_name))
            print('-'*15 + '  체험자 [ ' + path + ' ] 의 {}번째 사진을 촬영했습니다.'.format(img_counter+1) + '-'*15 )
            print('='*70)
            img_counter += 1

    cam.release()

    cv2.destroyAllWindows()
    
