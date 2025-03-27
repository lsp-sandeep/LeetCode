import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    max_salary = employee['salary'].max()
    second_highest_salary = employee[employee['salary'] != max_salary]['salary'].max()
    
    return pd.DataFrame({'SecondHighestSalary': [second_highest_salary]})