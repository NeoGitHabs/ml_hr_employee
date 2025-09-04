import uvicorn
from fastapi import FastAPI
from model_rf import predict_rf_router


app = FastAPI()
app.include_router(predict_rf_router)



if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
