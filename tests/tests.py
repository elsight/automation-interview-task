import requests
import time
import json
import pytest
from playwright.sync_api import Page, expect

# Configure Playwright for Replit environment
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
        "ignore_https_errors": True,
    }

@pytest.fixture(scope="session") 
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": True,
        "args": [
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--disable-gpu",
            "--disable-web-security",
            "--disable-features=VizDisplayCompositor"
        ]
    }

def test_devices():
    url = "http://localhost:8000"

    data = {"name": "test", "ip_address": "192.168.1.1", "active": True}
    r = requests.post(url + "/api/device", json=data)
    time.sleep(2)

    response = requests.get(url + "/api/devices")
    devices = response.json()

    assert len(devices) > 0

    data2 = {"name": "test device 2", "ip_address": "192.168.1.2", "active": True}
    r2 = requests.post(url + "/api/device", json=data2)

    device_id = r2.json()["id"]

    update_data = {"name": "updated device", "ip_address": "192.168.1.3", "active": False}
    requests.put(f"{url}/api/device/{device_id}", json=update_data)

    time.sleep(1)

    search_response = requests.get(f"{url}/api/devices/search?query=updated")
    search_results = search_response.json()

    print(f"Found {len(search_results)} devices")

    delete_response = requests.delete(f"{url}/api/device/{device_id}")

    time.sleep(1)

def test_create_device_validation():
    url = "http://localhost:8000"

    bad_data1 = {"name": ""}
    bad_data2 = {"ip_address": "192.168.1.1"}
    bad_data3 = {"name": "test", "ip_address": "999.999.999.999"}

    r1 = requests.post(url + "/api/device", json=bad_data1)
    r2 = requests.post(url + "/api/device", json=bad_data2)
    r3 = requests.post(url + "/api/device", json=bad_data3)

    print("Test completed")

def test_page_loads_with_playwright(page: Page):
    """Test that the main page loads correctly using Playwright"""
    
    # Navigate to the application
    page.goto("http://localhost:8000")
    
    # Verify the page title
    expect(page).to_have_title("Devices Management System")
    
    # Verify main heading is present
    heading = page.locator("h1")
    expect(heading).to_have_text("Devices Management System")
    
    # Verify the form is present
    form = page.locator("#device-form")
    expect(form).to_be_visible()
    
    # Verify the device table is present
    table = page.locator("#device-table")
    expect(table).to_be_visible()
    
    # Verify search input is present
    search_input = page.locator("#search-input")
    expect(search_input).to_be_visible()
    expect(search_input).to_have_attribute("placeholder", "Search devices by name or IP...")
    
    # Verify form fields are present
    name_input = page.locator('input[name="name"]')
    ip_input = page.locator('input[name="ip_address"]')
    active_checkbox = page.locator('input[name="active"]')
    submit_button = page.locator('button[type="submit"]')
    
    expect(name_input).to_be_visible()
    expect(ip_input).to_be_visible()
    expect(active_checkbox).to_be_visible()
    expect(submit_button).to_be_visible()
    expect(submit_button).to_have_text("Save Device")
