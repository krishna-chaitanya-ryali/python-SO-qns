            ┌──────────────────────────┐
            │   External Market APIs   │
            │        (JSON)            │
            └─────────────┬────────────┘
                          │
                          ▼
                ┌──────────────────┐
                │  API Ingestion   │
                │ (Async Fetchers) │
                └─────────┬────────┘
                          │
                          ▼
    ┌────────────────────────────────────────┐
    │          Event / Message Bus            │
    │        (Streaming Platform)             │
    └─────────────┬───────────────┬──────────┘
                  │               │
                  │               │
                  ▼               ▼
    ┌──────────────────┐   ┌──────────────────┐
    │ Internal Systems │   │   Batch Ingestor  │
    │   (CSV Feeds)    │──▶│ (Every 5 minutes)│
    └──────────────────┘   └─────────┬────────┘
                                      │
                                      ▼
                         ┌────────────────────────┐
                         │    Raw Data Storage    │
                         │   (Audit / Replay)    │
                         └─────────┬─────────────┘
                                   │
                                   ▼
                  ┌────────────────────────────────┐
                  │ Data Validation & Transformation │
                  │ - Schema checks                  │
                  │ - Data cleaning                  │
                  │ - Standardization                │
                  └─────────┬───────────────┬──────┘
                            │               │
                            │               │
                            ▼               ▼
         ┌────────────────────────┐   ┌────────────────────────┐
         │ Real-time Aggregation  │   │  Curated Data Storage   │
         │ - Avg price / minute   │   │                        │
         │ - Volume per asset     │   └─────────┬──────────────┘
         └─────────┬──────────────┘             │
                   │                              │
                   ▼                              ▼
    ┌──────────────────────────┐     ┌──────────────────────────┐
    │ Fast Query Store          │     │ Historical Analytics     │
    │ (Dashboard Queries)      │     │ (Compliance / ML / BI)  │
    └─────────┬────────────────┘     └─────────┬────────────────┘
              │                                │
              ▼                                ▼
    ┌──────────────────────────┐     ┌──────────────────────────┐
    │ Market Monitoring         │     │ Analytics / ML Systems   │
    │ Dashboards                │     │                          │
    └──────────────────────────┘     └──────────────────────────┘


    ┌──────────────────────────────────────────────────────────┐
    │              Monitoring & Observability                   │
    │ Logs | Metrics | Alerts | Data Quality | SLA Monitoring   │
    └──────────────────────────────────────────────────────────┘
