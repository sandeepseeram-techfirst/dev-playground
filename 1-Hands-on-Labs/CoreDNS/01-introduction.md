### CoreDNS
CoreDNS is a flexible, extensible DNS server written in Go that serves as the default DNS solution for Kubernetes clusters. 

### Plugin Chain Architecture
The entire behavior of CoreDNS is defined in a single configuration file called the Corefile. When a DNS query arrives, it passes through a chain of plugins in order, each performing a specific function.

* Zone plugins — look up names against a zone (list of names → IPs)

* Forwarder plugins — forward queries to upstream DNS servers (e.g., for external domains)

* Cache plugins — cache responses to reduce repeated upstream lookups