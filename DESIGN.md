# DESIGN.md

## Multi-cloud architecture

The Janitor should follow a provider abstraction model.

Core components:
- Scanner Engine
- Cloud Provider Adapters
- Reporting Engine
- Cleanup Engine

Each provider (AWS, GCP, Azure) should implement:
- Resource discovery
- Cost estimation
- Cleanup APIs
- Tag validation

Example structure:

```txt
providers/
 ├── aws/
 ├── gcp/
 └── azure/