# CLAUDE.md: agentic-ai-memory-management

Project context and decisions for anyone (human or Claude) working in this repo.

## What this is

Arooj Qureshi's exploration of the MemGPT paper (Packer et al., UC Berkeley, 2023, arXiv 2310.08560): Jupyter notebooks that rebuild MemGPT's memory ideas from scratch on Gemini with plain `google-generativeai` and function calling. There's no MemGPT/Letta framework dependency. The notebooks adapt the DeepLearning.AI course "LLMs as Operating Systems: Agent Memory".

Notebooks 1–6 cover: self-editing core memory (`core_memory_save`), memory blocks and agent state with a task queue, agentic RAG over `handbook.pdf` (`archival_memory_search`), multi-agent orchestration (résumé screening and round-robin groups), an all-in-one notebook, and memory redaction by security level.

## Decisions

- **README follows the "Sketch Bold" personal brand** (Arooj's LinkedIn design system): dark images, one highlighted phrase, a handwritten note, mono labels, sentence-case headings, no emoji in headings, and one everyday analogy carried through (desk = context window/RAM, filing cabinet = external memory/disk). Images live in `assets/` (`banner.png`, `diagram.png`) and are rendered from HTML at 2x. Regenerate them rather than editing the PNGs.
- **Voice:** practitioner first, honest about limits. The regex redaction failure in notebook 6 ("[REDACTED] Doe is a strong hire.") is kept on purpose as a lesson: regex isn't redaction.
- **No employer internals.** Examples stay generic and all sample data is synthetic.
- **Secrets:** `helper.py` reads `GEMINI_API_KEY` / `OPENAI_API_KEY` from the environment. Never commit keys.
- **GCP section** in the README is a production design sketch (BigQuery, Cloud Storage, Sensitive Data Protection, formerly Cloud DLP, Cloud Run, Vertex AI). It is not built here.
- **References:** the official MemGPT project is now `letta-ai/letta`. Earlier README links to `madebywild/MemGPT` and Google-search URLs were wrong and have been fixed.
- Notebook 6 was renamed from `6-Memory_Redactment_based-on_SecurityLevel.ipynb` to `6-Memory_Redaction_by_Security_Level.ipynb`.
- The repo is linked from Arooj's LinkedIn carousel "MemGPT, explored" (planned for Dec 3, 2026).

## Known limits

- The notebooks target `gemini-1.5-flash`. Swap `model_name` if that model is unavailable.
- The `documents/*.html` infographics load Tailwind from a CDN and don't render on GitHub. The PDF overview does.
