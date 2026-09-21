# RAG and Hybrid Retrieval

Use this reference for RAG, Graph RAG, hybrid retrieval, LlamaIndex, embeddings, query rewriting, context engineering, and retrieval evaluation.

## Pipeline

Model retrieval as: authorize corpus → ingest → parse → clean → chunk → enrich metadata → embed/index → retrieve → filter/rerank → assemble context → generate → cite/verify → monitor freshness and deletion.

## Retrieval families

Distinguish lexical/inverted retrieval, dense vector retrieval, hybrid retrieval, graph/knowledge-graph retrieval, SQL or structured retrieval, hierarchical and parent-child retrieval, multi-vector retrieval, time-aware retrieval, query-focused retrieval, agentic retrieval, corrective/self-reflective retrieval, multimodal retrieval, and federated/ensemble retrieval. Choose based on corpus, query type, latency, freshness, provenance, and access controls rather than popularity.

LlamaIndex and similar frameworks can implement document-to-node-to-embedding-to-index flows, but teach the underlying data, ranking, provenance, and evaluation contracts independently of current APIs.

## Query and context engineering

Use query rewriting, decomposition, multi-query expansion, filters, metadata constraints, and search-strategy orchestration only when they improve measured retrieval. Control context budgets through deduplication, compression, ordering, citation anchoring, relevance thresholds, and context offloading. Preserve source IDs and transformation history through every stage.

## Evaluation

Separate parsing, chunking, embedding, retrieval, ranking, context, generation, and verification failures. Track recall, precision, hit rate, MRR, nDCG, coverage, citation correctness, faithfulness, freshness, latency, cost, and access-control correctness. Include adversarial, stale, contradictory, multilingual, and long-context cases.

Graph RAG and project-wide episodic memory require explicit entities, relations, timestamps, provenance, conflict handling, and update/deletion semantics. Retrieved memories and generated answers remain hypotheses until supported by source evidence.
