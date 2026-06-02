from rcsbapi.data import DataQuery as Query
import json


query = Query(
    input_type="entries",
    input_ids=["4HHB", "3PQR"],
    return_data_list=[
        "struct.title",
        "rcsb_accession_info.deposit_date",
        "rcsb_accession_info.initial_release_date",
        "exptl.method",
        "rcsb_entry_info.resolution_combined",
        "rcsb_primary_citation.pdbx_database_id_PubMed",
        "rcsb_primary_citation.pdbx_database_id_DOI",
        "rcsb_entity_source_organism.ncbi_scientific_name"
    ]
)

return_data = query.exec()
print(json.dumps(return_data, indent=2))


