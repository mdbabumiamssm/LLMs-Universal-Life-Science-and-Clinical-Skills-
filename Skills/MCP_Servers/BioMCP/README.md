# BioMCP: Model Context Protocol for Biomedicine

**Source:** [genomoncology/biomcp](https://github.com/genomoncology/biomcp)
**Local Repository:** `./repo`
**Status:** Integrated & Downloaded

## Overview
BioMCP is an implementation of the **Model Context Protocol (MCP)** specifically for biomedical data. It allows any MCP-compliant AI client (like Claude Desktop, LobeChat, or Cursor) to natively "speak" to biomedical databases without custom glue code.

## Connected Data Sources
- **PubMed & PMC:** Literature search and retrieval.
- **ClinicalTrials.gov:** Trial matching and protocol extraction.
- **Genomic Databases:** Variant annotation (dbSNP, ClinVar).
- **PubTator3:** Named entity recognition API.

## Quick Start
1.  **Installation:**
    ```bash
    cd repo
    # Using uv (recommended in repo)
    uv sync
    # Or standard pip
    pip install .
    ```
2.  **Running the Server:**
    You can run the MCP server directly or via Docker (see `repo/docker-compose.yml`).
    ```bash
    cd repo
    make run
    ```
3.  **Client Configuration:**
    Add the server to your MCP client config (e.g., Claude Desktop):
    ```json
    {
      "mcpServers": {
        "biomcp": {
          "command": "python",
          "args": ["-m", "biomcp.server"]
        }
      }
    }
    ```

## Benefits
- **Standardization:** No need to write custom Python wrappers for every API.
- **Interoperability:** Works with any LLM that supports MCP.
- **Real-time:** Fetches the latest paper abstracts and trial statuses.