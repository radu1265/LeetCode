import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    return pd.DataFrame(data = {'SecondHighestSalary': [pd.NA if len(employee['salary'].unique()) < 2 else employee.sort_values(by='salary', ascending=False)['salary'].unique()[1]]})
