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

### Getting Started

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

