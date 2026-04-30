#### Motor Claims Triage Platform 

- for a fictitious insurer, not a generic chatbot or a giant LLM demo. 

The app should accept a claim submission with structured form data plus attachments, extract the key fields, score fraud/severity, and route the claim to one of three queues: **auto-approve**, **human review**, or **fraud investigation**. 

#### NOTE

A real company would first define the decision policy and the operational queue structure, then wire AI into the points where it adds leverage without removing accountability. 

The customer submits a claim, the intake service stores the payload, the extractor pulls text and structured fields from documents, the scorer generates a risk score, and the orchestrator applies business rules to decide whether the claim is auto-cleared or sent to an adjuster. 

Every step should emit telemetry so operations, compliance, and claims teams can inspect latency, decision rate, and model behavior, which is central to cloud-native observability.
