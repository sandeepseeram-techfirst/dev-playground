### CoreDNS
CoreDNS is a flexible, extensible DNS server written in Go that serves as the default DNS solution for Kubernetes clusters. 

### Plugin Chain Architecture
The entire behavior of CoreDNS is defined in a single configuration file called the Corefile. When a DNS query arrives, it passes through a chain of plugins in order, each performing a specific function.

* Zone plugins — look up names against a zone (list of names → IPs)

* Forwarder plugins — forward queries to upstream DNS servers (e.g., for external domains)

* Cache plugins — cache responses to reduce repeated upstream lookups 

### How It Works in Kubernetes
CoreDNS runs as a Deployment in the kube-system namespace, with 2 replicas by default for high availability and load balancing. It listens on UDP port 53 and is exposed to cluster workloads via a ClusterIP Service.

When a Pod makes a DNS request (e.g., my-service.default.svc.cluster.local), the flow is:

1. Pod's /etc/resolv.conf points to the CoreDNS Service IP

2. The query hits CoreDNS on port 53

3. The kubernetes plugin intercepts cluster-local domains and resolves them against the Kubernetes API (Services, Pods, EndpointSlices)

4. For external domains (e.g., google.com), the forward plugin proxies the query to an upstream resolver

5. The cache plugin stores the response with a default TTL of 5 seconds

### Key Protocols Supported
CoreDNS supports multiple DNS transport protocols out of the box:

* dns:// — plain DNS (default)

* tls:// — DNS over TLS (DoT, RFC 7858)

* https:// — DNS over HTTPS (DoH, RFC 8484)

* grpc:// — DNS over gRPC 