import os
import pandas as pd

# create a sample dataframe
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
# to ensure data exists in the root directory 
data_dir = "data"
os.makedirs(data_dir,exist_ok =True)
file_path = os.path.join(data_dir,"sample_data.csv")
df.to_csv(file_path,index=False)