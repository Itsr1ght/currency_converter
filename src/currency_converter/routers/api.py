import logging

import pycountry
from fastapi import APIRouter, Query, Request

logger = logging.getLogger("currency_converter")

router = APIRouter(prefix="/api", tags=["api"])
from ..schemas import ConvertResponse, CurrenciesResponse, CurrencyInfo


@router.get("/convert", response_model=ConvertResponse)
async def convert(
    request: Request,
    from_currency: str = Query(min_length=3, max_length=3),
    to_currency: str = Query(min_length=3, max_length=3),
    amount: float = Query(gt=0, default=1.0),
) -> dict:

    rate = 1.0

    return {
        "from": from_currency.upper(),
        "to": to_currency.upper(),
        "amount": str(amount),
        "rate": str(rate),
        "result": str(round(amount * rate, 2)),
    }


@router.get("/currencies", response_model=CurrenciesResponse)
async def currencies() -> CurrenciesResponse:

    currencies = [
        CurrencyInfo(code=c.alpha_3, name=c.name, numeric=c.numeric)
        for c in sorted(pycountry.currencies, key=lambda c: c.alpha_3)
    ]
    return CurrenciesResponse(count=len(currencies), currencies=currencies)
