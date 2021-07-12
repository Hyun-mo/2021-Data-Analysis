import os
import pandas as pd
import re

def mergeDust(filePath):
    print(filePath)
    extension = os.path.splitext(filePath)[1]
    if extension == '.csv':
        data = pd.read_csv(filePath)
    else :
        data = pd.read_excel(filePath)

    data.fillna(0, inplace=True)
    out = {}
    for idx in range(len(data)):
        day = data.iloc[idx][0]
        dust =  data.iloc[idx][6]
        if day in out:
            out[day][0] += dust
            out[day][1] += 1
        else:
            out[day] = [dust,1]

    for key, value in out.items():
        out[key] = round(value[0]/value[1], 2)
    
    return out
def init():
    Dir = './대기오염도'
    fileList = os.listdir(Dir)
    for File in sorted(fileList):
        out = {}
        filePath = '/'.join([Dir, File])
        out.update(mergeDust(filePath))
        year = re.sub('[^0-9]', '',File).strip()
        out_file = pd.DataFrame(list(out.items()), columns=['day', 'dust'])
        out_file.to_csv('./전처리/일별/대기오염도/%s.csv' %year, index=False)

if __name__ == '__main__':
    print('main')
    init()