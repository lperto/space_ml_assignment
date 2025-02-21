from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from features import calculate_features


app = FastAPI()


class ApplicationRequest(BaseModel):
    id: str
    application_date: str
    contracts: str | None = None


@app.get('/')
async def root():
    return RedirectResponse(url='/docs')


@app.post('/get_features')
async def process_application(data: ApplicationRequest):
    try:
        features = calculate_features(
            id=data.id, application_date=data.application_date, contracts=data.contracts
        )
        return features
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
