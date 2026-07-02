# Async API Aggregator

An asynchronous Python application that fetches weather data for multiple cities concurrently using the Open-Meteo API. The project demonstrates production-oriented backend engineering concepts including async programming, concurrent API calls, data validation, retry logic, and PostgreSQL integration.

---

## Features

- Fetches weather data for multiple cities concurrently
- Uses `asyncio` and `aiohttp` for non-blocking API requests
- Limits concurrent requests using `asyncio.Semaphore`
- Validates API responses with Pydantic
- Automatic retry mechanism using Tenacity
- Stores weather data in PostgreSQL (Neon)
- Uses environment variables for secure configuration

---

## Tech Stack

- Python 3.11
- asyncio
- aiohttp
- Pydantic
- PostgreSQL
- asyncpg
- Tenacity
- python-dotenv

---

## Project Structure

```
async_api_aggregator/
│
├── app/
│   ├── api_client.py
│   ├── cities.py
│   ├── config.py
│   ├── database.py
│   └── models.py
│
├── data/
├── logs/
├── tests/
│
├── .env.example
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

---

## How It Works

1. Load a list of cities with latitude and longitude.
2. Create concurrent tasks using `asyncio.gather()`.
3. Limit active requests with `Semaphore`.
4. Fetch weather data from the Open-Meteo API.
5. Validate every response using Pydantic.
6. Retry failed requests automatically.
7. Store successful results in PostgreSQL.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/async-api-aggregator.git
cd async-api-aggregator
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
DATABASE_URL=your_postgresql_connection_string
```

Example:

```env
DATABASE_URL=postgresql://username:password@host/database?sslmode=require
```

---

## Run the Project

```bash
python main.py
```

---

## Example Output

```
city='Lahore' temperature=40.7 windspeed=11.2
city='Karachi' temperature=31.4 windspeed=19.2
city='Islamabad' temperature=37.9 windspeed=8.5

Processed 20 cities
Completed in 2.15 seconds
```

---

## Skills Demonstrated

- Async Programming
- Concurrent API Calls
- REST API Integration
- Data Validation
- Retry Logic
- PostgreSQL
- Connection Pooling
- Environment Variable Management
- Clean Project Structure

---

## Future Improvements

- Rate limiting based on API headers
- Command-line interface (CLI)
- Performance benchmarking (Sync vs Async)
- Logging and monitoring
- Docker support
- Unit and integration tests
- Circuit breaker pattern

---

## License

This project is for educational and portfolio purposes.
