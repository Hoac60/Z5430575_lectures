import os

import toolkit_config as cfg
import yf_example2

def qan_prc_to_csv(year):
    """download the specific stock price from Jan 1 to Dec 31 of the given year and save into a csv file
    Parameters
    ---------------
    year as a int
        an integer "year" which has 4 numbers
    """
    tic = "QAN.AX"
    start = f'{year}-01-01'
    end = f'{year}-12-31'
    pth = os.path.join(cfg.DATADIR,f'qan_prc_{year}.csv')
    df = yf_example2.yf_prc_to_csv(tic = tic, pth = pth, start = start, end = end)


if __name__ == "__main__":
    year = 2020
    qan_prc_to_csv(year)