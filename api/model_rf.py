from fastapi import APIRouter
from db.schema import EmployeeSchema
import joblib


model = joblib.load('model_rf.pkl')
scaler = joblib.load('scaler.pkl')

predict_rf_router = APIRouter(prefix='/predict_rf', tags=['Predict_RF'])

@predict_rf_router.post('/', response_model=EmployeeSchema)
async def check_rf(data: EmployeeSchema):
    data_dict = dict(data)

    new_bus_travel = data_dict.pop('BusinessTravel')
    bus_travel_binary = [
        1 if new_bus_travel == 'Travel_Rarely' else 0,
        1 if new_bus_travel == 'Travel_Frequently' else 0]

    new_department = data_dict.pop('Department')
    department_binary = [
        1 if new_department == 'Sales' else 0,
        1 if new_department == 'Research & Development' else 0]

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

    new_education_field = data_dict.pop('EducationField')
    education_field_binary = [
        1 if new_education_field == 'Life Sciences' else 0,
        1 if new_education_field == 'Marketing' else 0,
        1 if new_education_field == 'Medical' else 0,
        1 if new_education_field == 'Other' else 0,
        1 if new_education_field == 'Technical Degree' else 0]

    new_marital_status = data_dict.pop('MaritalStatus')
    marital_status_binary = [
        1 if new_marital_status == 'Married' else 0,
        1 if new_marital_status == 'Single' else 0]

    new_gender = data_dict.pop('Gender')
    gender_binary = [1 if new_gender == 'Male' else 0]

    new_over_time = data_dict.pop('OverTime')
    over_time_binary = [1 if new_over_time == 'Yes' else 0]


    features = list(data_dict.values()) + bus_travel_binary + department_binary + job_role_binary + education_field_binary + marital_status_binary + gender_binary + over_time_binary
    scaled = scaler.transform([features])
    prediction = model.predict(scaled)[0]
    return {'Answer': 'Yes' if prediction == 1 else 'No'}
