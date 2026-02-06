import requests

def check_single_url(url, timeout=5):

	result = {
		"url": url,
		"status": None,
		"is_valid": False,
		"error_msg": None
		}
	
	try:
		respones = requests.get(url, timeout=timeout)

		result[status] = respones.status_code

		if 200 <= respones.status_code < 300:
			result[is_valid] = True 

	except Exception as e:
		result["error_msg"] = str(e)

	return result