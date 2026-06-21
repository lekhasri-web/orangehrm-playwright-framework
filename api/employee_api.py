from playwright.sync_api import APIRequestContext

class EmployeeAPI:
    def __init__(self, api_request_context: APIRequestContext):
        self.request = api_request_context

    def create_employee(self, first_name: str, last_name: str, employee_id: str):
        """Dispatches a POST request to seed an employee directly into the database."""
        payload = {
            "firstName": first_name,
            "lastName": last_name,
            "employeeId": employee_id
        }
        # OrangeHRM's actual endpoint route structure
        response = self.request.post("/web/index.php/api/v2/pim/employees", data=payload)
        assert response.ok, f"Failed to create employee via API: {response.status}"
        return response.json()