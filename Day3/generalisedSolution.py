import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    unique_salaries = (
        employee['salary']
        .sort_values(ascending= False)
        .drop_duplicates()
    )

    if len(unique_salaries) >= 2:
        val = unique_salaries.iloc[1]
    else:
        val = pd.NA
    
    return pd.DataFrame({'SecondHighestSalary': [val]})