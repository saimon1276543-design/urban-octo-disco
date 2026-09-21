# Domain Registry and Ontology

Use this reference to prevent category collapse when the learner names many large domains. A registry is an index of domain families and relationships; it is not a giant list of topics.

## Registry fields

| Field | Purpose |
|---|---|
| Domain ID | Stable identifier such as D-MED, D-IBCI, D-FS, D-ROB |
| Canonical name | Normalized family name while preserving the learner’s wording |
| Capability outcome | What the learner should be able to do |
| Subdisciplines | Major internal branches, not every leaf |
| Target level | Branch-specific depth and independence |
| Entry evidence | Diagnostic or existing artifact |
| Irreducible foundations | Prerequisites that cannot be replaced by shared foundations |
| Shared foundations | Reusable nodes linked by stable IDs |
| Bridge competencies | Cross-domain capabilities |
| Evidence artifacts | Performances, projects, exams, analyses, or demonstrations |
| Volatility class | Durable, medium-term, or volatile |
| Safety/authorization | Boundaries that affect learning or practice |
| Route state | Primary, supporting, parallel, deferred, exploratory, retired |

## Normalization rules

Preserve original labels in the coverage ledger, then normalize synonyms only when the meaning is equivalent. Separate a field or technology from the capability it supports. Separate a degree, license, certification, or regulated curriculum from informal self-study. A named “domain” may contain several distinct families; split it when its prerequisites, evidence, safety, or target outcomes differ.

## Example normalization

- **MBBS:** foundational biomedical sciences, anatomy, physiology, pathology, pharmacology, clinical reasoning, systems-based medicine, communication, ethics, clinical skills, supervised practice, and formal assessment/authorization boundaries. Do not represent it as a casual checklist or imply that an informal roadmap substitutes for medical school or licensure.
- **iBCI:** neuroscience, neurophysiology, neural signal acquisition, hardware/electronics, signal processing, machine learning, decoding, human-computer interaction, experimental design, ethics, and current research practice.
- **BCI and neurotechnology:** neuroscience, neurological function, neural measurement, EEG/ECoG/intracortical and peripheral modalities, signal processing, decoding, adaptive control, human factors, accessibility, neurorehabilitation, ethics, and translation. Keep clinical diagnosis and device authorization separate.
- **Neurology:** neuroanatomy, localization, neurologic examination concepts, motor/sensory/cognitive systems, disease families, diagnostic reasoning, investigations, rehabilitation, and supervised clinical practice. Do not reduce it to a list of diseases or imply that self-study authorizes patient care.
- **Full-stack development:** programming, data structures, web protocols, frontend, backend, databases, testing, security, deployment, observability, product requirements, and maintainable project evidence.
- **Robotics:** mechanics, electronics, embedded programming, sensing, estimation, control, planning, perception, simulation, safety, and system integration.

Additional stable families include **D-DATA** for data cleaning, manipulation, quality, provenance, and large-scale processing; **D-LLM** for ML/AI, LLM training, inference, evaluation, and model-behavior research; **D-RAG** for retrieval, indexing, embeddings, Graph RAG, and context engineering; **D-AGENT** for agent loops, orchestration, memory, parallel calls, sandboxes, and agent-to-agent protocols; **D-MCP** for MCP server and URL hosting; **D-CRAWL** for authorized crawling, browser automation, parsing, storage, indexing, and ranking; **D-FULLSTACK** for frontend/backend/API/database/network systems; **D-INFRA** for Linux, virtualization, containers, GPU/CUDA, DevOps, and MLOps; and **D-OSINT** for lawful open-source intelligence and evidence analysis.

Use separate entries for **D-JSON** (structured data and schemas), **D-REGEX** (regular expressions and parser selection), **D-DB** (advanced databases), **D-API** (API creation and integration), and **D-NET** (computer networking) when their prerequisites or evidence differ. Link them to shared foundations rather than collapsing every software topic into full-stack development.

Use **D-BCI** for general brain-computer-interface and neurotechnology foundations and **D-NEURO** for neurology and neurological reasoning. Link them to **D-IBCI**, medical education, signal processing, ML/AI, robotics, electrochemistry/materials, human factors, and ethics, but preserve independent evidence and safety boundaries.

Use **D-DEVTOOLS** for Chrome DevTools interface literacy, CDP domains, browser network debugging, request/response interception, HAR replay, storage/security inspection, performance/memory diagnostics, streaming protocols, and automation observability. Link it to **D-CRAWL**, **D-FULLSTACK**, **D-API**, **D-NET**, **D-INFRA**, and browser-agent routes without treating a debugging trace as proof of secure production operation.

These are architecture examples, not exhaustive curricula. Use current authoritative sources when the learner asks for a current professional or regulated route.
