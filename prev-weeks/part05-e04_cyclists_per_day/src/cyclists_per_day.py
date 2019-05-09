#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

MONTHS = {
    "tammi": 1,
    "helmi": 2,
    "maalis": 3,
    "huhti": 4,
    "touko": 5,
    "kesä": 6,
    "heinä": 7,
    "elo": 8,
    "syys": 9,
    "loka": 10,
    "marras": 11,
    "joulu": 12,
}

WEEKDAYS = {
    "ma": 1,
    "ti": 2,
    "ke": 3,
    "to": 4,
    "pe": 5,
    "la": 6,
    "su": 7,
}

def split_date(df):
    d = df["Päivämäärä"].str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]

    hourmin = d["Hour"].str.split(":", expand=True)
    d["Hour"] = hourmin.iloc[:, 0]

    d["Month"] = d["Month"].map(MONTHS)
    d["Weekday"] = d["Weekday"].map(WEEKDAYS)

    d = d.astype({"Weekday": int, "Day": int, "Month": int, "Year": int, "Hour": int})
    return d

def split_dates(raw):
    df = raw.dropna(how='all', axis=0).dropna(how='all', axis=1)
    split_dates = split_date(df)
    df = pd.concat([split_dates, df], axis=1)
    return df

def cyclists_per_day():
    cyclists = split_dates(pd.read_csv(get_path('Helsingin_pyorailijamaarat.csv'), sep=';'))
    return cyclists.groupby(['Year', 'Month', 'Day']).sum()

def main():
    cyclists = cyclists_per_day()
    print(cyclists.head(10))
    cyclists = cyclists.drop(columns=['Hour', 'Weekday'])

    august2017 = cyclists.loc[(2017, 8), :]
    august2017.plot()
    plt.show()
    return

if __name__ == "__main__":
    main()
