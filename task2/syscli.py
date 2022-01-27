import sys
import pandas as pd

try:
    df = pd.read_csv(sys.argv[1])

    try:
        print(df[int(sys.argv[2]):int(sys.argv[3])])

    except:
        print("invalid  format ")
except:
    print("csv file not found")
