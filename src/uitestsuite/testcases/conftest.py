import os
import platform
import pytest

def pytest_collection_modifyitems(items):
    """Modifies test items in place to ensure test classes run in a given order."""
    CLASS_ORDER = ["TestLogin", "TestOrg", "TestDataspace", "TestProjectList", "TestFileUpload"]
    #CLASS_ORDER = ["TestLogin", "TestOrg", "TestDataspace"]
    class_mapping = {item: item.cls.__name__ for item in items if hasattr(item, 'cls')}

    sorted_items = []
    for class_ in CLASS_ORDER:
        sorted_items.extend([item for item in items if class_mapping.get(item) == class_])

    # Update the items list to only include sorted items
    items[:] = sorted_items

def pytest_configure():
    """Creates an environment.properties file for Allure reports."""
    allure_dir = "allure-results"  # Folder where Allure stores results
    os.makedirs(allure_dir, exist_ok=True)
    
    with open(os.path.join(allure_dir, "environment.properties"), "w") as f:
        f.write(f"Browser=Chrome\n")  # Change if using another browser
        f.write(f"Browser.Version=120.0\n")  # Browser version
        f.write(f"OS={platform.system()} {platform.release()}\n")  # Auto-detect OS
        f.write(f"Python.Version={platform.python_version()}\n")  # Auto-detect Python version
        f.write(f"Tester=Sriganesh\n")  # Tester name
