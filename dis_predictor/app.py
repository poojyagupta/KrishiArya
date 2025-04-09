import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.fao.org/4/t0756e/t0756e06.htm"

#send requests to get the content of the webpage
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

dis_data=[]

SYMPTOM_LIST = ["Fever", "Adbominal pain", "Thickened head nad ears", "Vomiting", "Abortion", "lesions", "Pneumonia", 
                "Emaciation", "Difficulty breathing", "Salivation", "Loss of appetite", "Weakness",
                "Bloody nasal discharge", "Edema", "Lameness", "Laboured breathing", "Depression", "Dry wool", "Rough skin", 
                "Biting of legs", "Grinding of teeth", "Lacrimation", "Anaemia", "Frequent coughing", "Dullness", "Swollen vulva",
                "Cough", "Frequently laying", "stiff gait", "Frothing", "Green pasty diarrhoea", "Rapid and shallow respiration", 
                "Dyspnea", "Purulent ocular", "Incomplete mastication", "Blindness", "Weight loss", "Dark reddish brown urine",
                "Ascites", "Increased heart rate", "Swollen lymph nodes", "Enlarged lymph nodes"]