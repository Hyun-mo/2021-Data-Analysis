import os
import pandas as pd

def mergeDust(filePath):
    print(filePath)
    data = pd.read_csv(filePath)
    data.fillna(0, inplace=True)
    out = {}

    for idx in range(len(data)):
        day = data.iloc[idx][0]
        dust =  data.iloc[idx][1]
        day = str(day)
        if day in out:
            out[day[0:6]][0] += dust
            out[day[0:6]][1] += 1
        else:
            out[day[0:6]] = [dust,1]

    for key, value in out.items():
        out[key] = round(value[0]/value[1], 2)
    
    return out
def init():
    Dir = './전처리/일별/대기오염도'
    fileList = os.listdir(Dir)
    out = {}
    for File in sorted(fileList):
        filePath = '/'.join([Dir, File])
        out.update(mergeDust(filePath))
        out_file = pd.DataFrame(list(out.items()), columns=['month', 'dust'])
        out_file.to_csv('./전처리/월별/dust.csv', index=False)

if __name__ == '__main__':
    init()