#!/usr/bin/env python3
import pandas as pd

data = {'Population':
    [643272, 279044, 231853, 223027, 201810],
    'Total area':
    [715.48, 528.03, 689.59, 240.35, 3817.52]
}

city_names = ['Helsinki', 'Espoo', 'Tampere', 'Vantaa', 'Oulu']

def cities():
    df = pd.DataFrame(data, index=city_names)
    return df

def main():
    print(cities().head(5))
    return cities

if __name__ == "__main__":
    main()

