import pandas as pd

def init():
    dust_data = pd.read_csv('./전처리/월별/dust.csv')
    energy_data = pd.read_csv('./전처리/월별/energy.csv')
    op_data = pd.read_csv('./전처리/월별/operating_rate.csv')
    joined_table = pd.merge(dust_data, energy_data, on='month')
    joined_table = pd.merge(joined_table, op_data, on='month')
    joined_table.to_csv('./전처리/월별/merged.csv',index=False)
    print('com')
    print(joined_table['gas'].mean())
if __name__ == '__main__':
    init()