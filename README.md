# From LLMs to Operating Systems

Inspired by the MemGPT paper and the DeepLearning.AI course, this project explores how to overcome the memory limitations of LLMs by treating them like the **CPU of a traditional operating system**.

### The Problem

Static, one-size-fits-all business rules lead to poor recommendations, customer frustration, and low trust.

### The Goal

To create a stateful AI agent that adapts to customer patterns and events while using a **selective memory** to ensure only authorized data is ever recalled.

---

## 🧠 The Agent Memory Hierarchy

Just like a computer has fast RAM and slow disk storage, an agent has a tiered memory system. The key is to intelligently manage what information is loaded into the LLM's limited "working memory" (the context window).

* **Main Context (RAM):** Fast and limited. This is the LLM's direct context window, holding the system prompt, recent chat history, and critical working memory.
* **External Context (Disk):** Vast but slower. This is a vector database or file system where long-term knowledge (like a PDF handbook) is stored.

---

## 📊 Core Concepts & Infographics

To better visualize the complex processes happening within these agents, a series of infographic-style web pages have been created.

> All infographics are located in the `documents/` directory.

### **Self-Editing Memory**

The core idea of MemGPT: give the LLM the tools to manage its own memory. Instead of us deciding what's important, the agent learns to save critical information itself by calling a `core_memory_save` tool when it encounters new, relevant information.
The core idea of MemGPT: give the LLM the tools to manage its own memory. Instead of us deciding what's important, the agent learns to save critical information itself by calling a `core_memory_save` tool when it encounters new, relevant information.

```plaintext
[User provides new info: "My name is Bob"]
              |
              v
[LLM Reasons: "This is important. I should save it."]
              |
              v
[LLM Calls Tool: core_memory_save(section="human", memory="Name is Bob")]
              |
              v
[Python executes, updating the agent's memory state]
```



* **➡️ [View the Agent Memory Infographic](https://www.google.com/search?q=./documents/3-memory.html)**

### **Agentic RAG**

The agent actively decides when it needs more information and uses a tool to search its external memory. The retrieved information is then "augmented" into the agent's working memory for that turn, allowing it to generate fact-based, context-aware answers.
```
[User asks: "What is the vacation policy?"]
              |
              v
[LLM Reasons: "I need to search the handbook."]
              |
              v
[LLM Calls Tool: archival_memory_search(query="vacation policy")]
              |
              v
[Tool returns relevant passages from the PDF]
              |
              v
[LLM generates an answer based on the new context]
```


* **➡️ [View the Agentic RAG Infographic](https://www.google.com/search?q=./documents/4-agentic-RAG-memory.html)**

### **Multi-Agent Orchestration & Memory Redaction**

When multiple agents share memory, we need a way to control access to sensitive information. **Memory Redaction** is the process where an "Admin" agent with special privileges can view a full document, while a controller automatically redacts confidential data (like names, phone numbers, or addresses) before sharing it with other, restricted agents. This ensures security and compliance in collaborative agent systems.

```
+--------------------------+      +---------------------------+
|   Hiring Manager Agent   |      |   Junior Analyst Agent    |
|      (Admin Rights)      |      |    (Restricted Rights)    |
+--------------------------+      +---------------------------+
              |                                 ^
              v                                 |
[Views Full Document:"John Doe,555-1234"]  [Receives Redacted Doc                                        
"[REDACTED], [REDACTED]"]
              |                                 |
              +----->[Redaction Controller]<----+
```              

* **➡️ [View the Multi-Agent Orchestration Infographic](https://www.google.com/search?q=./documents/5-Orchestrating_agents.html)**

---

## ☁️ GCP Building Blocks & Architecture

This solution is designed to run on Google Cloud Platform, leveraging the following services:

* **BigQuery:** Secure data store with policy tags and row-level access control.
* **Cloud Storage:** Hosts the vector database files.
* **Cloud DLP:** Inspects and de-identifies Personally Identifiable Information (PII).
* **Cloud Run:** Hosts the "Memory Broker" microservice that enforces the selective memory pattern.
* **Vertex AI:** Provides the agent runtime, orchestration, and access to foundation models.

---

## Conclusion

By giving LLMs tools to manage a memory hierarchy, we transform them from simple chatbots into more capable, autonomous agents that can learn, reason, and solve complex, multi-step problems. This is the core idea of treating LLMs like an **operating system for intelligence**.

### References

These documents are adapted from:

* [DeepLearning.AI - LLMs as Operating Systems](https://learn.deeplearning.ai/courses/llms-as-operating-systems-agent-memory/lesson/nfkqk/introduction)
* [MemGPT Paper on arXiv](https://arxiv.org/pdf/2310.08560)
* [MemGPT GitHub Repository](https://github.com/madebywild/MemGPT)