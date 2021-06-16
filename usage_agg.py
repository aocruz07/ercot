# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 19:33:37 2021

@author: aocru
"""

import pandas as pd
import glob

path = r"C:\Users\aocru\OneDrive\Desktop\ercot_files"
#path = "/Users/alexandercruz/Desktop/ercot_files"

file_list = glob.glob(path + "\*.xlsx")

for file in file_list:
    #print(file)
    df = pd.read_excel(file, sheet_name="Usage")
    legal_name = df.CustLastName_vc[0]
    df_keep = df[["CustNo_i", "LDCAcctNo_vc", "ReadDate_sdt", "Consumption_n", "ConsumptionType"]]
    df_keep = df_keep[df.ConsumptionType == "KWH TOTAL"]
