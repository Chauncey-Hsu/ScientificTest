import os
path = 'E:\\WeatherData\\typhoon\\'
files = os.listdir(path)
for i, file in enumerate(files):

    OldFileName = os.path.join(path, file)
    # print(OldFileName)

    NewFileName = OldFileName[30:36] + '.txt'
    # print(NewFileName)
    NewFileName = path + NewFileName
    print(NewFileName)
    os.rename(OldFileName, NewFileName)
