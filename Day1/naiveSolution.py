import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    '''
    This function returns the nth highest salary from the employee table
    '''
    employee['rank'] = employee['salary'].rank(method= 'dense', ascending= False)

    val = employee[employee['rank'] == N]['salary'].min()
    out = pd.DataFrame({f'getNthHighestSalary({N})': [val]})

    return out