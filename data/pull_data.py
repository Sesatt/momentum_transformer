import os
from typing import List

import pandas as pd
import yfinance as yf

import numpy as np
import requests
import json
import pandas as pd
import datetime

from settings.default import PINNACLE_DATA_CUT, PINNACLE_DATA_FOLDER, QUANDL_TICKERS

def pull_quandl_sample_data(ticker: str) -> pd.DataFrame:
    return (
        pd.read_csv(os.path.join("data", "quandl", f"{ticker}.csv"), parse_dates=[0])
        .rename(columns={"Trade Date": "date", "Date": "date", "Settle": "close"})
        .set_index("date")
        .replace(0.0, np.nan)
    )

def pull_crypto_data(ticker) -> pd.DataFrame:
    comparison_symbol = 'USD'
    limit = 2000
    aggregate = 1
    api_key = '9902c6ffc3d85502297744648e73bee86fd5af1f9ba3ac4a6c444e42537a73d4'

    url = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym={}&tsym={}&limit={}&aggregate={}&allData=true&api_key={}'.format(
        ticker.upper(), comparison_symbol.upper(), limit, aggregate, api_key)
    response = requests.get(url)
    df = pd.DataFrame(response.json()['Data']['Data'])
    df['time'] = [datetime.date.fromtimestamp(d) for d in df.time]
    df = df[['time', 'close']].rename(columns = {'time':'Trade Date'}).set_index('Trade Date')[['close']]
    df.index = df.index.astype("datetime64[ns]")
    df = df.replace(0, np.nan)
    return df.dropna()


def pull_pinnacle_data(ticker: str) -> pd.DataFrame:
    return pd.read_csv(
        os.path.join(PINNACLE_DATA_FOLDER, f"{ticker}_{PINNACLE_DATA_CUT}.CSV"),
        names=["date", "open", "high", "low", "close", "volume", "open_int"],
        parse_dates=[0],
        index_col=0,
    )[["close"]].replace(0.0, np.nan)


def _fill_blanks(data: pd.DataFrame):
    return data[
        data["close"].first_valid_index() : data["close"].last_valid_index()
    ].fillna(
        method="ffill"
    )  # .interpolate()


def pull_pinnacle_data_multiple(
    tickers: List[str], fill_missing_dates=False
) -> pd.DataFrame:
    data = pd.concat(
        [pull_pinnacle_data(ticker).assign(ticker=ticker).copy() for ticker in tickers]
    )

    if not fill_missing_dates:
        return data.dropna().copy()

    dates = data.reset_index()[["date"]].drop_duplicates().sort_values("date")
    data = data.reset_index().set_index("ticker")

    return (
        pd.concat(
            [
                _fill_blanks(
                    dates.merge(data.loc[t], on="date", how="left").assign(ticker=t)
                )
                for t in tickers
            ]
        )
        .reset_index()
        .set_index("date")
        .drop(columns="index")
        .copy()
    )
