import logging

from fastapi import APIRouter, Query, Request

logger = logging.getLogger("currency_converter")

router = APIRouter(prefix="/api", tags=["api"])
from ..schemas import ConvertResponse


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
        "amount": amount,
        "rate": rate,
        "result": round(amount * rate, 2),
    }
