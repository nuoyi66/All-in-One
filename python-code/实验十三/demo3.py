try:
    with open("/root/file1.txt",mode='r') as f1:
         print('file opend!')
         f1.close()
except:
    print('file in not exist')
print('DONE!')