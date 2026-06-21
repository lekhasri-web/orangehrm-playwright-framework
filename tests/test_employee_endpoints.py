from api.employee_api import EmployeeAPI
import uuid

def test_api_employee_creation_payload(employee_api: EmployeeAPI):
    """Validates the exact JSON response structure from the backend system."""
    unique_id = str(uuid.uuid4())[:8]
    
    response_data = employee_api.create_employee("API_Tester", "Component", unique_id)
    
    # Structural assertion of backend values
    assert "data" in response_data
    assert response_data["data"]["firstName"] == "API_Tester"
    assert response_data["data"]["employeeId"] == unique_id