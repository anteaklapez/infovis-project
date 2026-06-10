from rcsbapi.search import AttributeQuery, Facet
import json
import os

disease_ids = ["1IYT", "2BEG",
               "2N0A", "6UFR",
               "6RMH", "6X9O",
               "3COJ", "1N5O",
               "2GS2", "2ITT",
               "2G1T", "3QRJ",
               "1E3G", "2AX8",
               "6Y1A", "6ZRQ",
               "2HIU", "1XW7",
               "1PAH", "1TG2",
               "2MQ0", "2MQ3",
               "1AJJ", "1D2J",
               "1UZJ", "1APJ",
               "2HHB", "2HBS",
               "2C9V", "1MFM"
               ]

def dashboard_query():
    q = AttributeQuery(
        attribute="rcsb_entry_container_identifiers.entry_id",
        operator="in",
        value=disease_ids
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

    # NEW PART
    results_list = list(q_result)
    rows_table = [{"entry_id": entry_id} for entry_id in results_list]
    facets_raw = q_result.facets
    total_count = len(results_list)
    #until here

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

def disease_query(wildtype_id: str, mutant_id: str):
    q = AttributeQuery(
        attribute="rcsb_entry_container_identifiers.entry_id",
        operator="in",
        value=[wildtype_id, mutant_id]
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
    facets_raw = q_result.facets
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

    return {
            "methods_pie": methods_pie,
            }


if __name__ == "__main__":
    print("Query IDs:", disease_ids) 
    out = dashboard_query()
    print("total_count:", out["total_count"])
    print("methods_pie:", out["methods_pie"])
    print("resolution_hist sample:", out["resolution_hist"][:5])
    print("deposits_timeline:", out["deposits_timeline"])
    print("rows:", out["rows"])
    
