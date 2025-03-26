import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    
    combined = (
        pd.merge(
            left= person, right= address,
            how= 'left', on= 'personId'
        )
        .drop(columns= ['personId', 'addressId'])
    )

    return combined