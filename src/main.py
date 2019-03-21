import seaborn as sns
import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
import yaml

def read_csv(filepath, separator, column_names):
    features = pd.read_csv(filepath, sep = separator, names = column_names)
    return features


def read_yaml(filepath):
    document = open(filepath, 'r')
    return yaml.load(document,Loader=yaml.FullLoader)

def main():
    current_dir=os.path.dirname(os.path.abspath(__file__))

    config_file = os.path.join(current_dir,"../resources/config.yaml")

    config_variables=read_yaml(config_file)

    config_variables.get("data_path")
    print(config_variables.get("data_path"))

    features = read_csv("../resources/ejemplo.csv", ",",
                        ["age", "workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation",
                         "relationship",
                         "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "native-country", "target"])

    features.describe()




if __name__=="__main__":

    main()