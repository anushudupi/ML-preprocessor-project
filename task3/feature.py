import click
import pandas as pd
from PyInquirer import prompt as piq
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PowerTransformer
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import MaxAbsScaler
from sklearn.preprocessing import QuantileTransformer

questions = [
    {
        'type': 'list',
        'name': 'user_option',
        'message': 'choose type of feature scaling - ',
        'choices': ["Normalisation/MinMaxScaling", "Standardisation/z-score", "PowerTransformer", "RobustScaler",
                    "MaxAbsScaler","QuantileTransformer"]
    }
]

@click.command()
@click.option('-f', prompt='enter pre processed csv file location', help='location of csv file')
def hello(f):
    """cli program to read csv file and implement feature scaling

       format: python feature.py -f 'filename.csv' """
    answers = piq(questions)
    try:
        df = pd.read_csv(f)
        for a in df.columns:
            if df[a].dtypes == 'object':
                df.drop([a], axis=1, inplace=True)
        df.dropna(inplace=True)
        if answers.get("user_option") == "Normalisation/MinMaxScaling":
            scaler = MinMaxScaler().fit(df)
            dfx = pd.DataFrame(scaler.transform(df), columns=df.columns)
            print(dfx)
        elif answers.get("user_option") == "Standardisation/z-score":
            scaler = StandardScaler().fit(df)
            dfx = pd.DataFrame(scaler.transform(df), columns=df.columns)
            print(dfx)
        elif answers.get("user_option") == "PowerTransformer":
            scaler = PowerTransformer(method='yeo-johnson')
            dfx = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
            print(dfx)
        elif answers.get("user_option") == "RobustScaler":
            scaler = RobustScaler()
            dfx = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
            print(dfx)
        elif answers.get("user_option") == "MaxAbsScaler":
            scaler = MaxAbsScaler()
            dfx = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
            print(dfx)
        elif answers.get("user_option") == "QuantileTransformer":
            scaler = QuantileTransformer()
            dfx = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

            print(dfx)

    except:
        print("csv file not found")


if __name__ == '__main__':
    hello()
