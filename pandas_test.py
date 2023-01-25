import pandas as pd
from pandas import DataFrame, Series  # for convenience

data1 = { 'time': [1,2,3,4,5],
        'X-Coord': [1,2,3,4,5],
        'Y-Coord': [6,7,8,9,10] }

data2 = { 'time': [1,3,5,7,9],
        'Feature1': [10,20,30,40,50],
        'Feature2': [.1, .2, .3, .4, .5] }

df1 = DataFrame(data1)
df2 = DataFrame(data2)

# Concatenates by column
df_col = pd.concat([df1, df2], axis=1)

# Full outer join.
df_outer = pd.merge(df1, df2, on='time', how='outer')
print(df_outer)


# Make sure to include .xlsx at the end of the filename
# fileLocation = 'C:\\Shri\\Princeton 2019 Research\\0622_Microrheology_05\\Water\\0622_Water_MSD.xlsx'


# IMPORTANT NOTE: Each time you write to an excel, it completely wipes the whole excel spreadsheet.
# Once a workbook has been saved it is not possible write further data without rewriting the whole workbook.
# For writing to multiple sheets at a time (sheets don't have to exist)
'''
with pd.ExcelWriter(fileLocation) as writer:
    df1.to_excel(writer, sheet_name='Test Sheet 1', engine='xlsxwriter')
    df2.to_excel(writer, sheet_name='Test Sheet 2',)
    df_col.to_excel(writer, sheet_name='Test Sheet 3')
    df_outer.to_excel(writer, sheet_name='Test Sheet 4')
    df_outer.to_excel(writer, sheet_name='Test Sheet 5')
'''

# For writing to a single sheet at at time (sheet doesn't have to exist)
# df2.to_excel(fileLocation, sheet_name='Sheet 2')


# For reading a data frame from an excel sheet, do 
# df_read = pd.read_excel(fileLocation, sheet_name='Sheet 2', index_col= 0)
# print(df_read)