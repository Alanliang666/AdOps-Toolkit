from modules import check_single_url

def main():
	urls = ["https://www.google.com", "https://www.coogle.com", "https://fake-url-for-testing.com"]

	result = {}
	all_result = []

	for url in urls:
		result = check_single_url(url)
		all_result.append(result)

	for result in all_result:
		print(f'URL: {result["url"]} Stauts: {result["status"]} Is_valid: {result["is_valid"]} Error_msg: {result["error_msg"]}')


if __name__ == '__main__':
	main()