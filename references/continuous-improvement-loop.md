# Continuous Improvement Loop & Retrospective Protocol

This protocol defines how the AI-Native SEO Content Strategy skill systematically learns from completed projects, content audits, user corrections, and editorial quality reviews. The skill is an evolving operational system—not a static prompt.

---

## 1. Operating Philosophy: Learning from Production Evidence

1. **Evidence-Driven Evolution:** Do not modify the skill after every isolated observation merely to make it longer. Only promote an observation into a reusable rule when it is generalizable, supported by evidence, and likely to prevent repeated defects in future projects.
2. **Layer Discipline:** Every lesson must be committed to its appropriate architectural layer. Never clutter the core skill with client-specific terminology or overly dense reference tables.
3. **Non-Destructive Enhancement:** Never introduce a change that solves one problem by breaking or degrading an existing successful workflow.

---

## 2. Post-Task Lightweight Retrospective (The 7 Questions)

At the conclusion of every substantive SEO strategy, benchmarking, or content creation task, conduct a rapid retrospective evaluating these 7 questions:

1. **What did the initial output handle well?** (Identify successful patterns, strong heading structures, or accurate technical explanations to preserve).
2. **Which gaps were discovered during review?** (Topical blind spots, missed buyer questions, weak proof, formatting friction).
3. **What did the user request to change?** (Direct feedback, preferred terminology, scope modifications, structural shifts).
4. **Which recommendations were accepted, rejected, or modified?** (Distinguish actionable client requirements from client-rejected strategic proposals).
5. **Which issues arose repeatedly?** (Patterns of failure occurring across multiple drafts or sessions).
6. **Which new checks could prevent those issues in future projects?** (Linter rules, intake questions, self-critique gates).
7. **Did an existing instruction fail, or was it simply not followed?** (Distinguish between an instruction defect that requires skill modification and an agent execution lapse that requires reinforcement).

---

## 3. The 5-Layer Architectural Update Framework

When an improvement is justified, place it in the correct layer:

| Layer | Destination Path | What Belongs Here | What Does NOT Belong Here |
|---|---|---|---|
| **Layer 1: Core Skill** | `SKILL.md` | Universal operating contract, mandatory end-to-end workflow stages, tool readiness gates, global E-E-A-T rules, and core SEO principles. | Deep 50-row evaluation tables, client-specific branding, raw template copy. |
| **Layer 2: Specialist Protocols** | `references/*.md` | Deep research methodologies, 12-dimension scorecards, website benchmarking procedures, Google Ads Keyword Planner RPC contracts. | Client-specific project briefs, temporary scratch scripts. |
| **Layer 3: Presentation & Output Formats** | `OutputFormates/*.md` | CMS-ready layout templates, visual/UX asset notes, section numbering conventions (e.g., Webnox Team v2). | Core SEO research algorithms, keyword difficulty formulas. |
| **Layer 4: Reference Examples** | `examples/*.md` | Annotated golden samples, V1-to-V4 evolution case studies, structure/tone models. | Live unverified client deliverables marked as facts. |
| **Layer 5: Improvement History** | `CHANGELOG.md` | Formal audit records, dates, files modified, lessons incorporated, validation results. | Ephemeral conversational chatter. |

---

## 4. Promotion Criteria: When to Update the Skill

Before promoting a lesson into a general rule or reference protocol, verify these 4 criteria:

1. **Reusability Test:** Does this rule apply to future clients, industries, or page types, or is it unique to one specific brand? *(If client-specific, record it in that client's project directory or output format).*
2. **Evidence Threshold:** Has this defect or opportunity been observed more than once, or confirmed by authoritative industry research (Google Search Central, Gartner, W3C)?
3. **Execution Feasibility:** Can an agent or human reviewer realistically evaluate and enforce this rule without ambiguous interpretation?
4. **Regression Safety:** Does this instruction conflict with existing rules regarding proof-before-pitch, value-first heroes, or anti-self-proclamation?

---

## 5. Periodic Maintenance Retrospective

At regular intervals (or after completing 5+ substantive page deliverables), conduct a broader system review:

1. **Review Workspace Artifacts:** Audit recent project deliverables in `projects/` and review feedback in `WORKFLOW_AUDIT_AND_CHANGES.md`.
2. **Identify Redundancies & Contradictions:** Check for overlapping instructions or conflicting gates between `SKILL.md`, `references/`, and `OutputFormates/`.
3. **Audit Local Linter Rules:** Run `tests/test_content_scorer.py` and inspect `scripts/content_scorer.py` to ensure heuristic checks match current quality protocols.
4. **Prune Stale References:** Verify that external links, tool documentation (e.g., Google Ads MCP), and framework versions reflect current standards.
5. **Log Validated Changes:** Record updates in `CHANGELOG.md` with explicit validation evidence.

---

## 6. Formal Change History Record Schema

Every entry in `CHANGELOG.md` must follow this schema:

```markdown
## [Version / Date] - Title of Refinement

- **Files Modified:** List of absolute or relative file paths.
- **Problem / Lesson Discovered:** Specific defect, user feedback, or competitive gap identified.
- **Capability Added / Changed:** New instruction, protocol, or verification gate introduced.
- **Rationale & Evidence:** Why the change was necessary and what source evidence supports it.
- **Validation Performed:** Tests run, scorer results, or smoke tests executed.
- **Known Limitations:** Any tool boundaries, manual decisions, or residual constraints.
```
