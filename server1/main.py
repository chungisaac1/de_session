from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import requests
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# ✅ 템플릿 경로 설정 (절대 경로로 설정)
TEMPLATES_DIR = Path(__file__).parent / "templates"
templates = Jinja2Templates(directory=TEMPLATES_DIR)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인에서 허용 (보안 강화를 위해 특정 도메인만 허용하는 것이 좋음)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """index.html 페이지를 클라이언트에 제공"""

    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/users")
async def get_users():
    """사용자 정보를 반환하는 API"""
    return {"users": ["Alice", "Bob", "Charlie"]}

@app.get("/get-orders")
async def get_orders_from_server2():
    """서버 2의 /orders API를 호출하여 주문 정보를 가져옴"""

    response = requests.get("http://server2:8001/orders")  # ✅ 올바른 요청 방식
    return response.json()

#app.get("/get-ybig-de-allmembers")
    """단톡방에 있는 DE 멤버 이름 모두 가져오기! """

# fastapi 서버를 하나 더 만들어서 DE 멤버 이름을 모두 작성한뒤 불러오기 
# 주의해야 할 점 여기에서는 가져오기만 해야함 데이터가 이곳에 저장되면 안됨!