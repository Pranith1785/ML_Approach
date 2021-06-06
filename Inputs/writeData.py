
import os
import pandas as pd


def writeToCsv(dataframe,filePath):
    print(filePath)
    return dataframe.to_csv(filePath,sep=",",header=True,index=False)
    
def writeToExcel(dataframe,filePath,sheetName):
    return dataframe.to_excel(filePath,sheet_name=sheetName,header=True,index=False)

def writeToJson(dataframe,filePath):
    return dataframe.to_json(filePath)



