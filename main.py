from datetime import datetime
from enum import Enum
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title='Trading App')

users = [
    {'id': 1, 'role': 'admin', 'name': 'Bob'},
    {'id': 2, 'role': 'manager', 'name': 'Anne'},
    {'id': 3, 'role': 'trader', 'name': 'Marat'},
    {'id': 4, 'role': 'trader', 'name': 'Peter', 'degree':
        {
            'id': 1, 'date_joined': '2020-01-01T00:00:00', 'ranking': 'Expert'}
     },
]

trades = [
    {'id': 1, 'trader_id': 1, 'currency': 'USD', 'side': 'buy', 'price': 79.87, 'amount': 2.15},
    {'id': 2, 'trader_id': 1, 'currency': 'USD', 'side': 'sell', 'price': 79.87, 'amount': 3.27},
]


class Ranking(Enum):
    NEWBIE = 'Newbie'
    PRO = 'Pro'
    EXPERT = 'Expert'


class UserDegree(BaseModel):
    id: int
    date_joined: datetime
    ranking: Ranking


class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[UserDegree] = []


class TradeSide(Enum):
    SELL = 'Sell'
    BUY = 'Buy'


class Trade(BaseModel):
    id: int
    trader_id: int
    currency: str = Field(max_length=3)
    side: TradeSide
    price: float = Field(ge=0)
    amount: float = Field(ge=0)


