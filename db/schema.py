from pydantic import BaseModel, Field
from typing import Literal


class EmployeeSchema(BaseModel):
    Age: int = Field(..., ge=18, le=60)
    BusinessTravel: Literal['Travel_Rarely', 'Travel_Frequently', 'Non-Travel']
    DailyRate: int = Field(..., ge=1, le=9999)
    Department: Literal['Sales', 'Research & Development']
    DistanceFromHome: int = Field(..., ge=1, le=99)
    Education: int = Field(..., ge=1, le=9)
    EducationField: Literal['Life Sciences', 'Marketing', 'Medical', 'Other', 'Technical Degree']
    EnvironmentSatisfaction: int = Field(..., ge=1, le=9)
    Gender: Literal['Female', 'Male']
    HourlyRate: int = Field(..., ge=1, le=100)
    JobInvolvement: int = Field(..., ge=1, le=9)
    JobLevel: int = Field(..., ge=1, le=9)
    JobRole: Literal['Human Resources', 'Laboratory Technician', 'Manager', 'Manufacturing Director', 'Research Director', 'Research Scientist', 'Sales Executive', 'Sales Representative']
    JobSatisfaction: int = Field(..., ge=1, le=9)
    MaritalStatus: Literal['Single', 'Married']
    MonthlyIncome: int = Field(..., ge=1, le=99999)
    MonthlyRate: int = Field(..., ge=1, le=99999)
    NumCompaniesWorked: int = Field(..., ge=0, le=99)
    OverTime: Literal['Yes', 'No']
    PercentSalaryHike:int =  Field(..., ge=1, le=99)
    PerformanceRating: int = Field(..., ge=1, le=9)
    RelationshipSatisfaction: int = Field(..., ge=1, le=9)
    StockOptionLevel: int = Field(..., ge=0, le=9)
    TotalWorkingYears: int = Field(..., ge=0, le=99)
    TrainingTimesLastYear: int = Field(..., ge=0, le=9)
    WorkLifeBalance: int = Field(..., ge=1, le=9)
    YearsAtCompany: int = Field(..., ge=0, le=99)
    YearsInCurrentRole: int = Field(..., ge=0, le=99)
    YearsSinceLastPromotion: int = Field(..., ge=0, le=99)
    YearsWithCurrManager: int = Field(..., ge=0, le=99)

    class Config:
        from_attributes = True
