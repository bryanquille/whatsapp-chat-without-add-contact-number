import pandas as pd

dcc = pd.read_excel('E:/COURSES/Programming Courses/Python Courses/Projects/whatsapp_chat_project/data/country_code.xlsx', index_col=False, engine='openpyxl' )
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

