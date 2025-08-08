# Clickhouse

* ClickHouse is an open-source, high-performance column-oriented SQL DBMS optimized for OLAP / analytical queries (large scans, aggregations). It stores columns separately, enabling fast reads of only the columns a query touches.

* It's designed for huge datasets ( trillions of rows ), features vectorized execution, aggressive compression, MergeTree family of table engines (and many variants), replication, and distributed query execution across shards/replicas.  

* On Kubernetes the recommended production approach is to use a ClickHouse Operator (manages StatefulSets, CRDs, replicas, config, Keeper/ZooKeeper, scaling). Altinity/Bitnami/others provide operators/Helm charts to automate this.