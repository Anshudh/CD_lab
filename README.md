# Time Complexity Analyzer

A full-stack project that predicts the time complexity of Python and Java code using static analysis and a trained machine-learning model.

## What it does

The backend parses source code, extracts structural features such as loop counts, nesting depth, recursion, and conditional usage, then feeds those features into a Random Forest model to estimate the algorithmic complexity. The frontend provides a clean browser UI for submitting code and viewing the result.

## Project Structure

- `backend/` - FastAPI service, analyzers, model training, and tests
- `frontend/` - Static browser UI for sending code to the API

## Backend

### Requirements

- Python 3.9+
- pip

### Install

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Train the model

The API expects a trained model at `backend/models/complexity_model.pkl`.

```bash
python ml_pipeline/train_model.py
```

### Run the API

```bash
python -m uvicorn app.main:app --reload
```

The API will be available at:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/api/health
- http://127.0.0.1:8000/docs

### API endpoint

`POST /api/analyze`

Request body:

```json
{
  "language": "python",
  "code": "for i in range(n):\n    print(i)"
}
```

Supported languages:

- `python`
- `java`

## Frontend

The frontend is a single-page static app in `frontend/`.

### Run it

You can open `frontend/index.html` directly in a browser, or serve it locally with any static server:

```bash
cd frontend
python -m http.server 5173
```

Then open:

- http://127.0.0.1:5173

## Example Output

The API returns a response similar to:

```json
{
  "language": "python",
  "time_complexity": "O(n)",
  "confidence": 0.96,
  "reason": "The program contains 1 non-nested linear loop(s) that iterate through the input.",
  "features": {
    "loop_count": 1,
    "for_loop_count": 1,
    "while_loop_count": 0,
    "max_loop_depth": 1,
    "nested_loop_count": 0,
    "if_count": 0,
    "function_count": 0,
    "method_count": 0,
    "function_call_count": 2,
    "recursive": false,
    "recursive_call_count": 0,
    "ast_depth": 0,
    "statement_count": 2,
    "condition_count": 0,
    "linear_loop_count": 1,
    "logarithmic_loop_count": 0
  }
}
```

## Notes

- Predictions are heuristic estimates based on static code features, not exact complexity proofs.
- The frontend talks to `http://127.0.0.1:8000` by default.
- CORS is enabled on the backend so the browser UI can call the API.
