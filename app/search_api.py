import requests
import json

search_url = "https://search.rcsb.org/rcsbsearch/v2/query"

query = {
    "query": {
        "type": "terminal",
        "service": "text",
        "parameters": {
            "operator": "greater",
            "value": "2015-01-01", # 10-years or more ?
            "attribute": "rcsb_accession_info.initial_release_date"
        }
    },                                          
    "request_options": {
        "paginate": {
            "start": 0,                         
            "rows": 25 # how many ids should be returned?
        },
        "facets": [
            {
                "name": "Experimental Method",
                "aggregation_type": "terms",
                "attribute": "exptl.method",    
                "min_interval_population": 1
            },
            {
                "name": "Resolution Combined",
                "aggregation_type": "histogram", 
                "attribute": "rcsb_entry_info.resolution_combined",
                "interval": 0.5                 
            },
            {
                "name": "DepositsPerMonth",
                "aggregation_type": "date_histogram",
                "attribute": "rcsb_accession_info.deposit_date",
                "interval": "year"
            }
        ]
    },
    "return_type": "entry"
}

def facet_by_name(root, name):
    if not isinstance(root, list):
        return None
    for f in root:
        if f.get("name") == name:
            return f
    return None

def get_attr(row, dotted):
    cur = row
    for part in dotted.split("."):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        elif isinstance(cur, list):
            cur = cur[0].get(part) if cur and isinstance(cur[0], dict) else None
            break
        else:
            cur = None
            break
    return cur

def dashboard_query():
    resp = requests.post(search_url, json=query, timeout=60)

    data = resp.json()

    total_count = data.get("total_count", 0)
    result_set = data.get("result_set", [])
    facets_root = data.get("facets", {})

    methods_facet = facet_by_name(facets_root, "Experimental Method")
    methods_pie = [
        (b.get("label"), b.get("population", 0))
        for b in (methods_facet.get("buckets", []) if methods_facet else [])
    ]

    res_facet = facet_by_name(facets_root, "Resolution Combined")
    resolution_hist = [
        ((b.get("label")), b.get("population", 0))
        for b in (res_facet.get("buckets", []) if res_facet else [])
    ]

    month_facet = facet_by_name(facets_root, "DepositsPerMonth")
    deposits_timeline = [
        (b.get("label"), b.get("population", 0))
        for b in (month_facet.get("buckets", []) if month_facet else [])
    ]

    rows_table = []
    for r in result_set:
        rows_table.append({
            "entry_id": r.get("identifier"),
            "score":    r.get("score"),
        })
    
    return {
        "total_count":       total_count,
        "methods_pie":       methods_pie,
        "resolution_hist":   resolution_hist,
        "deposits_timeline": deposits_timeline,
        "rows":              rows_table,
    }

if __name__ == "__main__":
    out = dashboard_query()
    print("total_count:", out["total_count"])
    print("methods_pie sample:", out["methods_pie"][:10])
    print("resolution_hist sample:", out["resolution_hist"][:10])
    print("deposits_timeline sample:", out["deposits_timeline"][:12])
    print("first 5 rows:", out["rows"][:5])
