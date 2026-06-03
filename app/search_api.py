from rcsbapi.search import AttributeQuery, Facet
import json
import os

path = os.path.join(os.path.dirname(__file__), "diseases_config.json")

with open(path) as f:
    diseases_config = json.load(f)

all_ids = []
for disease, info in diseases_config.items():
    all_ids.append(info["wildtype_pdb"])
    all_ids.append(info["mutant_pdb"])

def dashboard_query():
    q = AttributeQuery(
        attribute="rcsb_entry_container_identifiers.entry_id",
        operator="in",
        value=all_ids
    )

    q_result = q(
        facets=[
            Facet(
                name="Experimental Method",
                aggregation_type="terms",
                attribute="exptl.method",
                min_interval_population=1
            ),
            Facet(
                name="Resolution Combined",
                aggregation_type="histogram",
                attribute="rcsb_entry_info.resolution_combined",
                interval=0.5
            ),
            Facet(
                name="DepositsPerYear",
                aggregation_type="date_histogram",
                attribute="rcsb_accession_info.deposit_date",
                interval="year"
            )
        ]
    )
    rows_table = [
        {"entry_id": entry_id}
        for entry_id in list(q_result)
    ]

    facets_raw = q_result.facets
    total_count = len(list(q_result)) 

    def facet_by_name(root, name):
        if not isinstance(root, list):
            return None
        for f in root:
            if f.get("name") == name:
                return f
        return None

    methods_facet = facet_by_name(facets_raw, "Experimental Method")
    methods_pie = [
        (b.get("label"), b.get("population", 0))
        for b in (methods_facet.get("buckets", []) if methods_facet else [])
    ]

    res_facet = facet_by_name(facets_raw, "Resolution Combined")
    resolution_hist = [
        (float(b.get("label")), b.get("population", 0))
        for b in (res_facet.get("buckets", []) if res_facet else [])
    ]

    year_facet = facet_by_name(facets_raw, "DepositsPerYear")
    deposits_timeline = [
        (b.get("label"), b.get("population", 0))
        for b in (year_facet.get("buckets", []) if year_facet else [])
    ]

    return {
        "total_count":       total_count,
        "methods_pie":       methods_pie,
        "resolution_hist":   resolution_hist,
        "deposits_timeline": deposits_timeline,
        "rows":              rows_table,
    }


if __name__ == "__main__":
    print("Query IDs:", all_ids)
    out = dashboard_query()
    print("total_count:", out["total_count"])
    print("methods_pie:", out["methods_pie"])
    print("resolution_hist sample:", out["resolution_hist"][:5])
    print("deposits_timeline:", out["deposits_timeline"])
    print("rows:", out["rows"])