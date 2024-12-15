from abc import ABC, abstractmethod

class AppInfo(ABC):
    def __init__(self):
        self._developers = [
            {"name": "Ovi Shekh", "roll": "1824", "department": "CSE", "batch": "63", "university": "Daffodil Int. University"},
            {"name": "Khalid Anwar", "roll": "1553", "department": "CSE", "batch": "63", "university": "Daffodil Int. University"},
            {"name": "Apra Rani Das", "roll": "1823", "department": "CSE", "batch": "63", "university": "Daffodil Int. University"}
        ]
        self._app_name = "Weather App"
        self._version = "2.0"
        self._team = "Team Tengen"

    def show_app_info(self):
        print("=" * 80)
        print(f"\t {self._app_name}")
        print(f"\t Your Gateway to Real-Time Weather Information")
        print(f"\t Version: {self._version}")
        print(f"\t Developed By: {self._team}")
        print("=" * 80)

    @abstractmethod
    def show_developer_info(self):
        pass

class DevInfo(AppInfo):
    def show_developer_info(self):
        print("\nDeveloper Information:")
        print("*" * 50)
        for dev in self._developers:
            print(f"Name: {dev['name']}")
            print(f"ID: {dev['roll']}")
            print(f"Department: {dev['department']}")
            print(f"Batch: {dev['batch']}")
            print(f"University: {dev['university']}")
            print("-" * 50)
            print(f"Team: {self._team}\n")