from unittest import case
import pandas as pd


def count_letters(text, only_letters=False, case_sensitive=True):

    if case_sensitive == False:
        text = text.lower()

    if only_letters == True:
        print('burasi calisti')
        text = ''.join(filter(str.isalpha, text))

    charList = pd.Series(list(text)).value_counts()

    percentageTable = pd.concat(
        [charList, (charList/charList.sum())], axis=1)

    percentageTable.columns = ['Count', 'Percentage']
    return percentageTable
