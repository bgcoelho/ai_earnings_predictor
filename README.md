# true_earnings_predictor
AI-based solution that reviews financial statements, extracts relevant information, calculates adjusted earnings over 10 years timeline and projects future earnings

Problem statement: Estimation of core earnings, i.e., a firm’s persistent profitability from its core business activities is central to investors’ assessments of economic performance and valuations. Quantifying core earnings requires judgment and integration of information scattered throughout financial disclosures contextualized with general industry knowledge. This has become increasingly difficult as financial disclosures have become more “bloated” and accounting standards have increased non-recurring impacts on GAAP net income.

Solution:
- Collecting/ extracting the 10-K reports
- Chunking the 10-K text using ‘token text splitter’
- Chunk embedding
- Load embedded vector (PineCone index of dimension 1536)
- Retrieve (Similarity search)
- Augment (retrieved chunks) - 4o or 4o mini or Gemini
- Generate responses using LLMs (4o, 40-Mini, Gemini) and project next year earnings using Machine learning algorithms




