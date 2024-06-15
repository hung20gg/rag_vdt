# RAG with Vietnamese wiki

This RAG system is built by Nguyen Quang Hung and Thieu Ngoc Mai as the assignment of NLP module at Viettel Digital Talent 2024.

## What we used
- Dataset: Vietnamese wiki 10k
- Model: 
    - For generating synthetic data: `claude-3-sonnet-20240229-v1:0` from AWS Bedrock
    - For embedding: `bkai-foundation-models/vietnamese-bi-encoder`
    - For LLMs: Meta-Llama-3-8B-Instruct, Vistral-7b-chat
    - For RAG: Traditional, Rerank, RAPTOR
    - Rerank: `bge-reranker-v2-m3`

## Addition data
We generate additional synthetic data based on original database from Claude3. 

## Setup
Before running any file, make sure you install the llm library via
```
git clone https://github.com/hung20gg/llm.git
```
And install any necessary library

## Evaluation
For evaluation, we used 4k multiple choices questions generated from Claude3. 
| Model   | Base    | Rerank   | Base + synthetic   |Rerank + Synthetic |RAPTOR  | RAPTOR + synthetic
|--------------|--------------|--------------|--------------|--------------|--------------|--------------|
| Llama-3-8B          | 65.38            | 71.02          |      69.54        |      71.71        |      60.46       |      65.45        |
| Vistral-7B-Chat         | 46.35           | 44.56          |      50.45        |      52.67        |             |              |



