from fastapi import FastAPI
from src.users import router as auth_router
from src.transactions import router as transactions_router
from src.tasks import router as tasks_router
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Счёт расходов и доходов",
    version="0.0.1",
    description="API для управления задачами и транзакциями приходов и расходов",
)

app.include_router(auth_router, prefix="/auth")
app.include_router(transactions_router, prefix="/transactions")
app.include_router(tasks_router, prefix="/tasks")
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
