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

st.title("Test project 7 dashboaard")
