from rcsbapi.data import DataQuery as Query
import json
from pathlib import Path

base = Path(__file__).parent

with open(base / "../data/diseases_config.json") as f:
    diseases = json.load(f)

all_ids = []
for category, diseases_in_category in diseases.items():
    for disease_name, info in diseases_in_category.items():
        all_ids.append(info["wildtype_pdb"])
        all_ids.append(info["mutant_pdb"])

def data_query():
    query = Query(
        input_type="entries",
        input_ids=all_ids,
        return_data_list=[
            "struct.title",
            "rcsb_accession_info.deposit_date",
            "exptl.method",
            "rcsb_entry_info.resolution_combined",
            "rcsb_entry_info.deposited_model_count",
            "rcsb_primary_citation.pdbx_database_id_PubMed",
            "rcsb_primary_citation.pdbx_database_id_DOI",
            "polymer_entities.rcsb_entity_source_organism.ncbi_scientific_name" 
        ]
    )
    return query.exec()


if __name__ == "__main__":
    data = data_query()
    print(json.dumps(data, indent=2))