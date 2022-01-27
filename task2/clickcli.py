import click
import pandas as pd


@click.command()
@click.option('-f', prompt='enter csv file location', help='location of csv file')
@click.option('-s', prompt='enter starting row', type=int, help='starting row')
@click.option('-e', prompt='enter ending row', type=int, help='ending row row')
def hello(f, s, e):
    """cli program to read csv file and display range of rows

       format: python cli.py -f 'filename.csv' -s 'starting row' -e ending row """
    try:
        df = pd.read_csv(f)
        print(df[s:e])
    except:
        print("csv file not found")


if __name__ == '__main__':
    hello()
