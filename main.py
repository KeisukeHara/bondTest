from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

class BondTrade(BaseModel):
    id:Optional[str] = None
    notional:Optional[float] = None
    price:Optional[float] = None

app = FastAPI()

@app.get("/")
async def top():
    print("log:top")
    return {"message": "calc pv of bond trade."}

@app.post("/bond/")
async def calc_pv(trade: BondTrade):
    print("log:POST")
    return {"id": trade.id, "pv": int(trade.price / 100 * trade.notional)}