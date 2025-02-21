import requests


url = 'http://localhost:8000/get_features'

contracts_data = [
    {'id': '2925210', 'application_date': '2024-02-12 19:22:46.652000'},
    {
        'id': '2925212',
        'application_date': '2024-02-12 19:24:41.493000',
        'contracts': None,
    },
    {
        'id': '2925214.0',
        'application_date': '2024-02-12 19:24:56.857000+00:00',
        'contracts': None,
    },
    {
        'id': '2926072',
        'application_date': '2024-02-13 05:58:49.357',
        'contracts': '{"contract_id": "", "bank": "013", "summa": "", "loan_summa": "", "claim_date": "13.02.2024", "claim_id": 2691002, "contract_date": ""}',
    },
    {
        'id': '2926173',
        'application_date': '2024-02-13 06:05:24.987',
        'contracts': '[{"contract_id": "", "bank": "ORG", "summa": "", "loan_summa": "", "claim_date": "13.12.2022", "claim_id": 1491348, "contract_date": ""}, {"contract_id": "", "bank": "062", "summa": "", "loan_summa": "", "claim_date": "29.08.2023", "claim_id": 14465636, "contract_date": ""}]',
    },
]


def main():
    for data in contracts_data:
        print(f'-------- Sending request for "{data["id"]}"')
        response = requests.post(url, json=data)
        print(f'---- Status Code: {response.status_code}')
        print(f'---- Response: {response.json()}')
        print('--------')


if __name__ == '__main__':
    main()
