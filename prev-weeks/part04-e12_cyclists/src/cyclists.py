#!/usr/bin/env python3
import pandas as pd
def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)


def cyclists():
    df = pd.read_csv(get_path('Helsingin_pyorailijamaarat.csv'), sep=';')
    return df.dropna(how='all', axis=0).dropna(how='all', axis=1)

def main():
    print('cyclist data:', cyclists().shape)
    return

if __name__ == "__main__":
    main()
