import pandas as pd
import numpy as np
import xlsxwriter
import os

def writeToExcel(pandas_dataframe, file, sheet_name="Sheet1", index=False, first_column='A:A', second_column='B:B', first_column_width=None, second_column_width=None):
    """Format Excel output data column to wrap text."""
    newdf = pandas_dataframe
    writer = pd.ExcelWriter(file, engine='xlsxwriter')
    newdf.to_excel(writer, sheet_name=sheet_name, index=index)
    workbook = writer.book
    worksheet = writer.sheets[sheet_name]
    center_format = workbook.add_format()
    center_format.set_align('left')
    center_format.set_align('vcenter')
    worksheet.set_column(first_column, first_column_width, center_format)
    wrap_format = workbook.add_format({'text_wrap': True})
    worksheet.set_column(second_column, second_column_width, wrap_format)
    writer.save()


df1 = pd.read_excel("C:\\Users\\mmendenh\\Documents\\CPLWVaultProjectFiles\\CPLW_ALL_FILES(12-3-2018).xlsx").sort_index()
npfirst = df1.values
first = npfirst.tolist()

df2 = pd.read_excel("C:\\Users\\mmendenh\\Documents\\CPLWVaultProjectFiles\\CPLW_DuplicatesInVault(12-3-2018).xlsx").sort_index()
npsecond = df2.values
second = npsecond.tolist()

temp = [x[0] for x in second]

matches = []
differences = []

# Get matches and differences lists
for i in range(len(first)):
    if(first[i][0] in temp):
        matches.append(first[i])
    else:
        differences.append(first[i])

# Outputs differences (original list without items from second list) to excel file
writeToExcel(pd.DataFrame(differences, columns=["FileName", "FileLocation"]), "C:\\Users\\mmendenh\\Documents\\CPLWVaultProjectFiles\\CPLW_Need_MetaData(12-4-2018).xlsx", first_column_width=60, second_column_width=200)