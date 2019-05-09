#!/usr/bin/env python3
import pandas as pd

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

def split_date(df):
    d = df["Päivämäärä"].str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]

    hourmin = d["Hour"].str.split(":", expand=True)
    d["Hour"] = hourmin.iloc[:, 0]

    d["Month"] = d["Month"].map(MONTHS)

    d = d.astype({"Day": int, "Month": int, "Year": int, "Hour": int})
    return d

def split_dates(raw):
    df = raw.dropna(how='all', axis=0).dropna(how='all', axis=1)
    split_dates = split_date(df)
    df = df.drop(columns="Päivämäärä")
    df = pd.concat([split_dates, df], axis=1)
    return df


def cycling_weather():
    cycling = split_dates(pd.read_csv(get_path('Helsingin_pyorailijamaarat.csv'), sep=';'))
    weather = pd.read_csv(get_path('kumpula-weather-2017.csv'))
    weather = weather.rename(columns = {'m': 'Month', 'd': 'Day'}, index=str)
    merged = pd.merge(cycling, weather)
    merged = merged.drop(["Time zone", "Time"], axis=1)
    return merged

def main():
    print(cycling_weather().head(3))
    return

if __name__ == "__main__":
    main()
