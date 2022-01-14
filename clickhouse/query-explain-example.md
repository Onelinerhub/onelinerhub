# Query EXPLAIN example

```sql
-- EXPLAIN SELECT ...

┌─explain───────────────────────────────────────────────────────────────────────────────┐
│ Expression (Projection)                                                               │
│   CreatingSets (Create sets before main query execution)                              │
│     Expression (Before ORDER BY)                                                      │
│       Filter (WHERE)                                                                  │
│         SettingQuotaAndLimits (Set limits and quota after reading from storage)       │
│           ReadFromMergeTree                                                           │
│     CreatingSet (Create set for subquery)                                             │
│       Expression (Projection)                                                         │
│         Limit (preliminary LIMIT (without OFFSET))                                    │
│           Sorting (Sorting for ORDER BY)                                              │
│             Expression (Before ORDER BY)                                              │
│               SettingQuotaAndLimits (Set limits and quota after reading from storage) │
│                 ReadFromMergeTree                                                     │
└───────────────────────────────────────────────────────────────────────────────────────┘
```



