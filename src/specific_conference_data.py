import json
from semanticscholar import SemanticScholar
import multiprocessing
import argparse

def paper_object_to_json(paper):
    # Converts a Semantic Scholar paper object to a JSON object
    new_json = {}
    # Extracting various attributes from the paper object
    new_json['paperId'] = paper.paperId
    new_json['externalIds'] = paper.externalIds
    new_json['corpusId'] = paper.corpusId
    new_json['url'] = paper.url
    new_json['title'] = paper.title
    new_json['abstract'] = paper.abstract
    new_json['venue'] = {}

    # Adding publication venue details if available
    if paper.publicationVenue is not None:
        new_json['venue'] = {
            'name': paper.publicationVenue.name,
            'id': paper.publicationVenue.id,
            'type': paper.publicationVenue.type,
            'alternate_names': paper.publicationVenue.alternate_names,
            'url': paper.publicationVenue.url
        }
    new_json['year'] = paper.year
    new_json['referenceCount'] = paper.referenceCount
    new_json['citationCount'] = paper.citationCount
    new_json['influentialCitationCount'] = paper.influentialCitationCount
    new_json['isOpenAccess'] = paper.isOpenAccess
    new_json['openAccessPdf'] = paper.openAccessPdf
    new_json['fieldsOfStudy'] = paper.fieldsOfStudy
    new_json['publicationTypes'] = paper.publicationTypes

    # Extracting author details
    new_json['authors'] = [{'authorId': author.authorId, 'name': author.name} for author in paper.authors]

    return new_json

def search_paper(sch, search_func, search_term):
    # Search for a paper based on a search term using Semantic Scholar API
    try:
        results = search_func(search_term)
        if results:
            # Extracts the first result if searching by title, otherwise returns the paper directly
            return paper_object_to_json(results if search_func == sch.get_paper else results[0])
    except Exception as e:
        print(f"Error searching for {search_term}: {e}")
    return None

def process_paper_search(args):
    # Processes individual paper search task
    paper_title, paper_doi, search_method, timeout = args
    # Extracts DOI from the URL if present
    paper_doi = paper_doi.split("org/")[1] if "org/" in paper_doi else paper_doi
    sch = SemanticScholar(timeout=timeout)
    # Selects the appropriate search function based on method
    search_func = sch.get_paper if search_method == "doi" else sch.search_paper
    search_term = paper_doi if search_method == "doi" else paper_title
    return search_paper(sch, search_func, search_term)

def paper_search(previous_json, num_processes, search_method, timeout, output_path):
    # Main function to orchestrate the paper searching process
    with open(previous_json, 'r') as f:
        data = json.load(f)

    # Creating a list of tasks for multiprocessing
    tasks = [(paper["title"], paper["link"], search_method, timeout) for paper in data]

    # Using multiprocessing to process tasks in parallel
    with multiprocessing.Pool(num_processes) as pool:
        results = pool.map(process_paper_search, tasks)

    # Saving the results to a JSON file
    save_to_json(results, output_path)

def save_to_json(data, filename):
    """Save extracted data to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    # Setting up command-line argument parsing
    parser = argparse.ArgumentParser(description="Script to search papers using Semantic Scholar API")
    parser.add_argument("--input", required=True, help="Path to the input JSON file containing paper data")
    parser.add_argument("--output", required=True, help="Path to save the output JSON file")
    parser.add_argument("--processes", type=int, default=30, help="Number of parallel processes to use")
    parser.add_argument("--search_method", choices=["doi", "title"], default="doi", help="Method to search papers (doi or title)")
    parser.add_argument("--timeout", type=int, default=15, help="Timeout for Semantic Scholar API requests in seconds")

    args = parser.parse_args()
    paper_search(args.input, args.processes, args.search_method, args.timeout, args.output)
