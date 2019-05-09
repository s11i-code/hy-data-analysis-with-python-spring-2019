#!/usr/bin/env python3

import pandas as pd

URL = 'https://en.wikipedia.org/wiki/List_of_countries_by_average_yearly_temperature'

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

def suicide_fractions():
    suicides = pd.read_csv(get_path('who_suicide_statistics.csv'))
    suicides['suicide_frac'] = suicides['suicides_no']/suicides['population']
    return suicides.groupby(["country"]).mean()

def suicide_weather():
    suicides = suicide_fractions()
    temperatures = pd.read_html(get_path('List_of_countries_by_average_yearly_temperature.html'), header=0, index_col=0)[0]
    merged = pd.merge(suicides.to_frame(), temperatures, left_index=True, right_index = True)
    merged.columns = ['suicide_frac', 'avg_temp']
    merged['avg_temp'] = merged['avg_temp'].str.replace(u'\u2212','-').astype('float')
    weather_suicide_corr = merged['avg_temp'].corr(merged['suicide_frac'])
    return (suicides.shape[0], temperatures.shape[0], merged.shape[0], weather_suicide_corr)

def main():
    sw = suicide_weather()
    print("Suicide DataFrame has {} rows".format(sw[0]))
    print("Temperature DataFrame has {} rows".format(sw[1]))
    print("Common DataFrame has {} rows".format(sw[2]))
    print("Spearman correlation: {:.1f}".format(sw[3]))
    return

if __name__ == "__main__":
    main()
