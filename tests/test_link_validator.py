import pytest
import requests_mock
import requests
from modules.link_validator import check_single_url

# Scenario 1 : The URL returns a successful status code (200-299)
def test_single_url_success():

	url = 'https://fake-url.com'

	with requests_mock.Mocker() as m:
		m.get(url, status_code=200)

		result = check_single_url(url)

		assert result["status"] == 200
		assert result["is_valid"] is True
		assert result["error_msg"] is None


# Scenario 2 : The URL returns a 404 Not Found error
def test_single_url_404():

	url = 'https://404-not-found.con'

	with requests_mock.Mocker() as m:
		m.get(url, status_code=404)

		result = check_single_url(url)

		assert result["status"] == 404
		assert result["is_valid"] is False
		assert result["error_msg"] is None

# Scenario 3: The URL raises a Connection Error (Exception)
def test_single_url_error():

	url = 'https://can-not-connect.com'

	with requests_mock.Mocker() as m:
		m.get(url, exc=requests.exceptions.ConnectionError("Network Down"))

		result = check_single_url(url)

		assert result["is_valid"] is False
		assert result["error_msg"] is not None


