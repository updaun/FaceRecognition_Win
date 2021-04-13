import os
def make(name):
    def createFolder(directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print ('Error: Creating directory. ' +  directory)
            
    createFolder('./dataset/'+name)

    print('='*70)
    print('-'*15 + '  체험자 폴더  [ ' + name + ' ]이(가) 생성되었습니다.' + '-'*15)
    print('='*70)
