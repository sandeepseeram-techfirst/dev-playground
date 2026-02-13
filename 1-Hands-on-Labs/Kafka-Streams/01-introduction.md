### Kafka Streams
Kafka Streams is a lightweight Java client library built into Apache Kafka for real-time stream processing of data stored in Kafka topics — no separate processing cluster needed. 

### Core Concept
Unlike batch processing, Kafka Streams treats data as a continuous, unbounded flow of records. It represents data using two key abstractions:

1. KStream — an append-only log where each record is treated as an INSERT (new data, preserving history)

2. KTable — a changelog-based snapshot of the latest value per key, similar to a database table

