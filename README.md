# QuantPortfolio

QuantPortfolio is a full-stack quantitative finance application for portfolio optimization, market data analysis, and pipeline orchestration.

## Stack

- **Backend**: FastAPI + Uvicorn (`/backend/app`)
- **Analytics**: Pandas + NumPy/SciPy vectorized portfolio calculations
- **Pipeline**: Prefect + yfinance market data flow
- **Database**: PostgreSQL with SQLAlchemy + psycopg2
- **Frontend**: Next.js + TypeScript (`/frontend`)
- **Infra**: Docker + docker-compose

## Quick start

### API (local)

```bash
pip install -r requirements.txt
uvicorn backend.app.main:app --reload
```

### Frontend (local)

```bash
cd frontend
npm install
npm run dev
```

### Docker

```bash
docker compose up --build
```
