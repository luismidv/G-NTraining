import data_prepare
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder



route = "./data/marketing_campaign.xlsx"
data = pd.read_excel(route)
data_prepare.information_checking(data)

