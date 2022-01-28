import click
import pandas as pd
from PyInquirer import prompt as piq
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

questions = [
    {
        'type': 'list',
        'name': 'user_option',
        'message': 'choose type of feature scaling - ',
        'choices': ["Normalisation", "Standardisation"]
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
        for a in df[1:1]:
            if df[a].dtypes == 'object':
                df.drop([a], axis=1, inplace=True)
        df.dropna(inplace=True)
        if answers.get("user_option") == "Normalisation":
            norm = MinMaxScaler().fit(df)
            print(norm.transform(df))
        elif answers.get("user_option") == "Standardisation":
            stds = StandardScaler().fit(df)
            print(stds.transform(df))

    except:
        print("csv file not found")


if __name__ == '__main__':
    hello()
