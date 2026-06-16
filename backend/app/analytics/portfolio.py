from __future__ import annotations

import numpy as np
import pandas as pd


def annualized_returns(returns: pd.DataFrame, periods_per_year: int = 252) -> pd.Series:
    """Compute annualized mean return for each asset using vectorized operations."""
    return returns.mean(axis=0) * periods_per_year


def annualized_covariance(returns: pd.DataFrame, periods_per_year: int = 252) -> pd.DataFrame:
    """Compute annualized covariance matrix using vectorized operations."""
    return returns.cov() * periods_per_year


def max_sharpe_weights(
    returns: pd.DataFrame,
    risk_free_rate: float = 0.0,
    periods_per_year: int = 252,
) -> pd.Series:
    """Compute long-only tangency-like portfolio weights that sum to 1."""
    if returns.empty:
        raise ValueError("returns must contain at least one row")

    mu = annualized_returns(returns, periods_per_year)
    cov = annualized_covariance(returns, periods_per_year)

    excess = mu.to_numpy(dtype=float) - risk_free_rate
    inv_cov = np.linalg.pinv(cov.to_numpy(dtype=float))
    raw = inv_cov @ excess

    clipped = np.clip(raw, a_min=0.0, a_max=None)
    total = float(clipped.sum())
    if total <= 0:
        clipped = np.full_like(clipped, 1.0 / len(clipped))
    else:
        clipped = clipped / total

    return pd.Series(clipped, index=returns.columns, name="weight")
