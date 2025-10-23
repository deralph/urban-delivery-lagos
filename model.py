from pydantic import BaseModel

class RouteRequest(BaseModel):
    source: str
    destination: str
    deadline: str

class RoutePlan(BaseModel):
    mode: str
    estimated_time: float
    cost: float
    path: list

class StatusUpdate(BaseModel):
    status: str
    timestamp: str
