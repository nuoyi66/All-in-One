def getName(srcStr):
    infoline=srcStr.split('\n')
    for info in infoline:
        if info != '':
            info = info.split('the name is')[1].split(',')[0].strip()
        print(info)
    return
srcStr = '''
A girl come in,the name is Jack,level 955;
A old lady come in, the name is Mary,level 94454;
A pretty boy come in, the name is Patrick,level 194;
'''
getName(srcStr)