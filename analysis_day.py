import pandas as pd
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm

def day():
    filePath = './전처리/일별/merged.csv'
    data = pd.read_csv(filePath)
    print(data[['dust', 'trafic']].corr())

def month():
    filePath = './전처리/월별/merged.csv'
    data = pd.read_csv(filePath)
    print(data.corr()['dust'])
    reg = ols('dust~elec+gas+operating_rate', data = data).fit()
    print(reg.summary())
    fig=sm.graphics.plot_partregress_grid(reg)
    fig.tight_layout(pad=1)

if __name__ == '__main__':
    day()
    month()