import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def information_checking(data):
    #This function is a pretty typical one when working with datasets. What we are going is basically searching for missing values.
    #There are many techniques to replace missing values, personally I replace them for the mean of the column they belong to.
    #I preffer it because it is not going to change the representation.
    for column in data.columns:
        all_index = data[data[column].isnull()].index
        numerical = True if data[column].dtype == 'float64' else False
        for index in all_index:
            if(numerical):
                data.loc[index,column] = data[column].mean()

        print(data[column].isnull().any())

def visualization_prep(data):
    #Get some information on the campaigns target, education level, year of birth...

    #First of all, we are going to get some counts of the aparitions for each value in some columns of interest
    education_levels = data["Education"].value_counts()
    years_births = data['Year_Birth'].value_counts()
    marital_status = data['Marital_Status'].value_counts()
    education_options = data["Education"].value_counts()

    #We are going to provide relevant details depending on the client level of studies completed
    phd_rows = education_options.keys()
    gold_spent_dict = {}
    fish_spent_dict = {}
    for row in phd_rows:
        gold_spent_dict[row] = data[data["Education"]==row]["MntGoldProds"].mean()
        fish_spent_dict[row] = data[data["Education"]==row]["MntFishProducts"].mean()


    #Creating Pie plot to visualize the value counts for education levels and marital status
    fig,axes = plt.subplots(1,2, figsize=(10,5))
    axes[0].pie(education_levels, labels=education_levels.index, autopct='%1.1f%%')
    axes[0].set_title('Education levels')

    axes[1].pie(marital_status, labels=marital_status.index, autopct='%1.1f%%')
    axes[1].set_title('Marital status')
    plt.show()

    #Creating bar plots to visualize how many products of fish and gold people buy
    fig,axes = plt.subplots(1,2, figsize=(10,5))
    axes[0].bar(gold_spent_dict.keys(), gold_spent_dict.values())
    axes[0].set_title("Gold products per PhD havers")

    axes[1].bar(fish_spent_dict.keys(), fish_spent_dict.values())
    axes[1].set_title("Fish products per PhD havers")

    plt.show()


def trial(data):
    education = data["Education"].value_counts().keys()
    for row in education:
        print(data[data["Education"]==row]["MntGoldProds"].mean())



#trial(data)
