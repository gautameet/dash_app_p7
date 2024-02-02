 ## Import des librairies
import streamlit as st
import altair as alt              # for data visualtization
from PIL import Image
import requests
import os
os.environ["SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL"] = "True"
from zipfile import ZipFile, BadZipFile
import pickle
import sys
#import shap


st.title("Test project 7 dashboaard")

feat = ['SK_ID_CURR','TARGET','DAYS_BIRTH','NAME_FAMILY_STATUS','CNT_CHILDREN',
        'DAYS_EMPLOYED','NAME_INCOME_TYPE','AMT_INCOME_TOTAL','AMT_CREDIT','AMT_ANNUITY']

# Nombre de ligne
num_rows = 100000

# Original Data
zip_file_train = ZipFile('./sample_application_train.zip')
print(zip_file_train.namelist())
try:
    raw_train = pd.read_csv(zip_file_train.open('sample_application_train.csv'), usecols=feat, nrows=num_rows)
#with ZipFile(zip_file_train, 'r') as zip_train:
except Exception as e:
    print(f'Error:{e}')
