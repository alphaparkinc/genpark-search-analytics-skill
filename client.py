from typing import Dict, Any, List

class SearchAnalyticsClient:
    def aggregate_metrics(self, search_logs: List[dict]) -> Dict[str, Any]:
        totals = {}
        no_hits = 0
        for entry in search_logs:
            q = entry.get("query", "").strip().lower()
            hits = entry.get("results_count", 0)
            totals[q] = totals.get(q, 0) + 1
            if hits == 0:
                no_hits += 1
        top_queries = sorted(totals.items(), key=lambda x: x[1], reverse=True)[:5]
        return {
            "total_queries_logged": len(search_logs),
            "zero_results_count": no_hits,
            "top_searches": [{"query": k, "count": v} for k, v in top_queries]
        }
