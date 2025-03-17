from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/orders")
async def get_orders():
    """주문 정보를 반환하는 API"""

    return {"orders": ["Order1", "Order2", "Order3"]}
