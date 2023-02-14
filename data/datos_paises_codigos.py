import pandas as pd
from pathlib import Path
import os

base_dir = Path.cwd()
print(base_dir)
direct = os.path.join(base_dir, "data\country_code.xlsx")
print(direct)

dcc = pd.read_excel(direct, 
                    index_col=False, 
                    engine='openpyxl')
dcc_df = pd.DataFrame(dcc)  # Convert to DataFrame
dcc_list = dcc_df.to_numpy().tolist()  # Convert rows on lists
# print(df_list)

# Convert a list on a dictionary
dcc_dic = {}
dc_list = []
for i in range(0, len(dcc_list)):
    dcc_dic[dcc_list[i][0]] = dcc_list[i][1]
    dc_list.append(dcc_list[i][0])
print(dcc_dic)
print(dc_list)
print(dc_list.index('Ecuador'))

