import os
import pandas as pd
import numpy

def mergeTrafic(filePath):
    print(filePath)
    data = pd.read_excel(filePath)
    data.fillna(0, inplace=True)
    out = {}
    for idx in range(len(data)):
        trafic = 0
        day = data.iloc[idx][0]
        for trf in data.iloc[idx][6:31]:
            if type(trf) != numpy.float64:
                continue
            trafic += int(trf)
        if day in out:
            out[day] += int(trafic)
        else :
            out[day] = int(trafic)
    return out

def init():
    Dir = './교통량'
    dirList = os.listdir(Dir)
    for year in sorted(dirList):
        print(year)
        year_dir = '/'.join([Dir, year])
        fileList = os.listdir(year_dir)
        out = {}
        for month_file in sorted(fileList):
            filePath = '/'.join([year_dir, month_file])
            out.update(mergeTrafic(filePath))
            print(out)
        out_file = pd.DataFrame(list(out.items()), columns=['day', 'trafic'])
        out_file.to_csv('./전처리/일별/교통량/%s.csv' %year, index=False)

if __name__ == '__main__':
    init()