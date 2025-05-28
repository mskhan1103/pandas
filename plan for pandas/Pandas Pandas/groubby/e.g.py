import pandas as pd

data = {
    'Department': ['IT', 'HR', 'IT', 'HR', 'Finance', 'Finance'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Salary': [70000, 50000, 80000, 55000, 60000, 62000]
}
print("data")
df = pd.DataFrame(data)
print(df)


# Group by 'Department' and calculate the mean salary
gby=df.groupby("Department")
print(gby["Salary"].mean())
print(gby.size())
print(gby.get_group("IT"))