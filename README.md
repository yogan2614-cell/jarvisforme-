# JARVISFORME

A modular personal AI assistant foundation.

## Phase 1

- Gemini-powered text brain
- Command router
- Optional ElevenLabs text-to-speech
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

Then add your own `GEMINI_API_KEY`. ElevenLabs values are optional for Phase 1 voice output.

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
├── voice/
│   └── elevenlabs.py
├── app.py
├── .env.example
├── .gitignore
└── requirements.txt
```

API keys are loaded from `.env` and are intentionally excluded from Git.
