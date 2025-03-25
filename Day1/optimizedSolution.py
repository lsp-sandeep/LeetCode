import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    '''
    This function returns the nth highest salary from the employee table
    '''
    ranked_salaries = (
        employee['salary']
        .sort_values(ascending= False)
        .drop_duplicates()
    )

    if N <= 0 or len(ranked_salaries) < N:
        val = pd.NA
    else:
        val = ranked_salaries.iloc[N - 1]

    out = pd.DataFrame({f'getNthHighestSalary({N})': [val]})

    return out