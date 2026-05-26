# Project Brief for AI Agents
This repo is the canonical knowledge base for NeuralSeek — an LLM-agnostic AI orchestration platform for regulated enterprises. It contains product reference, client deployments, sales and positioning insights, partnership materials, and brand assets.
## ⚠ CRITICAL: Brand Compliance for Any Visual Output
Before generating any HTML, slide, mockup, social card, dashboard, or image:
1. Read [BRAND_RULES.md](BRAND_RULES.md) for the full CSS and forbidden patterns.
2. Read [2026_images/neuralseek-brand-guidelines_2026.md](2026_images/neuralseek-brand-guidelines_2026.md) for the complete brand system.
**Mandatory canvas:** Body background must be `#131316` (near-black) with five overlapping radial-gradient ellipses in `#301E4C` (regal purple).
**Forbidden anti-patterns:** Dots, grids, mesh, noise, particles, stripes, circuit-board patterns, "AI hex" patterns, or any tiled / repeated pattern.
## Recommended Reading Order for First-Time Sessions
1. `llms.txt` — full repo index optimized for AI agents
2. `BRAND_RULES.md` — visual compliance rules
3. `README.md` — human-oriented overview
4. The subdirectory relevant to the task:
   - `NeuralSeek Knowledge/Features/` — product reference
   - `NeuralSeek Knowledge/Client Stories/` — case studies
   - `NeuralSeek Knowledge/Knowledge from Calls/` — sales and positioning insights
   - `NeuralSeek Knowledge/Talk Tracks/` — quotable lines and selling angles
Markdown is canonical. PDF / DOCX / PPTX live in `source/` subfolders for fallback only.

---

## Claude Code–specific guidance

This section applies when the agent is **Claude Code** (the Anthropic CLI). Other AI agents should read [AGENTS.md](AGENTS.md) instead.

### What this repo actually is (so you don't treat it like a code project)

- **Not a codebase.** No build, no tests, no dependencies. The "product" is well-organized markdown that AI tools retrieve to answer questions about NeuralSeek, generate pitch material, and produce branded outputs.
- **Single writer model.** Lawrence (`lawrence-spec`) is the only user with push access to `main` (enforced via branch protection). Other org members can clone, read, open issues, and submit PRs — but cannot push directly.
- **Public repo.** Anything committed becomes world-readable. No secrets, no unredacted customer call transcripts (those live at `~/Desktop/NeuralSeek_Private_Backup/` outside the repo), no personally-identifying info about non-public people.

### Common task patterns you'll be asked to run

| Task type | Pattern |
|---|---|
| **Add a new folder of files** | 1) Create folder under `NeuralSeek Knowledge/` 2) Copy files 3) Write `00-INDEX.md` (when-to-use table + cross-refs) 4) Add row in `README.md` folder map 5) Add section in `llms.txt` with per-file routing descriptions 6) Commit with a descriptive multi-line message. See the `Talk Tracks` / `ROI_Analysis` / `Marketing Alignment Pack` commits as templates. |
| **Add a single file to an existing folder** | Drop in the right folder. Add an `llms.txt` entry only if it's significant content; small additions don't need indexing. |
| **Convert a DOCX/PDF/PPTX to markdown** | `pandoc -f docx -t gfm --extract-media=…` for DOCX, `pdftotext -layout` for PDF. Then add YAML frontmatter (`title`, `summary`, `tags`, `source`). Move the original into a `source/` subfolder. |
| **Anonymize identifying content** | Use a Python script for ordered find/replace (most-specific patterns first, broad ones last). Verify with `grep -r -n -i "<identifying tokens>"`. Preserve the lessons; remove the identifiers. See the YourAI commit (`4cc1e84`) as a template. |
| **Drop in user-shared images from chat** | Images pasted into Claude Code live in the conversation transcript as base64, not on disk. Extract via Python parsing the `.jsonl` transcript, verify by reading each extracted file back, then save to the target folder with descriptive names. See the Hackathon Photos / Product Screenshots commits as templates. |
| **Update brand-discoverability surfaces** | Always update `BRAND_RULES.md` + `2026_images/neuralseek-brand-guidelines_2026.md` + `llms.txt` + `README.md` + the in-body HTML aside together. The redundancy is the point. |

### Tool preferences (Claude Code conventions)

- **Reading files:** use `Read`, not `cat` / `head` / `tail` via Bash.
- **Editing files:** use `Edit`, not `sed` via Bash. Use `Write` only for new files or full rewrites.
- **Exploring "where is X":** delegate to the `Explore` agent for breadth searches across the repo.
- **Multi-step work (3+ discrete tasks):** open a `TodoWrite` list. Mark items `in_progress` as you start them, `completed` immediately when done. Don't batch the updates.
- **Background work:** use `run_in_background` for long-running operations (e.g., bulk file conversions). The harness notifies on completion — don't poll.
- **Independent operations:** batch them in a single message with multiple tool calls in parallel (e.g., reading 4 files at once, running git status + git diff + git log together).

### Commit conventions for this repo

- **Never commit unless explicitly asked.** "Add this folder and update the index" implies commit; ambiguous requests don't.
- **Never push to `main` unless explicitly asked.** Local commits are reversible; pushes to the public repo are not.
- **Commit message style:** short imperative subject line (under 80 chars), blank line, then a body that explains the *why* and lists material changes. Multi-line bodies should use a HEREDOC to preserve formatting. Recent commits in `git log` are the style reference.
- **`Co-Authored-By` trailer:** include it on commits per Claude Code defaults.
- **No `--amend` and no `--force` to `main`** without explicit permission. If a commit needs revision, prefer a new commit on top.
- **`git filter-repo` for history rewrites** (e.g., scrubbing accidentally-committed sensitive content) is reasonable but always confirm with Lawrence before force-pushing.

### Things to never do without checking first

- **Don't add dot-grids, mesh, noise, or any tiled pattern to any generated visual.** Ever. See `BRAND_RULES.md` for the full anti-pattern list and the format-specific guidance.
- **Don't modify Lawrence's wording in his original files** (Talk Tracks, ROI Analysis, Marketing Alignment Pack, Knowledge from Calls). Copy them as-authored. Add indexes and routing around them, not edits inside them.
- **Don't add YAML frontmatter to files Lawrence wrote** without asking — the index files and `llms.txt` carry the retrieval metadata.
- **Don't change repo settings** (visibility, branch protection, collaborators) without explicit permission.
- **Don't push to remote** without explicit permission.

### Useful context already saved in your project memory

If you're resuming a Claude Code session, check `~/.claude/projects/-Users-neuralseek-lawrence-Desktop-All-NeuralSeek/memory/MEMORY.md` — Lawrence's role, the central-brain project intent, and the canonical NeuralSeek domain (`neuralseek.ai`, not `.com`) are pinned there.

### Available MCP servers (when configured)

- **`neuralseek`** — hundreds of pre-built NeuralSeek agents (CRM, governance, demo, research, sales-ops). Useful when a task explicitly needs to invoke a NeuralSeek capability rather than just describe it.
- **GitHub web access** via `WebFetch` / `WebSearch` — for verifying live repo state or pulling third-party citations.

