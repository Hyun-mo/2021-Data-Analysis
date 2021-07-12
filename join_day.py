import pandas as pd

from pandas.core.reshape.merge import merge

def init():
    merged_table = pd.DataFrame()
    for year in range(2016,2021):
        trafic_data = pd.read_csv('./전처리/일별/교통량/%s.csv' %year)
        dust_data = pd.read_csv('./전처리/일별/대기오염도/%s.csv' %year)
        trafic_data = trafic_data.astype({'trafic':float})
        trafic_data['trafic'] = trafic_data['trafic'].apply(lambda x : x/100000)
        joined_table = pd.merge(dust_data, trafic_data, on='day')
        merged_table = pd.concat([merged_table, joined_table])

    merged_table.to_csv('./전처리/일별/merged.csv',index=False)

if __name__ == '__main__':
    init()