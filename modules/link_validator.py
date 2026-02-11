import requests

def check_single_url(url: str, timeout: int = 5) -> dict:
	"""
	Validates the URL, records its status code and error message,
	and returns the results in a dictionary.
	"""
	result = {
		"url": url,
		"status": None,
		"is_valid": False,
		"error_msg": None
		}
	
	try:
		response = requests.get(url, timeout=timeout)

		result['status'] = response.status_code

		if 200 <= response.status_code < 300:
			result['is_valid'] = True

	except Exception as e:
		result["error_msg"] = str(e)

	return result