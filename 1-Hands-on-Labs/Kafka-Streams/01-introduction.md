### Kafka Streams
Kafka Streams is a lightweight Java client library built into Apache Kafka for real-time stream processing of data stored in Kafka topics — no separate processing cluster needed. 

### Core Concept
Unlike batch processing, Kafka Streams treats data as a continuous, unbounded flow of records. It represents data using two key abstractions:

1. KStream — an append-only log where each record is treated as an INSERT (new data, preserving history)

2. KTable — a changelog-based snapshot of the latest value per key, similar to a database table

### Architecture

Applications are structured as a processor topology — a DAG of source processors (consuming from Kafka topics), stream processors (transforming data), and sink processors (writing results back to Kafka or external systems).

### Key Capabilities

1. Stateful operations — uses local state stores backed by Kafka changelog topics for aggregations and lookups

Joins — supports stream-stream, stream-table, and table-table joins on real-time data

Windowing — time-based windowing (tumbling, hopping, session windows) for aggregations over time periods

Fault tolerance & scalability — leverages Kafka's partitioning for elasticity; state is replicated via changelog topics

Interactive queries — query the local state stores directly from your application