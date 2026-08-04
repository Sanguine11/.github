# .github

## Geopolitical Network Analysis

This repository contains utilities for modeling and analyzing complex geopolitical systems through layered network graphs.

### 668.ant.py

A Python module that builds a multi-layered directed graph representing relationships between geopolitical actors and contexts.

#### Features

- **Layered Architecture**: Organizes nodes into four distinct layers:
  - **Context Layer**: regional_tension, cross_border_trade, migration_flow
  - **State Layer**: government, military_command, intelligence_service
  - **Institution Layer**: humanitarian_agency, regional_block, mediator
  - **Public Layer**: civil_society, media, diaspora_network

- **Relationship Mapping**: Defines directed edges with semantic relationship types:
  - Signal, coordination, intelligence, pressure
  - Aid delivery, diplomatic support, community links

#### Usage

```python
from 668.ant import write_output

# Generate the geopolitical network graph
result = write_output("geopolitical_layers.json")
```

This will create a JSON file with nodes organized by layer and edges representing relationships between actors.

#### Output Format

The generated JSON contains:
- **nodes**: List of actor nodes with id and layer assignment
- **edges**: List of relationships with source, target, and relationship type

#### Encryption

AES 8889

#### Language

Python 100%
