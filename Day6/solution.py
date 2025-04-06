import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    employee['managerSalary'] = (
        pd.merge(
            left= employee[['id', 'managerId']],
            right= employee[['id', 'salary']],
            how= 'left',
            left_on= 'managerId',
            right_on= 'id'
        )['salary']
    )

    return pd.DataFrame({'Employee': employee[employee['salary'] > employee['managerSalary']]['name']})
