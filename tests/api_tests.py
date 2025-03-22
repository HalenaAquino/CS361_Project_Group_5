import pytest
from api.shodan_integration import fetch_shodan_data
from api.haveibeenpwned_integration import check_email_pwned
from api.virustotal_integration import fetch_virustotal_data

# Test for Shodan
@pytest.fixture
def shodan_data():
    return fetch_shodan_data("8.8.8.8")  # Example IP address

def test_shodan_api_status_code(shodan_data):
    """Test to ensure Shodan API call returns valid data."""
    assert isinstance(shodan_data, dict)
    assert "ip" in shodan_data
    assert "ports" in shodan_data

def test_shodan_ports(shodan_data):
    """Test to verify that the 'ports' field is a list and contains data."""
    assert isinstance(shodan_data["ports"], list)
    assert len(shodan_data["ports"]) > 0

# Test for Have I Been Pwned
@pytest.fixture
def hibp_data():
    return check_email_pwned("test@example.com")  # Example email

def test_hibp_api_status_code(hibp_data):
    """Test to ensure HIBP API call returns valid data."""
    assert isinstance(hibp_data, list)  # Expect a list of breaches
    assert len(hibp_data) >= 0  # Should not be negative
    if len(hibp_data) > 0:
        assert "Title" in hibp_data[0]  # Ensure breach details contain 'Title'

# Test for VirusTotal
@pytest.fixture
def virustotal_data():
    # URL needs to be encoded for VirusTotal API.
    encoded_url = "aHR0cHM6Ly9nb29nbGUuY29t"  # Base64 encoded "https://google.com"
    return fetch_virustotal_data(encoded_url)

def test_virustotal_api_status_code(virustotal_data):
    """Test to ensure VirusTotal API call returns valid data."""
    assert isinstance(virustotal_data, dict)
    assert "data" in virustotal_data
    assert "attributes" in virustotal_data["data"]

def test_virustotal_url_scan(virustotal_data):
    """Test to ensure the URL scan has a 'scan_id'."""
    assert "scan_id" in virustotal_data["data"]["attributes"]
