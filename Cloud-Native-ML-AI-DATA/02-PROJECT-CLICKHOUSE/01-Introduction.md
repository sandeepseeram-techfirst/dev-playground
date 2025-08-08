# Clickhouse

* ClickHouse is an open-source, high-performance column-oriented SQL DBMS optimized for OLAP / analytical queries (large scans, aggregations). It stores columns separately, enabling fast reads of only the columns a query touches.

* It's designed for huge datasets ( trillions of rows ), features vectorized execution, aggressive compression, MergeTree family of table engines (and many variants), replication, and distributed query execution across shards/replicas.  

* On Kubernetes the recommended production approach is to use a ClickHouse Operator (manages StatefulSets, CRDs, replicas, config, Keeper/ZooKeeper, scaling). Altinity/Bitnami/others provide operators/Helm charts to automate this.


### Project Activities 

1. Install the ClickHouse Operator via Helm.

2. Deploy a small ClickHouse cluster with 1 shard × 2 replicas (for learning about replication + distributed queries).

Create MergeTree tables, a Distributed table, and a Materialized View.

Ingest sample data and run OLAP queries (aggregation, filtering).

Expose an external service for SQL clients (or kubectl port-forward).

Add monitoring: ClickHouse metrics exporter → Prometheus → Grafana.

Scale up/down replicas and observe behavior.

Demonstrate backup/snapshot options and cleanup.