import pandas as pd

def init():
    filePath = './에너지 사용량/에너지사용량데이터 통계 요약정보.xlsx'
    data = pd.read_excel(filePath)
    out = pd.DataFrame()
    for idx in range(len(data)):
        line = data.iloc[idx]
        YM = '%s%02d' %(line[0], line[1])
        if line['회원타입'] == '개인':
            if YM in out:
                out[YM][0] += line[4]/line['건수']
                out[YM][1] += line[5]/line['건수']
            else:
                out[YM] = [line[4]/line['건수'], line[5]/line['건수']]
            
    out_file = pd.DataFrame(out).transpose()
    out_file.columns = [ 'elec', 'gas']
    out_file = out_file.rename_axis('month').reset_index()
    out_file.to_csv('./전처리/월별/energy_personal.csv', index=False)

if __name__ == '__main__':
    print('main')
    init()
