import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    return pd.DataFrame({f'getNthHighestSalary({N})' : [pd.NA if N <= 0 or len(employee['salary'].unique()) < N else employee.sort_values(by='salary', ascending=False)['salary'].unique()[N - 1]]})
