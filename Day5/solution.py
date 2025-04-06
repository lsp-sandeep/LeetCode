import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    
    logs['prev_num'] = logs.num.shift(1)
    logs['next_num'] = logs.num.shift(-1)

    flag = (logs['num'] == logs['prev_num']) & (logs['num'] == logs['next_num'])

    ConsecutiveNums = logs.loc[flag,'num'].drop_duplicates()

    return pd.DataFrame({'ConsecutiveNums' : ConsecutiveNums})