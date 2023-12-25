import requests
from bs4 import BeautifulSoup
import json
import os
import argparse
from semanticscholar import SemanticScholar

def semanticscholar_crawler_by_topics( search_keyworks, timeout=10, limit = 3):
    sch = SemanticScholar(timeout=timeout)
    search_results = []
    for keyword in search_keyworks:
        results = sch.search_paper(keyword, limit=limit)
        count = 0
        for item in results:
            item_json = paper_object_to_json(item)
            search_results.append(item_json)
            count += 1
            if not count < limit:
                break
    return search_results


def paper_object_to_json(paper):
    new_json = {}
    new_json['paperId'] = paper.paperId
    new_json['externalIds'] = paper.externalIds
    new_json['corpusId'] = paper.corpusId
    new_json['url'] = paper.url
    new_json['title'] = paper.title
    new_json['abstract'] = paper.abstract
    new_json['venue'] = {}

    if paper.publicationVenue is not None:
        new_json['venue']['name'] = paper.publicationVenue.name
        new_json['venue']['id'] = paper.publicationVenue.id
        new_json['venue']['type'] = paper.publicationVenue.type
        new_json['venue']['alternate_names'] = paper.publicationVenue.alternate_names
        new_json['venue']['url'] = paper.publicationVenue.url
    new_json['year'] = paper.year
    new_json['referenceCount'] = paper.referenceCount
    new_json['citationCount'] = paper.citationCount
    new_json['influentialCitationCount'] = paper.influentialCitationCount
    new_json['isOpenAccess'] = paper.isOpenAccess
    new_json['openAccessPdf'] = paper.openAccessPdf
    new_json['fieldsOfStudy'] = paper.fieldsOfStudy
    new_json['publicationTypes'] = paper.publicationTypes
    new_json['authors'] = []
    for author in paper.authors:
        new_json['authors'].append({'authorId': author.authorId, 'name': author.name})

    return new_json


def save_to_json(data, filename):
    """Save extracted data to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def save_to_txt(data, filename):
    """Save extracted data to a TXT file."""
    with open(filename, 'w') as f2:
        for paper in data:
            title = paper['title']
            venue_name = paper['venue'].get('name', 'N/A')
            year = paper.get('year', 'N/A')
            abstract = paper.get('abstract', 'N/A')
            citecount = paper.get('citationCount', 0)
            authors = ', '.join([author['name'] for author in paper.get('authors', [])])
            openaccesspdf = paper.get('openAccessPdf', 'N/A')

            f2.write(f"Title: {title}\nVenue: {venue_name}\nYear: {year}\nAbstract: {abstract}\nCitation Count: {citecount}\nAuthors: {authors}\nOpen Access PDF: {openaccesspdf}\n\n")


def main(keywords, output_format, output_filename):
    search_results = semanticscholar_crawler_by_topics(keywords)
    if output_format == "json":
        save_to_json(search_results, f"{output_filename}.json")
    else:
        save_to_txt(search_results, f"{output_filename}.txt")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Semantic Scholar Research Paper Crawler")
    parser.add_argument("--keywords", nargs="+", default=["ChatGPT"],
                        help="List of keywords for paper search")
    parser.add_argument("--output_format", choices=["json", "txt"], default="json",
                        help="Output format (json or txt)")
    parser.add_argument("--output_filename", default="semantic_scholar_results",
                        help="Base name for the output file")

    args = parser.parse_args()
    main(args.keywords, args.output_format, args.output_filename)