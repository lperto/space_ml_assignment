# ML Assignment

## Local Setup

* Install the requirements `pip install -r requirements.txt`
* Place the `data.csv` in the `data` folder
* Start the server: `uvicorn app.main:app --reload`

### API


Without contracts:
```bash
curl -X 'POST' \
  'http://localhost:8000/get_features' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "id": "2925210",
    "application_date": "2024-02-12 19:22:46.652000"
  }'
```

With single contract:
```bash
curl -X 'POST' \
  'http://localhost:8000/get_features' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "id": "2926072",
    "application_date": "2024-02-13 05:58:49.357",
    "contracts": "{\"contract_id\": \"\", \"bank\": \"013\", \"summa\": \"\", \"loan_summa\": \"\", \"claim_date\": \"13.02.2024\", \"claim_id\": 2691002, \"contract_date\": \"\"}"
  }'
```

With multiple contracts:
```bash
curl -X 'POST' \
  'http://localhost:8000/get_features' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "id": "2926173",
    "application_date": "2024-02-13 06:05:24.987",
    "contracts": "[{\"contract_id\": \"\", \"bank\": \"ORG\", \"summa\": \"\", \"loan_summa\": \"\", \"claim_date\": \"13.12.2022\", \"claim_id\": 1491348, \"contract_date\": \"\"}, {\"contract_id\": \"\", \"bank\": \"062\", \"summa\": \"\", \"loan_summa\": \"\", \"claim_date\": \"29.08.2023\", \"claim_id\": 14465636, \"contract_date\": \"\"}]"
  }'
```

## Docker Deployment

* Build the docker image: `docker build -t ml-assignment .`
* Run the docker container: `docker run -p 8000:8000 ml-assignment`

### API

## Miscellaneous
* Re-generate output: `python output.py`

