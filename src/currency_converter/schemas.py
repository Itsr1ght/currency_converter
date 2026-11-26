from pydantic import BaseModel, Field


class ConvertResponse(BaseModel):
    from_currency: str = Field(alias="from", examples=["INR"])
    to_currency: str = Field(alias="to", examples=["JPY"])
    amount: str = Field(examples=[100])
    rate: str = Field(examples=[0.90])
    result: str = Field(examples=[90.0])


class CurrencyInfo(BaseModel):
    code: str
    name: str
    numeric: str


class CurrenciesResponse(BaseModel):
    count: int
    currencies: list[CurrencyInfo]
