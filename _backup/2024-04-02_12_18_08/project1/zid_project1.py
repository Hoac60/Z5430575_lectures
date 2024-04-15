""" zid_project1.py

"""
import json
import os

import toolkit_config as cfg

# ----------------------------------------------------------------------------
# Location of files and folders
# Instructions:
#   - Replace the '<COMPLETE THIS PART>' strings with the appropriate
#   expressions.
# IMPORTANT:
#   - Use the appropriate method from the `os` module to combine paths
#   - Do **NOT** include full paths like "C:\\User...". You **MUST* combine
#     paths using methods from the `os` module
#   - See the assessment description for more information
# ----------------------------------------------------------------------------

ROOTDIR = os.path.join(cfg.PRJDIR, 'project1')
DATDIR = os.path.join(ROOTDIR, 'data')
TICPATH = os.path.join(ROOTDIR, 'TICKERS.txt')

# ----------------------------------------------------------------------------
# Variables describing the contents of ".dat" files
# Instructions:
#   - Replace the '<COMPLETE THIS PART>' string with the appropriate
#     expression.
#   - See the assessment description for more information
# ----------------------------------------------------------------------------
# NOTE: `COLUMNS` must be a list, where each element is a column name in the
# order they appear in the ".dat" files
COLUMNS = ['Volume','Date','Adj Close','Close','Open','High']

# NOTE: COLWIDTHS must be a dictionary with {<col> : <width>}, where
# - Each key (<col>) is a column name in the `COLUMNS` list
# - Each value (<width>) is an **integer** with the width of the column, as
#   defined in your README.txt file
#
COLWIDTHS = {'Volume': 14, 'Date': 11,'Adj Close': 19, 'Close': 10, 'Open': 6, 'High': 20}


# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def get_tics(pth):
    """ Reads a file containing tickers and their corresponding exchanges.
    Each non-empty line of the file is guaranteed to have the following format:

    "XXXX"="YYYY"

    where:
        - XXXX represents an exchange.
        - YYYY represents a ticker.

    This function should return a dictionary, where each key is a properly formatted
    ticker, and each value the properly formatted exchange corresponding to the ticker.

    Parameters
    ----------
    pth : str
        Full path to the location of the TICKERS.txt file.

    Returns
    -------
    dict
        A dictionary with format {<tic> : <exchange>} where
            - Each key (<tic>) is a ticker found in the file specified by pth (as a string).
            - Each value (<exchange>) is a string containing the exchange for this ticker.

    Notes
    -----
    The keys and values of the dictionary returned must conform with the following rules:
        - All characters are in lower case
        - Only contain alphabetical characters, i.e. does not contain characters such as ", = etc.
        - No spaces
        - No empty tickers or exchanges

    """
    with open(pth, mode='r') as change_dic_fobj:
        dict={}
        for line in change_dic_fobj:
            exchange, ticker = tuple(line.strip().replace('\"','').lower().split('='))
            dict[ticker] = exchange
        return dict




# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def read_dat(tic):
    """ Returns a list with the lines of the ".dat" file containing the stock
    price information for the ticker `tic`.


    Parameters
    ----------
    tic : str
        Ticker symbol, in lower case.

    Returns
    -------
    list
        A list with the lines of the ".dat" file for this `tic`. Each element
        is a line in the file, without newline characters (e.g. '\n')


    Hints (optional)
    ----------------
    - Create a variable with the location of the relevant file using the `os`
      module, the `DATDIR` constant, and f-strings.

    """
    # IMPORTANT: The answer to this question should NOT include full paths
    # like "C:\\Users...". There should be no forward or backslashes.
    # <COMPLETE THIS PART>
    pth = os.path.join(DATDIR, f"{tic}_prc.dat")
    with open(pth, mode='r') as change_list_fobj:
        lines = []
        for i in change_list_fobj:
             lines.append(i.strip())
    return lines



# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def line_to_dict(line):
    """Returns the information contained in a line of a ".dat" file as a
    dictionary, where each key is a column name and each value is a string
    with the value for that column.

    This line will be split according to the field width in `COLWIDTHS`
    of each column in `COLUMNS`.

    Parameters
    ----------
    line : str
        A line from ".dat" file, without any newline characters

    Returns
    -------
    dict
        A dictionary with format {<col> : <value>} where
        - Each key (<col>) is a column in `COLUMNS` (as a string)
        - Each value (<value>) is a string containing the correct value for
          this column.

    Hints (optional)
    ----------------
    - Your solution should include the constants `COLUMNS` and `COLWIDTHS`
    - For each line in the file, extract the correct value for each column
      sequentially.

    """
    dict = {}

    i = 0
    for column in COLUMNS:
        dict[column] = line[i:i +COLWIDTHS[column]]
        i += COLWIDTHS[column]
    return dict


# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def verify_tickers(tic_exchange_dic, tickers_lst= None):
    """Verifies if the tickers provided are valid according to the rules provided in the Notes.
        If a rule is broken, this function should raise an Exception.

        Parameters
        ----------
        tic_exchange_dic : dict
            A dictionary returned by the `get_tics` function

        tickers_lst : list, optional
            A list containing tickers (as strings) to be verified

        Returns
        -------
        None
            This function does not return anything

        Notes
        -----
        If tickers_lst is not None, raise an Exception if any of the below rules are violated:
            1. tickers_lst is an empty list.

            2. tickers_lst contains a ticker that does not correspond to a key tic_exchange_dic

               Example:
               If tic_exchange_dic is {'tsm':'nyse', 'aal':'nasdaq'},
               tickers_lst = ['aal', 'Tsm'] would raise an Exception because
               'Tsm' is not a key of tic_exchange_dic.

    """
    if tickers_lst is None:
        pass
    elif tickers_lst == []:
        raise Exception('tickers_lst is an empty list')
    else:
        for i in tickers_lst:
            if i in list(tic_exchange_dic.keys()):
                continue
            else:
                raise Exception(f"tickers_lst contains a {i} that does not correspond to a key tic_exchange_dic")



# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def verify_cols(col_lst=None):
    """Verifies if the column names provided are valid according to the rules provided in the Notes.
        If a rule is broken, this function should raise an Exception.

        Parameters
        ----------
        col_lst : list, optional
            A list containing column names (as strings) to be verified

        Returns
        -------
        None
            This function does not return anything

        Notes
        -----
        If col_lst is not None, raise an Exception if any of the below rules are violated:
            1. col_lst is an empty list.

            2. col_lst contains a column that is not found in `COLUMNS`.

               Example:
               If COLUMNS = ['Close', 'Date'],
               col_lst = ['close'] would raise an Exception because 'close' is not found in `COLUMNS`

    """
    if col_lst is None:
        pass
    elif col_lst == []:
        raise Exception('col_lst is an empty list')
    else:
        for i in col_lst:
            if i in COLUMNS:
                continue
            else:
                raise Exception(f"col_lst contains a {i} that is not found in `COLUMNS`")



# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def create_data_dict(tic_exchange_dic, tickers_lst=None, col_lst=None):
    """Returns a dictionary containing the data for the tickers specified in tickers_lst.
        An Exception is raised if any of the tickers provided in tickers_lst or any of the
        column names provided in col_lst are invalid.

        Parameters
        ----------
        tic_exchange_dic: dict
            A dictionary returned by the `get_tics` function

        tickers_lst : list, optional
            A list containing tickers (as strings)

        col_lst : list, optional
            A list containing column names (as strings)

        Returns
        -------
        dict
            A dictionary with format {<tic> : <data>} where
            - Each key (<tic>) is a ticker in tickers_lst (as a string)
            - Each value (<data>) is a dictionary with format
                {
                    'exchange': <tic_exchange>,
                    'data': [<dict_0>, <dict_1>, ..., <dict_n>]
                }
              where
                - <tic_exchange> refers to the exchange that <tic> belongs to in lower case.
                - <dict_0> refers to the dictionary returned by line_to_dict(read_dat(<tic>)[0]),
                  but that only contains the columns listed in col_lst
                - <dict_n> refers to the dictionary returned by line_to_dict(read_dat(<tic>)[-1]),
                  but that only contains the columns listed in col_lst

        Notes
        -----
        - Please refer to the assessment description for an example of what the returned dictionary should look like.
        - If tickers_lst is None, the dictionary returned should contain the data for
          all tickers found in tic_exchange_dic.
        - If col_lst is None, <dict_0>, <dict_1>, ... should contain all the columns found in `COLUMNS`

        Hints (optional)
        ----------------
        - To check if tickers_lst contains any invalid tickers, you can call `verify_tickers`
        - To check if col_lst contains any invalid column names, you can call `verify_cols`
        - This function should call the `read_dat` and `line_to_dict` functions

    """
    # The first section；
    verify_tickers(tickers_lst)
    verify_cols(col_lst)
    if tickers_lst is None:
        tickers_lst = list(tic_exchange_dic.keys())
    if col_lst is None:
        col_lst = COLUMNS

    # The second section:
    dict = {}
    for tic in tickers_lst:
        tic_dict = {}
        tic_dict["stock_exchange"] = tic_exchange_dic[tic]

        stock_DATA = []
        lines = read_dat(tic)
        for line in lines:
            daily_record = {}
            for col in col_lst:
                daily_record[col] = line_to_dict(line)[col]
            stock_DATA.append(daily_record)

        tic_dict['data'] = stock_DATA
        dict[tic] = tic_dict

    # to present the result
    return dict




# ---------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def create_json(data_dict, pth):
    """Saves the data found in the data_dict dictionary into a
        JSON file whose name is specified by pth.

        Parameters
        ----------
        data_dict: dict
            A dictionary returned by the `create_data_dict` function

        pth : str
            The complete path to the output JSON file. This is where the file with
            the data will be saved.


        Returns
        -------
        None
            This function does not return anything

    """
    with open(pth, mode='w') as Finish_fobj:
        json.dump(data_dict, Finish_fobj)


# ----------------------------------------------------------------------------
#    Please put your answers for the last question here:
# ----------------------------------------------------------------------------
    """
    STEP 10 the Open-ended Question
    1. Explain why to configure as in step 1
        The configuration constructs a separate Python file for the whole project, which can be imported as an independent entity to different projects. 
        The standardised configuration is to cooperate with all the team members effectively. 
        The highly standardised configuration simplifies importing modular fundamental settings, improving the convenience of managing data and settings and the consistency with the team coding environment. 
        To avoid hard-coding and complicated coding, the configuration builds up the module setting file to reduce the difficulties in the coding periods and increase the productivity of the development. 
        The distinct relationship between the configured file and the project provides outstanding understandability and well-organised coding structures to the management team to work on the code and maintenance of the project. 
        The feature also provides traceability for the overall project; the configuration can be easily saved safely, the coding errors can be tracked and modified, and the fundamental coding issue of the project can be located without meaningless searching.

    2. Explain which one of the two hypotheses is more likely to be true. Please evaluate both hypotheses.
       On the first hypothesis, if the journalist writing the view of the firm performance based on the "investors' evaluations of those firms", the output of the articles combines the different opinions from variable investors and the negative word or pessimistic investment mood also presented the majority of the investors are negatively view on those corporations. 
        If the observation of the investor evaluation is sufficient, the investor's view will cause pessimistic market sentiment. 
        Additionally, Lehner Investments (2024) indicates the market sentiment will significantly impact short-term market reactions driven by fear and greed. 
        This phenomenon will cause the individual investor to make irrational trading decisions in the short term. 
        However, the short-term negative market sentiment makes it difficult to impact the market in the long run; the individual investor will purchase more when the institutional, professional manager captures the buy-in signal and makes a large volume of long positions in an undervalued price, the market will be reversed which makes stock price will be increased. 
        Therefore, the first hypothesis is less likely to cause the second observation to happen.
        
        On the other second hypothesis, if the journalist writing the view of the firm performance based on the "valuable information beyond firm fundamentals", the negative perspective presented in the article is supported by the valuable information, which causes panic emotion to the individual investor duo the unknown valuable information and the fear of market movement. 
        Furthermore, the panic emotion targets the pessimistic market sentiment and irrational investment decisions, which creates significant uncertainty in the capital market environment and lots of selling pressure on the share of the related corporations. 
        Additionally, the negatively valuable information beyond the corporation's fundamentals makes it difficult for investors to determine that the information will have a serious impact on the corporation's future activities or daily operations. 
        Therefore, uncertainty will always exist in those corporations, which decreases the long-term investor's expectation of the company's future profitability, and the share prices are difficult to reverse in the long run.
    
    
    3. Given the hypothesis you have chosen, evaluate the short-run predictability for the trading volume with reason(s)
        Tetlock's article indicates that the pessimism created by the journal will cause a general downturn in the market price and contribute to an unusually high trading volume in the market (2007). 
        Additionally, once the individual investor captures the increasing selling trading volume, they will confirm the stock momentum of selling and identify the selling trend, further forming a more significant selling trading and extending the trading volume. 
        Furthermore, the outstanding trading volume also attracts individuals to implement their shorting strategies and the reverse traders to trade in the opposite trend from the market, increasing the trading volume to a higher level in the short run.

    references: 
    Bowman, R. (2021) Sentiment analysis - market sentiment and how it affects the stock market, LEHNER INVESTMENTS. Available at: https://www.lehnerinvestments.com/en/sentiment-analysis-stock-market-sentiment/ (Accessed: 22 March 2024). 
    TETLOCK, P.C. (2007) ‘Giving content to investor sentiment: The role of media in the stock market’, The Journal of Finance, 62(3), pp. 1139–1168. doi:10.1111/j.1540-6261.2007.01232.x. 
    
    """

# ----------------------------------------------------------------------------
#   Test functions:
#   The purpose of these functions is to help you test the functions above as
#   you write them.
#   IMPORTANT:
#   - These functions are optional, you do not have to use them
#   - These functions do not count as part of your assessment (they will not
#     be marked)
#   - You can modify these functions as you wish, or delete them altogether.
# ----------------------------------------------------------------------------
def _test_get_tics():
    """ Test function for the `get_tics` function. Will print the tickers as
    returned by the `get_tics` function.
    """
    pth = TICPATH
    tics = get_tics(pth)
    print(tics)


def _test_read_dat():
    """ Test function for the `read_dat` function. Will read the lines of the
    first ticker in `TICPATH` and print the first line in the list.
    """
    pth = TICPATH
    tics = sorted(list(get_tics(pth).keys()))
    tic = tics[0]
    lines = read_dat(tic)
    # Print the first line in the file
    print(f'The first line in the dat file for {tic} is:')
    print(lines[0])


def _test_line_to_dict():
    """ Test function for the `read_dat` function. This function will perform
    the following operations:
    - Get the tickers using `get_tics`
    - Read the lines of the ".dat" file for the first ticker
    - Convert the first line of this file to a dictionary
    - Print this dictionary
    """
    pth = TICPATH
    tics = sorted(list(get_tics(pth).keys()))
    lines = read_dat(tics[0])
    dic = line_to_dict(lines[0])
    print(dic)


def _test_verify_cols():
    print(COLUMNS)
    col_lst = ['Adj Close']
    verify_cols(col_lst)

def _test_verify_tickers():
    pth = TICPATH
    tic_exchange_dic = get_tics(pth)
    print(list(tic_exchange_dic.keys()))
    tickers_lst = ['aapl', 'tsla']
    verify_tickers(tic_exchange_dic, tickers_lst)

def _test_create_data_dict():
    """ Test function for the `create_data_dict` function. This function will perform
    the following operations:
    - Get the tickers using `get_tics`
    - Call `create_data_dict` using
        - tickers_lst =  ['aapl', 'baba']
        - col_lst = ['Date', 'Close']
    - Print out the dictionary returned, but only the first 3 items of the data list for each ticker for brevity

    """
    pth = TICPATH
    tic_exchange_dic = get_tics(pth)
    tickers_lst = ['aapl', 'baba']
    col_lst = ['Date', 'Close']
    data_dict = create_data_dict(tic_exchange_dic, tickers_lst, col_lst)

    for tic in tickers_lst:
        data_dict[tic]['data'] = data_dict[tic]['data'][:3]

    print(data_dict)


def _test_create_json(json_pth):
    """ Test function for the `create_json_ function.
    This function will save the dictionary returned by `create_data_dict` to the path specified.

    """
    pth = TICPATH
    tic_exchange_dic = get_tics(pth)
    tickers_lst = ['aapl', 'baba']
    col_lst = ['Date', 'Close']
    data_dict = create_data_dict(tic_exchange_dic, tickers_lst, col_lst)
    create_json(data_dict, json_pth)
    print(f'Data saved to {json_pth}')


# ----------------------------------------------------------------------------
#  Uncomment the statements below to call the test and/or main functions.
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    # Test functions
    #_test_get_tics()
    #_test_read_dat()
    #_test_line_to_dict()
    #_test_verify_tickers()
    #_test_verify_cols()
    #_test_create_data_dict()
    #_test_create_json(os.path.join(DATDIR, 'data.json'))  # Save the file to data/data.json
    pass





