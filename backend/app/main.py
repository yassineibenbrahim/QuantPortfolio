from __future__ import annotations

from fastapi import FastAPI
import pandas as pd

from .analytics.portfolio import max_sharpe_weights
from .schemas import HealthResponse, OptimizationResponse

app = FastAPI(title="QuantPortfolio API", version="0.1.0")


@app.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse()


@app.post("/optimize/sample", response_model=OptimizationResponse)
async def optimize_sample() -> OptimizationResponse:
    """Sample async endpoint demonstrating portfolio optimization path."""
    data = pd.DataFrame(
        {
            "AAPL": [0.01, -0.02, 0.015, 0.005],
            "MSFT": [0.008, -0.01, 0.012, 0.004],
            "GOOGL": [0.012, -0.018, 0.017, 0.003],
        }
    )
    weights = max_sharpe_weights(data)
    return OptimizationResponse(weights={k: float(v) for k, v in weights.items()})
