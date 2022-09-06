from prometheus_client import Counter

demoApiRequestCounter = Counter("demo_api_request", "demo接口请求统计", labelnames=("api",))
