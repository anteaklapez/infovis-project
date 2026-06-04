from rcsbapi.data import DataQuery as Query
import json
from pathlib import Path

base = Path(__file__).parent

with open(base / "../data/diseases_config.json") as f:
    diseases = json.load(f)

mutant_ids = [info["mutant_pdb"] for info in diseases.values()]
 
query = Query(
    input_type="entries",
    input_ids=mutant_ids,
    return_data_list=[
        "struct.title",
        "rcsb_accession_info.deposit_date",
        "exptl.method",
        "rcsb_entry_info.resolution_combined",
        "rcsb_primary_citation.pdbx_database_id_PubMed",
        "rcsb_primary_citation.pdbx_database_id_DOI",
        "rcsb_entity_source_organism.ncbi_scientific_name"
    ]
)

return_data = query.exec()
print(json.dumps(return_data, indent=2))

with open(base / "../data/mutant_protein_data.json", "w") as f:
    json.dump(return_data, f, indent=2)

