import requests
from bs4 import BeautifulSoup
import json
import os
import argparse

def scrape_dblp_page(dblp_url, year):
    """Scrape the DBLP page for a given conference and year."""
    conference = dblp_url.split("/")[-1]
    url = f"{dblp_url}{year}.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    extracted_data = []

    for entry in soup.find_all('li', class_='entry inproceedings'):
        title = entry.find('span', class_='title').get_text(strip=True) if entry.find('span', class_='title') else None
        authors = [author.get_text(strip=True) for author in entry.find_all('span', itemprop='author')]
        link = entry.find('nav', class_='publ').find('a')['href'] if entry.find('nav', class_='publ') else None
        extracted_data.append({'title': title, 'authors': authors, 'venue': conference, 'year': year, 'link': link})

    return extracted_data

def save_to_json(data, filename):
    """Save extracted data to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def save_to_txt(data, filename):
    """Save extracted data to a TXT file."""
    with open(filename, 'w') as f2:
        for paper in data:
            title = paper['title']
            authors = paper['authors']
            link = paper['link']
            write_str = f"{title}\tAuthors: {', '.join(authors)}\tConference: {paper['venue']}_{paper['year']}\tLink: {link}\n"
            f2.write(write_str)


def main(dblp_url, start_year, end_year, output_format, output_filename):
    saved_p = f"{output_filename}.{output_format}"  # Filename based on user input

    all_data = []
    for year in range(start_year, end_year + 1):
        print(f"Scraping data for year {year}")
        data = scrape_dblp_page(dblp_url, year)
        all_data.extend(data)

    if output_format == "json":
        save_to_json(all_data, saved_p)
    else:
        save_to_txt(all_data, saved_p)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DBLP Conference Data Scraper")

    # Define arguments with default values
    parser.add_argument("--dblp_url", default="https://dblp.uni-trier.de/db/conf/sigsoft/fse",
                        help="DBLP URL of the target conference (default: FSE conference)")
    parser.add_argument("--start_year", type=int, default=2020,
                        help="Start year for data scraping (default: 2020)")
    parser.add_argument("--end_year", type=int, default=2023,
                        help="End year for data scraping (default: 2023)")
    parser.add_argument("--output_format", choices=["json", "txt"], default="json",
                        help="Output format (json or txt), default: json")
    parser.add_argument("--output_filename", default="output",
                        help="Name of the output file (without extension), default: 'output'")

    args = parser.parse_args()
    main(args.dblp_url, args.start_year, args.end_year, args.output_format, args.output_filename)