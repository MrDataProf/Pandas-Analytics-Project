#pip install requests beautifulsoup4


import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url):
    # Step 1: Fetch the HTML content of the Wikipedia page
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return

    # Step 2: Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Step 3: Identify the HTML elements containing the data
    # You need to inspect the HTML structure of the page to find the appropriate tags and classes

    # Example: Assuming the data is in a table with class 'wikitable'
    table = soup.find('table', {'class': 'wikitable'})

    if not table:
        print("Table not found on the page.")
        return

    # Step 4: Extract data from the identified elements
    for row in table.find_all('tr')[1:]:  # Skip the header row
        columns = row.find_all('td')

        # Extracting data from columns (modify as per actual HTML structure)
        rank = columns[0].text.strip()
        company_name = columns[1].text.strip()
        industry = columns[2].text.strip()
        revenue = columns[3].text.strip()
        revenue_growth = columns[4].text.strip()
        headquarters = columns[5].text.strip()

        # Process the extracted data (you can print or store it as needed)
        print(f"Rank: {rank}")
        print(f"Company Name: {company_name}")
        print(f"Industry: {industry}")
        print(f"Revenue: {revenue}")
        print(f"Revenue Growth: {revenue_growth}")
        print(f"Headquarters: {headquarters}")
        print("\n")

# Example usage
wikipedia_url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
scrape_wikipedia(wikipedia_url)
