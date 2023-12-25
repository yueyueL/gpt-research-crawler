# gpt-research

`gpt-research` is an innovative tool designed to crawl research paper data and generate knowledge files, enabling the creation of custom GPT models based on specific conference materials or individual paper PDFs. This tool is particularly useful for researchers, academics, and enthusiasts in the field of AI and Machine Learning.

## Interesting Features

- **Crawler for Conference Data**: Automate the collection of research papers from specified conferences.
- **Custom GPT Creation**: Generate a tailored GPT model using the content extracted from research papers.
- **PDF Content Extraction**: Efficiently extract and process the content of academic papers from their PDF format.

## Example

I have successfully utilized `gpt-research` to create a custom GPT model that incorporates all papers from top Security and Software Engineering conferences. This custom GPT is designed to provide query support for these specific fields.

- **See the Custom GPT in Action**: [SE & SEC Scholar Supportive - Providing inclusive support for SE & SEC research.](https://chat.openai.com/g/g-mPO2BZegm-se-sec-scholar-supportive)
  
This project crawled the relevant documentation and generated a knowledge file, which was then uploaded to create this custom GPT model. You can try it out and explore the potential of integrating a custom GPT into your research endeavors.

> **Note**: Access to this feature might require a paid ChatGPT plan.


### Custom GPT for One research Domain
This repository contains a Python script designed to scrape research paper data from the DBLP database. The script extracts key information about research papers (including venues, titles, links, authors, and years) and saves it in either JSON or text format. This data can be instrumental in creating knowledge files for building domain-specific GPT models, such as a custom GPT for AI or Security domain researchers.

How to Use the Script

1. **Identify Top Venues in Your Domain**: Determine the top venues relevant to your research domain. For instance, in AI, prominent venues might include ICLR, ICML, NeurIPS, and ACL. You can refer to this [link](https://yueyuel.github.io/ReliableLM4Code/docs/venus/) for guidance on selecting top venues.
   
2. **Find DBLP URLs**: Obtain the specific DBLP URLs for your chosen venues. For example, the URL for ICLR is `https://dblp.uni-trier.de/db/conf/iclr/iclr`.

3. **Run the Script**: Use the script to collect data from the DBLP database for your selected venues and years. The script is designed to be user-friendly, allowing for command-line input of parameters such as the DBLP URL, start and end years, output format, and output file name.

```bash
python conference_crawler_dblp.py [--dblp_url <dblp_url>] [--start_year <start_year>] [--end_year <end_year>] [--output_format <output_format>] [--output_filename <output_filename>]
```

For example, to scrape data from ICLR from 2015 to 2023 and save it in TXT format with a custom file name:

```bash
python conference_crawler_dblp.py --dblp_url https://dblp.uni-trier.de/db/conf/iclr/iclr --start_year 2015 --end_year 2023 --output_format txt --output_filename iclr_data
```


### Custom GPT for One Research Topic

This repository contains a Python script for scraping research paper data from Semantic Scholar. It focuses on collecting relevant papers based on specified keywords, including details like paper title, abstract, authors, citation count, and more. This script can be particularly useful for constructing a knowledge base to build a custom GPT model for a specific research domain.

1. **Identify All Relevant Keywords**: Determine the relevant keywords that define your research topic. These keywords will be used to search for related papers on Semantic Scholar.

2. **Run the Script**: Use the script to collect data from [Semantic Scholar](https://www.semanticscholar.org/). The script allows for command-line arguments to customize your search. 


```bash
python topic_crawler.py [--keywords <keyword1 keyword2 ...>] [--output_format <json/txt>] [--output_filename <filename>]
```

For example, to scrape data for papers related to "chatgpt" and "gpt-4" and save the results in a JSON file named 'ai_research.json', use the following command:
```bash
python topic_crawler.py --keywords "chatgpt" "gpt-4" --output_format json --output_filename gpt_research
```


#### Upload Your Data to OpenAI

The crawl process generates a file named `output.json` at the root of this project. This file can be uploaded to OpenAI to create your custom assistant or GPT model.

#### Steps to Create a Custom GPT

1. Visit [OpenAI Chat](https://chat.openai.com/).
2. Click your profile name in the bottom left corner.
3. Select "My GPTs" from the menu.
4. Click on "Create a GPT".
5. Proceed to "Configure".
6. Under "Knowledge", choose "Upload a file" and upload your generated file.
7. In case of a file size error, consider splitting the file into multiple parts using the `maxFileSize` option in the `config.ts` file. Alternatively, use tokenization to reduce the file size with the `maxTokens` option in the same file.

> **Note**: A paid ChatGPT plan may be necessary to create and use custom GPT models at this time.

