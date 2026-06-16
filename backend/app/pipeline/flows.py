from __future__ import annotations

import pandas as pd
import yfinance as yf
from prefect import flow, task


@task
def fetch_prices(tickers: list[str], period: str = "1mo") -> pd.DataFrame:
    prices = yf.download(tickers=tickers, period=period, auto_adjust=True, progress=False)
    if isinstance(prices.columns, pd.MultiIndex):
        prices = prices["Close"]
    return prices.dropna(how="all")


@task
def compute_returns(prices: pd.DataFrame) -> pd.DataFrame:
    return prices.pct_change().dropna(how="all")


@flow(name="market-data-pipeline")
def market_data_pipeline(tickers: list[str], period: str = "1mo") -> pd.DataFrame:
    prices = fetch_prices(tickers=tickers, period=period)
    return compute_returns(prices=prices)
