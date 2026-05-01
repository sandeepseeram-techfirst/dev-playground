#### Motor Claims Triage Platform 

- for a fictitious insurer, not a generic chatbot or a giant LLM demo. 

The app should accept a claim submission with structured form data plus attachments, extract the key fields, score fraud/severity, and route the claim to one of three queues: **auto-approve**, **human review**, or **fraud investigation**. 

#### NOTE

A real company would first define the decision policy and the operational queue structure, then wire AI into the points where it adds leverage without removing accountability. 

The customer submits a claim, the intake service stores the payload, the extractor pulls text and structured fields from documents, the scorer generates a risk score, and the orchestrator applies business rules to decide whether the claim is auto-cleared or sent to an adjuster. 

Every step should emit telemetry so operations, compliance, and claims teams can inspect latency, decision rate, and model behavior, which is central to cloud-native observability.

**claims intake + fraud triage**
**claims intake + damage estimation**
**underwriting pre-check + risk scoring**

#### Services 

**1. Claims API (FNOL Intake Service)**

This service is the entry point where the customer or broker submits a **First Notice of Loss (FNOL)**: claim type, policy number, claimant details, loss date, and supporting documents. It exposes REST endpoints to create and query claims, persists structured metadata in a database, and writes uploaded files (forms, PDFs, images) to object/storage backend.

In a real-world cloud‑native system, this service would also handle authentication, basic validation, and emit events/telemetry so downstream services (extractor, scorer, workflow) can react to new claims without tight coupling.

**2. Document Extractor (AI Document Processing Service)**

This service takes raw claim documents (scanned forms, photos, PDFs) and extracts text and key fields, such as vehicle details, damage description, and incident narrative. In practice it would use OCR or text‑extraction models, plus simple NLP, to convert unstructured content into a normalized internal schema for later scoring
