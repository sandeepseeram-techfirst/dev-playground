## CubeSandbox

CubeSandbox is an open‑source, high‑performance sandbox platform built by Tencent Cloud to give each AI agent its own hardware‑isolated MicroVM so it can run code, tools, and even browsers safely, fast, and at scale. 

[cubesandbox](https://cubesandbox.com/about-us.html)

## What CubeSandbox is

- CubeSandbox is a production‑grade security sandbox system for serverless computing and secure code execution, now fully open‑sourced under Apache 2.0.  
- It is specifically optimized for AI agents: “Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents,” and has been deployed at scale inside Tencent Cloud’s own serverless and agent platforms.  
- Technically, it is a MicroVM‑based sandbox (its own RustVMM + KVM stack) in the same architectural family as Firecracker, but as a separate implementation you self‑host instead of consuming a closed SaaS.  

## How it works (architecture and mechanics)

At a high level, CubeSandbox is a multi‑component stack that you deploy in your own infra:

- Control plane and API: The stack includes an E2B‑compatible REST API gateway (CubeAPI), cluster orchestrator (CubeMaster), and request router (CubeProxy).  

- Data plane on each node: Per‑node “Cubelet” manages sandbox lifecycle; CubeHypervisor + CubeShim implement the MicroVM runtime on top of KVM, and CubeVS provides eBPF‑based network isolation.  

- Hardware‑level isolation: Each sandbox runs a dedicated guest OS kernel via KVM; there is no shared host kernel like in containers, so a kernel escape in one sandbox does not affect others.  

- Performance profile:  
  - Cold start under ~60 ms in real scenarios via pre‑provisioned pools, snapshot cloning, and lazy EPT loading (P95 ≈ 90 ms at 50 concurrent).  
  - Per‑instance overhead <5 MB RAM using CoW and reflinked disk images, allowing ~2,000 sandboxes on a 96‑vCPU host and large storage savings.  
  - Distributed scheduling + bin‑packing enables 100K+ instances per minute at platform level, with P99 launch latency <200 ms at 100 concurrent on a 96‑vCPU host.  
- Network and security: eBPF‑based fine‑grained egress filtering and a triple‑layer defense architecture aimed at blocking malicious code, data exfiltration, resource abuse, and kernel escapes.  
- Time‑machine style rollback (roadmap): They’ve built millisecond‑level event snapshots so an “undo” of bad agent actions can roll the sandbox back with sub‑hundred‑millisecond latency; this is being prepared for full open‑sourcing.  
From a developer perspective, you mostly interact through familiar SDKs:

- E2B SDK compatibility: It is designed as a drop‑in replacement for existing E2B‑based sandboxes; often you just change an environment variable to point your agent runtime to Cube.  
- OpenAI Agents & tooling: They provide examples wiring OpenAI Agents SDK’s `E2BSandboxClient` to Cube, including a shell agent and a SWE‑bench debugging agent.  
- One‑click deployment: The project ships one‑click scripts for single node and multi‑node clusters, so you don’t need to run Kubernetes to start using it.   

## Real‑world use cases it solves

Here are the main real‑world patterns they highlight (plus the docs’ example projects):

### 1. Safe code execution for AI agents

- Basic “code sandbox” use: Create sandboxes, run arbitrary Python or shell, manipulate files, and enforce network policies from an agent, all via the E2B SDK.  
- Data‑analysis / “Code Interpreter”: Example projects show OpenAI Agents running pandas/matplotlib for data analysis in Cube, with cross‑turn state and automatic image capture similar to a Jupyter‑style Code Interpreter.   
- Problem solved: Run untrusted LLM‑generated code (RAG pipelines, data wrangling, report generation) with strong isolation, no kernel sharing, and fast startup; containers are often too leaky for this threat model.  

### 2. Autonomous software‑engineering agents (SWE‑bench, mini‑SWE‑agent)

- SWE‑bench automation: There is an example integrating `mini-swe-agent` with Cube to perform SWE‑bench coding tasks inside isolated sandboxes, including debugging a Django app.  
- Multi‑model / RL vision: They explicitly position this for RL‑style agent training where many code‑editing trials run concurrently, each in its own sandbox.  
- Problem solved: Safely run large volumes of autonomous coding experiments on real repos without risking the host and without the cold‑start penalty of full VMs.  

### 3. Browser automation in a safe MicroVM

- Browser sandbox: They provide an example that runs headless Chromium inside a MicroVM and controls it via Playwright/CDP.  
- Problem solved: Agents can browse, click, and scrape the web or internal SaaS apps in an isolated environment, mitigating risks from compromised pages or browser exploits. 

### 4. Agentic RL training at extreme concurrency

- Foundation model labs: Tencent cites MiniMax running hundreds of thousands of heterogeneous sandboxes (Linux, Windows, Android) concurrently for Agentic RL training.  
- Benefits: Distributed scheduling and their image acceleration allow 100K+ instance bursts per minute, reducing training wall‑clock time versus container or heavyweight VM approaches.  
- Problem solved: High‑throughput, multi‑environment agent training where environment reset, rollback, and isolation are crucial for safety and correctness.  

### 5. Secure tools for enterprise / regulated workloads

- Private deployment, compliance: Enterprises can deploy Cube entirely within their own infra, keeping all data within their security perimeter and meeting cybersecurity grading requirements.  
- Apache 2.0, vendor‑neutral: Fully open source and commercially friendly; no dependence on foreign cloud providers or hosted sandboxes. 
- Problem solved: Let internal agents execute powerful tools (databases, SaaS APIs, file systems) in regulated environments, while keeping the runtime auditable and on‑prem. 

### 6. Out‑of‑the‑box agent platforms / startups

- For SMBs / agent startups: Designed so you do not need Kubernetes or proprietary infra; one‑click deployment plus E2B/OpenAI SDK integration makes it suitable as the default “code runner” for new agent products.  
- Example integrations: OpenClaw skill integration, where Cube gives the skill an isolated VM to execute code and tools on behalf of agents.  
- Problem solved: Quickly stand up a secure, low‑latency execution layer for your agent app without building a sandbox system from scratch.  

### 7. Benchmarks and ops tooling

- `cube-bench` CLI: They ship a Go‑based benchmarking tool that measures sandbox create/delete latency at configurable concurrency, with a TUI, percentile metrics, and JSON export.  
- Problem solved: SRE/infra teams can characterize performance on their own hardware and feed numbers into capacity planning and autoscaling logic.  
 