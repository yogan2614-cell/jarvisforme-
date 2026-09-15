# JARVISFORME

A modular personal AI assistant foundation.

## Phase 1

- Gemini-powered text brain
- Command router
- Optional ElevenLabs text-to-speech
- PostgreSQL persistence with SQLAlchemy
- Secure `.env` configuration
- Lightweight terminal interface

## Setup

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create your local environment file:

```bash
copy .env.example .env
```

Then configure your API keys and PostgreSQL connection in `.env`.

### PostgreSQL

Install PostgreSQL locally, create a database named `jarvis`, and set `DATABASE_URL` in `.env`:

```text
DATABASE_URL=postgresql+psycopg://jarvis:password@localhost:5432/jarvis
```

Initialize the tables:

```bash
python scripts/init_db.py
```

The current database layer stores conversation history and provides durable memory helpers. PostgreSQL is optional during initial setup; JARVIS can still run without `DATABASE_URL`.

## Run

```bash
python app.py
```

Try:

```text
hello
status
Explain what you can do.
```

Type `exit` to stop.

## Project structure

```text
JARVISFORME/
├── ai/
│   └── gemini.py
├── core/
│   ├── brain.py
│   └── router.py
├── database/
│   ├── connection.py
│   ├── models.py
│   └── repository.py
├── scripts/
│   └── init_db.py
├── voice/
│   └── elevenlabs.py
├── app.py
├── .env.example
├── .gitignore
└── requirements.txt
```

API keys and local runtime data are excluded from Git.
