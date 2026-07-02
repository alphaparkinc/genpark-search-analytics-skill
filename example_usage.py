from client import SearchAnalyticsClient
def main():
    c = SearchAnalyticsClient()
    print(c.aggregate_metrics([
        {"query": "headphones", "results_count": 12},
        {"query": "headphones", "results_count": 12},
        {"query": "broken wallet", "results_count": 0}
    ]))
if __name__ == '__main__':
    main()
