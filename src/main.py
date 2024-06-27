from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from schemas import SDepositParams
from service import calculate_deposit

app = FastAPI(title="Deposit App")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"error": exc.errors()[0]["msg"]}),
    )


@app.post("/deposit")
def deposit_report(data: SDepositParams):
    return calculate_deposit(data)
