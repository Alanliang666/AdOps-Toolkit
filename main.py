from modules import check_single_url
import pandas as pd

def main():

	input_path = 'data/urls.xlsx'
	print(f"Reading data from: {input_path}")

	# Load target URLs from the Excel data source
	try:
		df = pd.read_excel(input_path)
		urls = df['url']
	
	except Exception as e:
		print(f"Error reading Excel file: {e}")
		return

	# Initialize a container for validation results
	all_results = []
	total_urls = len(urls)
	print(f"Found {total_urls} URLs.")

	# Validate each URL and collect the results
	for url in urls:
		result = check_single_url(url)
		all_results.append(result)

	# Output: Save results to a new Excel file
	results_df = pd.DataFrame(all_results)

	output_path = 'data/report.xlsx'

	results_df.to_excel(output_path, index=False)

	print("-" * 30)
	print(f"Done! Report saved to : {output_path}")
	print("-" * 30)

	print(results_df.head())

if __name__ == '__main__':
	main()