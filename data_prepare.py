import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def information_checking(data):
    #print(data.head())
    #print(data.describe())

    for column in data.columns:
        all_index = data[data[column].isnull()].index
        numerical = True if data[column].dtype == 'float64' else False
        for index in all_index:
            if(numerical):
                data.loc[index,column] = data[column].mean()

        print(data[column].isnull().any())

def visualization_prep(data):
    #Get some information on the campaigns target, education level, year of birth...
    education_levels = data["Education"].value_counts()
    years_births = data['Year_Birth'].value_counts()
    marital_status = data['Marital_Status'].value_counts()
    print(marital_status)

    fig,axes = plt.subplots(1,2, figsize=(10,5))
    axes[0].pie(education_levels, labels=education_levels.index, autopct='%1.1f%%')
    axes[0].set_title('Education levels')

    axes[1].pie(marital_status, labels=marital_status.index, autopct='%1.1f%%')
    axes[1].set_title('Marital status')

    plt.show()


route = "./data/marketing_campaign.xlsx"
data = pd.read_excel(route)
#visualization_prep(data)
information_checking(data)
