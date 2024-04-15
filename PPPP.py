import os
import datetime as dt
import pandas as pd
import toolkit_config as cfg





CSVLOC = os.path.join(cfg.DATADIR, 'qan_prc_2020.csv')

dt_now = dt.datetime.now()
print(dt_now)
print(type(dt_now))

A= 'Date is day/month/year format is: {}/{}/{}'. format(dt_now.day, dt_now.month,dt_now.year)
print(A)

print(repr(dt_now))

dt0=dt.datetime(year=2024, month=12, day=31)
dt1=dt.datetime(year=2025, month=1, day=1)

delta = dt1-dt0
print(repr(delta))
print(delta)

New_delta= dt.datetime(year=2024, month=12, day=31) - dt.datetime(year=2025, month=1, day=1)
print(New_delta)

prc= pd.read_csv(CSVLOC, index_col='Date')
prc.info()
prc.sort_index(inplace=True)

print(prc.loc['2020-01-02'])
print(prc.loc['2020-01-02':'2020-01-05'])

returns = prc.loc[:,'Close'].pct_change()
print(returns)





def time_it(func, parms):
    """ Returns a string representing the time it took to execute a function.

    Parameters
    ----------
    func : any function

    parms : dict
        A dictionary with the parameters that will be passed to the function.
        For instance, if `parms` is {'parm1': 1}, then the function call will be
        `func(parm1=1)`

    Returns
    -------
    str
        A string with the time it took to execute `func` with the parameters `parms`.
        This string should have the following format:

        "It took <n days> days, <n hours> hours, <n mins> mins, and <n secs> secs to execute the function"

        where:
            <n days>, <n hours>, <n mins>, and <n secs> represent the number of days, hours, minutes,
            and seconds it took to run the function.

    Example
    -------

    Suppose there is a function called `my_func` that takes a single parameter called `parm1`.

        >> res = time_it(my_func, {'parm1': 3})
        >> print(res)
        It took 0 days, 0 hours, 1 mins, and 2 secs to execute the function

    In the example above, we are assuming it took 1 minute and 2 seconds to execute the function
    `my_func(parm1=3)`.

    Note
    ----
    - You should not use the `time` module inside this function
      (meaning, do not use `import time` inside this function)

    - You can use the function _mk_msg to produce a string with the
      format specified in the docstring (given the number of days, hours,
      mins, and secs)

    """
    # You can use this function if you want
    def _mk_msg(days, hours, mins, secs):
        """ This function produces a string with the format specified in the docstring
        of the main function.
        """
        msg = f"It took {days:.0f} days, {hours:.0f} hours, {mins:.0f} mins, and {secs} secs to execute the function"
        return msg

    before_time = dt.datetime.now()
    func(**parms)
    after_time = dt.datetime.now()
    elapsed = after_time - before_time

    days = elapsed.days
    total_seconds = elapsed.total_seconds() - days*24*3600

    mins, secs =divmod(total_seconds, 60)
    hours, mins = divmod(mins,60)

    return _mk_msg(days,hours,mins,secs)

def _test_time_it():
    """ This function uses the time.sleep to test the function time_it.

    the output of this function should be:

        Note: It will take about 1 min to execute this test function...
        It took 0 days, 0 hours, 1 mins, and 4.0 secs to execute the function

    NOTE
    ----
    - The number of secs in the output may be slignly different if the ED server is busy.
      If this happens, just run this test function again.

    """
    import time
    print("Note: It will take about 1 mins to execute this test function...")
    def _my_func(secs):
        time.sleep(secs)
    res = time_it(_my_func, {'secs': 64})
    print(res)



if __name__ == "__main__":
    pass
    _test_time_it()





import pandas as pd

from webinars import lec_utils as utils

utils.pp_cfg.sep = True
utils.pp_cfg.df_info = False


def mk_rec_df0(show: bool = False):

    cnts_rec_csv = '''
    date                , firm           , action
    2012-02-16 07:42:00 , JP Morgan      , main
    2020-09-23 08:58:55 , Deutsche Bank  , main
    2020-09-23 09:01:26 , Deutsche Bank  , main
    2020-09-23 09:11:01 , Wunderlich     , down
    2020-09-23 11:15:12 , Deutsche bank  , up
    2020-11-18 11:07:44 , Morgan Stanley , up
    2020-12-09 15:34:34 , JP Morgan      , main
    '''
    df = utils.csv_to_df(cnts_rec_csv, index_col='date', parse_dates=['date'])

    # Upper case version of 'firm' column
    df.loc[:, 'firm'] = df.loc[:, 'firm'].str.upper()

    # Create a string with the date part of the DatetimeIndex
    df.loc[:, 'event_date'] = df.index.strftime('%Y-%m-%d')

    if show is True:
        utils.pprint(df, "Example DF:")
    return df


df = mk_rec_df0(show=True)

df ["THE_action"] = df["action"].astype("category")

df["THE_action"]

new_category = ["down_sign_should_sell_or_short","remains_same_price","up_sign_should_buy_or_Long"]
df["THE_action"]=df["THE_action"].cat.rename_categories(new_category)

print(df)

df.sort_values(by='THE_action')

df.groupby("THE_action", observed=False).size()