from modules import check_single_url
import pandas as pd

def main():

	# Load target URLs from the Excel data source
	df = pd.read_excel('data/urls.xlsx')
	urls = df['url']

	# Initialize a container for validation results
	all_result = []

	# Validate each URL and collect the results
	for url in urls:
		result = check_single_url(url)
		all_result.append(result)

	# Display the final validation report
	for result in all_result:
		print(f'URL: {result["url"]} Stauts: {result["status"]} Is_valid: {result["is_valid"]} Error_msg: {result["error_msg"]}')


if __name__ == '__main__':
	main()