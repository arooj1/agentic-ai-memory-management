# 🤖 Agentic AI Memory Management 

This repository contains a series of Google Colab notebooks converted to use the **Google Gemini API**. These notebooks demonstrate advanced agentic concepts like memory management, custom tool use, and Retrieval-Augmented Generation (RAG) by simulating complex functionalities with standard Python and the Gemini API.

---

## 📊 Agent Logic Infographics

To better visualize the complex processes happening within these agents, a series of infographic-style web pages have been created. Each infographic breaks down a specific workflow, explaining the purpose and logic at each step of the agent's "thought" process.

> All infographics are located in the `documents/` directory.

---

### **🧠 Agent Memory: Process & Purpose**

This infographic explains the fundamental concept of how an agent's memory is structured, processed, and used to inform its actions. It covers the core `memory_blocks` and how they are formatted into a prompt.

**➡️ [View the Agent Memory Infographic](./documents/3-memory.html)**

---

### **🎂 Birthday Agent: Process Flow**

This infographic details a simple but powerful workflow where an agent uses a custom tool (`query_birthday_db`) to access an external data source and answer a user's question. It's a clear example of how agents can be extended with custom capabilities.

**➡️ [View the Birthday Agent Infographic](./documents/5-Orchestrating_agents.html)**

---

### **📚 Agentic RAG: Process Flow**

This infographic breaks down the more advanced concept of Retrieval-Augmented Generation. It shows the end-to-end process of ingesting a PDF, creating a vector database, retrieving relevant information, and using that information to generate a fact-based, context-aware answer.

**➡️ [View the Agentic RAG Infographic](./documents/4-agentic-RAG-memory.html)**

---

### **⚙️ Agent Memory & Tools: Purpose & Flow**

This infographic provides a high-level overview of how an agent uses custom tools to read from and write to its own memory. This enables it to perform complex, stateful tasks like managing a to-do list, demonstrating a more advanced form of agentic behavior.

**➡️ [View the Custom Memory & Tools Infographic](./documents/3-memory.html)**

---

### Reference 
These documents/documents are adapted from https://learn.deeplearning.ai/courses/llms-as-operating-systems-agent-memory/lesson/nfkqk/introduction 