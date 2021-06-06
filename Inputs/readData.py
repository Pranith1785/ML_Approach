
import os
import pandas as pd

def readCsv(filePath,header = "infer",skiprows=0):
    return pd.read_csv(filePath,sep=",",header=header,skip_blank_lines=True,skiprows=skiprows,encoding='utf-8')
    
def readExcel(filePath,header = 0,sheetName = 0,skiprows = 0):
    return pd.read_excel(filePath,sheet_name=sheetName,header=header,skiprows=skiprows,encoding='utf-8')

def readJson(filePath):
    return pd.read_json(filePath,encoding='utf-8')


def test(folderPath):
    return "pass"

def read_data(folderPath,fileType,numofFiles = 1):

    fileFunctions = {
                     "csv" : readCsv,
                     "excel" : readExcel,
                     "json"  : readJson
                    }

    fileTypeExtension = {
                         "csv" : "csv",
                         "xlsx" : "excel",
                         "json" : "json"
                        }
    iLoop = 0
    
    for fileName in os.listdir(folderPath):
        filePath = os.path.join(folderPath,fileName)
        fileExtension  = fileName.split(".")[1]
        if fileTypeExtension[fileExtension] == fileType:

            df = fileFunctions[fileType](filePath)

            if iLoop == 0 :
                final_df = df.copy()
            else:
                final_df = final_df.append(df,ignore_index=True)
                
            iLoop += 1

            if numofFiles == iLoop:
                break
            
    return final_df



