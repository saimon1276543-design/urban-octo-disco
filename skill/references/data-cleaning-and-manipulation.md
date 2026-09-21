# Data Cleaning and Manipulation

Use this reference for data cleaning, wrangling, transformation, preprocessing, data quality, dataframe work, ETL/ELT, and downstream ML/search impact.

## Core workflow

Define the downstream use and data contract first. Preserve raw data and provenance. Profile schema, types, units, missingness, duplicates, invalid values, outliers, conflicts, temporal coverage, and sensitive fields. Then transform with explicit, testable, reproducible operations: parsing, type conversion, normalization, filtering, joins, grouping, reshaping, aggregation, entity resolution, deduplication, and temporal alignment.

Distinguish observed, inferred, imputed, synthetic, corrected, and unresolved values. Validate constraints, referential integrity, ranges, distributions, reconciliation, and sample-level review. Record lineage, quality metrics, assumptions, and rollback/reprocessing procedures.

## Domain-specific care

Biomedical and iBCI signals require calibration, synchronization, artifact handling, and scientific validity boundaries. Robotics telemetry requires sensor clocks, calibration, missing intervals, and state-estimation assumptions. OSINT requires provenance, corroboration, uncertainty, entity resolution, and preservation of source context. ML/AI requires leakage prevention, label quality, train/validation/test separation, imbalance handling, and downstream evaluation. Crawl/index pipelines require canonicalization, deduplication, permissions, versions, chunk metadata, and deletion propagation.

For multi-terabyte work, read `references/large-scale-data-engineering.md`. For current library syntax, warehouse features, or regulations, use freshness controls.
