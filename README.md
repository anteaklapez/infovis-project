# Protein & Disease Dashboard
**Information Visualization — Group 13**

Antea Klapez (12536843) · Jenny Tran (12502821) · Mariia Karnaukh (62106413)

---

## Overview

This interactive dashboard dives into the relationship between protein mutations and disease, with visualization of global prevalence for each disease. The main research question is: *How does a single amino acid mutation alter a protein's 3D shape, and how does disease burden reflect this globally?*

Users can pick a disease category and specific disease to compare wildtype (healthy) and mutant protein structures side by side. Additionally, they can explore global disease burden over time on a choropleth map, and view structural analytics through multiple charts, enabling disease-specific or global overview of statistics.

---

## Setup & Installation

### Python Version
- Python 3.11+

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the dashboard
```bash
streamlit run app/app.py
```

---

## Features

### Disease & Protein Explorer
- **Category and Disease dropdowns** — enables choosing between 5 disease categories (Neurological, Cancers, Metabolic & Endocrine, Cardiovascular, Genetic/Monogenic) covering 15 diseases
- **Disease summary panel** — shows PDB metadata
- **Side-by-side 3D protein viewer** — renders wildtype and mutant structures using `py3Dmol`
- **Choropleth world map** — shows global disease prevalence per 100,000 population with a year slider (data: GBD 2023, 2014-2023)
- **Experimental methods pie chart** — proportions of methods (X-ray, NMR, etc.) used to find out the disease-specific structures of proteins
- **Structural resolution bar chart** — compares resolution (Å) of wildtype vs. mutant, where NMR structures (no resolution value) are handled with an appropriate info message

### Global Dashboard Overview
- **PDB Deposits Over Time** — bar chart of disease-related structures deposited to PDB per year
- **Resolution Histogram** — distribution of resolution quality across all 30 structures

---

## Technologies Used

| Library | Purpose |
|---|---|
| `streamlit` | Interactive UI framework |
| `py3Dmol` | 3D protein structure rendering |
| `rcsbapi` | RCSB PDB Search + Data API client |
| `plotly` | Interactive charts and choropleth map |
| `biopython` | PDB file parsing and cleaning |
| `pandas` | Data manipulation |
| `country_converter` | Country name → ISO-3 code mapping |


---

## Data Mining

Data is fetched programmatically at runtime from two sources.

### RCSB PDB — Search API (`search_api.py`)
Faceted queries are issued via `rcsbapi.search.AttributeQuery` against a pre-made set of
30 PDB entry IDs to retrieve aggregated statistics:

- **Deposits timeline** — `rcsb_accession_info.deposit_date` (date histogram, yearly interval)
- **Resolution histogram** — `rcsb_entry_info.resolution_combined` (histogram, 0.5 Å bins)
- **Experimental methods** — `exptl.method` (terms aggregation)

A disease-specific faceted query is also issued per selected disease using only the wildtype
and mutant PDB IDs to power the per-disease pie chart.

### RCSB PDB — Data API (`data_api.py`)
A structured `DataQuery` fetches per-entry metadata for all disease entries:

- `struct.title`, `rcsb_accession_info.deposit_date`, `exptl.method`
- `rcsb_entry_info.resolution_combined`, `rcsb_entry_info.deposited_model_count`
- `rcsb_primary_citation.pdbx_database_id_PubMed`, `.pdbx_database_id_DOI`
- `polymer_entities.rcsb_entity_source_organism.ncbi_scientific_name`

### RCSB PDB — Structure Files (`protein_download.py`)
`.pdb` files are downloaded from `https://files.rcsb.org/download/{PDB_ID}.pdb` for all wildtype and mutant entries defined in `diseases_config.json`. This is a 
setup step which was only done once during disease search.

### IHME GBD 2023 — Disease Burden Maps
Pre-downloaded CSV files (one per disease) from the GBD Results Tool. Each file contains
prevalence rates per 100,000 people by country and year. This is done due to 
unreliable naming conventions of diseases and proteins, which makes matching per 
disease name impossible.


---

## Data Cleaning

### PDB Structure Files (`pdb_clean.py`)
Cleaned using `BioPython`'s `PDB.PDBIO` with a custom `ChainAFilter`:
- Only *Chain A* is saved, while other chains are removed
- *HETATM records* are excluded (keeps only standard amino acid ATOM records)
- Applied once as a preprocessing step to all downloaded `.pdb` files

### Resolution Data (`resolution_chart.py`)
- `resolution_combined` is returned as a list by the API — the first element is extracted
- `NULL` / `None` values are filtered out before plotting 
- in case of no such data, info card is shown with an appropriate message

### Map Data (`map.py`)
- Country names converted to *ISO-3 codes* using `country_converter`
- Rows where conversion returns `"not found"` are dropped which removes regional aggregates
  like "Sub-Saharan Africa" that are not plottable as countries
- Per-year data is grouped and averaged with `groupby` before rendering the plot

### API Response Parsing (`search_api.py`, `data_api.py`)
- Facet buckets are accessed by name using a `facet_by_name` helper to safely handle
  missing or reordered facets
- `deposit_date` strings are parsed to extract the year only via `pd.to_datetime(...).dt.year`

---

## Data Exploration

With the help of official documentation on DataAPI and SearchAPI in `rcsb-api` library, specific parameters were found and queried to provide information for making the visualizations. In addition to that, as proteins in PDB dataset are not saved in a user-friendly manner, but rather with domain-specific namings, wildtype and mutant proteins had to manually be matched, to ensure appropriate protein visualizations. 

All views are linked through the disease selector and update reactively:

- **Disease dropdowns** (`filters.py`) — navigate the curated disease space by category,
  constraining all downstream views to the selected disease
- **3D protein viewer** (`protein_viewer.py`) — spatial exploration via rotation, zoom,
  and pan (built into `py3Dmol`); secondary structure color-coding (helix / sheet / loop)
  guides structural comparison between wildtype and mutant
- **Choropleth map with year slider** (`map.py`) — temporal exploration of disease
  prevalence across countries; color saturation encodes burden intensity per 100,000
- **Hover tooltips** — available on all Plotly charts and the map for reading exact values
  without cluttering the view
- **Resolution bar chart** (`resolution_chart.py`) — disease-specific comparison of
  structural precision (Å) between wildtype and mutant
- **Global overview charts** (`deposits_chart.py`, `resolution_hist.py`) — allow
  cross-disease pattern recognition across all 30 curated PDB entries

---

## Visual Encoding Summary

| Data | Encoding | Rationale |
|---|---|---|
| Protein secondary structure | Color hue (helix/sheet/loop) | Immediate visual distinction of structural elements |
| Disease prevalence | Choropleth color saturation | Geographic patterns in affected regions |
| Deposits over time | Bar chart (x=year) | Ordered time axis with discrete yearly counts |
| Resolution quality | Bar chart per structure | Direct comparison of wildtype vs. mutant precision |
| Experimental methods | Pie chart | Proportions of a small number of categories |
| Time dimension of map | Year slider | Temporal exploration without clutter |


---


## Data Sources

### RCSB Protein Data Bank
- **Search API** (`rcsbapi.search`) — faceted queries for deposits timeline, resolution histogram, experimental methods pie chart
- **Data API** (`rcsbapi.data`) — per-entry metadata (title, organism, deposition date, resolution, citation)
- **Structure files** — `.pdb` files downloaded from `https://files.rcsb.org/download/{PDB_ID}.pdb`

### IHME Global Burden of Disease (GBD 2023)
Disease prevalence CSV files per country per year, one per disease.

> **Citation:** Global Burden of Disease Collaborative Network. *Global Burden of Disease Study 2023 (GBD 2023) Results.* Seattle, United States: Institute for Health Metrics and Evaluation (IHME), 2024. Available from https://vizhub.healthdata.org/gbd-results/
