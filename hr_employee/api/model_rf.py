from fastapi import APIRouter
from db.schema import EmployeeSchema
import joblib
from pathlib import Path



BASE_DIR = Path(__file__).parent

model = joblib.load(BASE_DIR / 'model_rf.pkl')
scaler = joblib.load(BASE_DIR / 'scaler.pkl')


predict_rf_router = APIRouter(prefix='/predict_rf', tags=['Predict_RF'])

@predict_rf_router.post('/')
async def check_rf(data: EmployeeSchema):
    data_dict = dict(data)

    new_job_role = data_dict.pop('JobRole')
    job_role_binary = [
        1 if new_job_role == 'Human Resources' else 0,
        1 if new_job_role == 'Laboratory Technician' else 0,
        1 if new_job_role == 'Manager' else 0,
        1 if new_job_role == 'Manufacturing Director' else 0,
        1 if new_job_role == 'Research Director' else 0,
        1 if new_job_role == 'Research Scientist' else 0,
        1 if new_job_role == 'Sales Executive' else 0,
        1 if new_job_role == 'Sales Representative' else 0]

    new_over_time = data_dict.pop('OverTime')
    over_time_binary = [1 if new_over_time == 'Yes' else 0]

    features = list(data_dict.values()) + job_role_binary + over_time_binary
    scaled = scaler.transform([features])
    prediction = model.predict(scaled)[0]
    return {"Answer: " + 'Yes' if prediction == 1 else 'No'}
