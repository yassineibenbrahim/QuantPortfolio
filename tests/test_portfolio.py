from __future__ import annotations

import unittest

import pandas as pd

from backend.app.analytics.portfolio import max_sharpe_weights


class PortfolioAnalyticsTests(unittest.TestCase):
    def test_max_sharpe_weights_sum_to_one(self) -> None:
        returns = pd.DataFrame(
            {
                "A": [0.01, 0.02, -0.01, 0.01],
                "B": [0.005, 0.007, -0.002, 0.004],
                "C": [0.015, 0.01, -0.015, 0.012],
            }
        )
        weights = max_sharpe_weights(returns)

        self.assertAlmostEqual(float(weights.sum()), 1.0, places=8)
        self.assertTrue((weights >= 0.0).all())
        self.assertListEqual(list(weights.index), ["A", "B", "C"])

    def test_empty_returns_raises(self) -> None:
        with self.assertRaises(ValueError):
            max_sharpe_weights(pd.DataFrame())


if __name__ == "__main__":
    unittest.main()
