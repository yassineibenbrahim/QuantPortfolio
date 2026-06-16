from __future__ import annotations

from sqlalchemy import Column, DateTime, Integer, Numeric, String, func

from .db import Base


class PortfolioAllocation(Base):
    __tablename__ = "portfolio_allocations"

    id = Column(Integer, primary_key=True, index=True)
    asset = Column(String(32), nullable=False, index=True)
    weight = Column(Numeric(10, 6), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
