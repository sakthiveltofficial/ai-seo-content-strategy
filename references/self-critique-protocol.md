# Self-Critique Protocol — Evidence-Led Editorial Quality Gate

Mandatory editorial quality gate before any SEO strategy, content brief, or page copy is declared publish-ready. 

Scores represent an internal qualitative assessment—**not a Google ranking factor, organic traffic prediction, or guarantee of AI answer citations**.

---

## 1. The 12-Dimension Editorial Scoring Framework

Score each dimension on a 1–10 scale:

| Dimension | What It Measures | Weight |
|---|---|---|
| **1. SEO Strategy & Intent** | Match between content and searcher's actual intent; SERP feature capture | 10% |
| **2. Keyword Targeting** | Natural primary, secondary, and semantic entity placement without stuffing | 8% |
| **3. Buyer Clarity** | Clear answers to the 14 core buyer questions; friction-free commercial decision path | 12% |
| **4. Competitive Differentiation** | Clear, defensible positioning that distinguishes the client from alternatives | 8% |
| **5. Content Quality & Voice** | Humanized sentence rhythm, active verbs, absence of buzzwords and AI tells | 10% |
| **6. E-E-A-T & Evidence Integrity** | Verifiable proof, transparent sourcing, absence of fake statistics or case studies | 12% |
| **7. Technical Accuracy** | Accuracy of frameworks, models, APIs, and systems engineering trade-offs | 10% |
| **8. Center of Gravity** | Dominant focus on core service pillar; supporting services appropriately weighted | 8% |
| **9. GEO / AI-Search Readiness** | Direct answer formatting, entity clarity, cite-worthy tables and definitions | 8% |
| **10. Internal-Link Architecture** | Contextual links, anchor diversity, integration with topical site graph | 4% |
| **11. Conversion Potential** | Action-oriented CTAs, value-first hero framing, low-friction next step | 5% |
| **12. Technical SEO & Schema** | Clean metadata, valid JSON-LD schema matching visible content, H1-H3 hierarchy | 5% |

### Passing Standards
- **Minimum Overall Passing Score:** **8.5 / 10** (weighted average).
- **Minimum Individual Dimension Floor:** **7.0 / 10** (no dimension below 7.0).
- **Hard Blocker Overrides:** An unverified customer claim, fabricated metric, unsupported absolute claim, broken primary CTA, or critical indexability error overrides the average score and blocks approval regardless of numeric points.

---

## 2. Mandatory Buyer Clarity Diagnostic (14 Core Questions)

For all commercial service and solution landing pages, evaluate whether the intended buyer can find clear, unambiguous answers to these 14 diagnostic questions. 

*(Note: These are diagnostic evaluation criteria, not a mandate to force 14 individual sections onto every page. Integrate answers where they naturally belong in the user journey.)*

1. **Who is this service for?** (Target persona, company stage, team size, technical maturity).
2. **Which business problems does it solve?** (Specific operational bottlenecks, cost drains, or latency issues).
3. **Which solution or tier is appropriate for their situation?** (Decision criteria guiding selection).
4. **What does the service include?** (Concrete capabilities, architecture design, coding, integration).
5. **What does the customer receive at the end?** (Explicit deliverables: Git repository, custom weights, runbooks, documentation).
6. **What inputs, access, and cooperation are required from the customer?** (Data access, technical contact, API keys, sprint reviews).
7. **How does the project progress and what does the timeline depend on?** (Phased stages, pilot timeline, variables affecting launch).
8. **What affects pricing and ongoing operating costs?** (Engineering scope, compute hosting, token consumption, vector storage).
9. **How will quality, reliability, and success be evaluated?** (Automated benchmarks, latency SLAs, accuracy metrics, RAGAS/Langfuse).
10. **How are security, privacy, and compliance requirements handled?** (Private VPC, zero data retention, HIPAA/SOC 2/GDPR compliance).
11. **How does the solution integrate with existing systems?** (Model Context Protocol, REST/GraphQL APIs, ERP/CRM connectors).
12. **Why is this provider credible and what evidence supports its claims?** (Production workflows, technical depth, verified client results).
13. **What happens after deployment?** (Warranty period, SLA support, maintenance options, internal team training).
14. **What happens when the customer clicks the primary CTA?** (Clear expectation: e.g., "Schedule a 30-minute scoping call with a senior AI engineer").

---

## 3. The 6-Perspective Independent Quality Review

After drafting, switch roles and independently audit the page from 6 distinct perspectives:

| Review Perspective | Key Questions & Audit Focus |
|---|---|
| **1. Target Buyer** | "Do I immediately understand what I get? Is this written for my technical level? Does it address my specific operational risks and budget constraints?" |
| **2. Competitor Analyst** | "Does this sound like every other agency, or is there a defensible reason to choose this company? What do competitors prove that this page only claims?" |
| **3. SEO Strategist** | "Does the page satisfy the search query intent? Are primary and secondary keywords natural? Is there a risk of cannibalizing an existing site page?" |
| **4. Subject-Matter Reviewer** | "Are the technical frameworks, model versions, and architectural trade-offs accurate? Does the engineering logic hold up under senior scrutiny?" |
| **5. Factual-Accuracy Reviewer** | "Are all metrics, research citations, and partner references authentic? Are hypothetical scenarios clearly labeled rather than disguised as case studies?" |
| **6. Conversion-Focused Editor** | "Is the primary CTA compelling and specific? Is there a value-first hero hook? Does the page resolve objections before asking for high-commitment action?" |

---

## 4. Evidence & Trust Verification Workflow

Categorize every substantive factual, technical, or performance claim into one of 6 evidence tiers:

1. **Tier 1: Verified Client / Project Evidence:** Independently confirmed outcomes with documented client approval for public release.
2. **Tier 2: Official Product / Technical Documentation:** Sourced directly from official vendor documentation (e.g., Anthropic, Google Cloud, AWS, Python docs).
3. **Tier 3: Credible External Research:** Cited from recognized research institutions or analyst reports with explicit 4-digit publication years (e.g., *Gartner 2025 AI Report*, *Stanford 2024 AI Index*).
4. **Tier 4: Client-Provided Assertions (Unverified):** Stated by the client but lacking documentation. Must be internally tagged `[SOURCE REQUIRED]` or qualified in public copy.
5. **Tier 5: Illustrative Examples & Hypothetical Scenarios:** Engineered architectural spikes or conceptual workflows. **Must be explicitly labeled as illustrative or hypothetical.**
6. **Tier 6: Proposed Targets & Expected Outcomes:** Future engineering goals (e.g., targeted sub-second latency). Must be stated as targets or ranges, not guaranteed performance.

### Non-Negotiable Rules on Proof
- **Never convert a hypothetical architecture into a real client case study.** If a case study is illustrative, label it clearly: *"Representative Engineering Scenario"* or *"Illustrative Architectural Workflow"*.
- **Never invent client names, testimonials, awards, or performance percentages.**
- **Flag and qualify absolute claims:**

| Absolute / Unsafe Claim | Required Qualification / Safe Alternative |
|---|---|
| *"Eliminates all hallucinations"* | *"Mitigates hallucination risk through grounded RAG and schema validation"* |
| *"Guarantees sub-second latency"* | *"Engineered for sub-second inference targets via vLLM and TensorRT-LLM runtimes"* |
| *"Zero security or compliance risk"* | *"Enforces strict data isolation via private VPC deployment and zero data retention agreements"* |
| *"Universally compatible with any software"* | *"Integrates with major ERP, CRM, and SQL systems via standardized MCP and REST APIs"* |
| *"Guaranteed #1 Google ranking"* | Remove entirely. Never promise ranking positions or search traffic. |

---

## 5. Technical & Pre-Publication Validation Checklist

Before recommending publication, differentiate items **actually tested** from items that **require production deployment testing**:

### On-Page SEO & Content Checks
- [ ] Primary keyword in Title Tag (50–60 chars) and Meta Description (140–160 chars).
- [ ] Single H1 tag outside fenced code blocks (under 70 chars).
- [ ] Heading hierarchy follows strict semantic nesting (H1 > H2 > H3).
- [ ] Target phrase appears naturally in opening 100 words and in at least one H2.
- [ ] Zero forbidden buzzwords (`seamlessly`, `robust solution`, `revolutionize`, `unprecedented`, `synergy`).
- [ ] Zero self-proclaimed superlatives (`premier`, `leading`, `#1`, `best-in-class`, `world-class`).
- [ ] Em-dash density strictly under 2 per 500 words.
- [ ] Contextual internal links point to valid, existing site URLs (not placeholder paths).
- [ ] Structured Data JSON-LD (`Service`, `FAQPage`, `LocalBusiness`) matches visible page content exactly.
- [ ] Schema `@id` and URLs match the actual canonical domain, not an invented URL.

---

## 6. Revision Cycle Template

Document up to 3 iterative revision cycles when an initial draft fails quality thresholds:

```markdown
### Revision Cycle [Number] Output
| Dimension | Baseline Score | Specific Defect / Gap Identified | Tactical Revision Applied | Re-Test Score |
|---|---|---|---|---|
| Buyer Clarity | 6.5 / 10 | Unclear deliverables and handoff terms | Added explicit deliverables bullet list in Section 01 | 9.0 / 10 |
| Evidence & Proof | 6.0 / 10 | Unverified percentage claim in use case | Replaced unverified stat with Gartner 2025 citation | 9.5 / 10 |
| Conversion | 7.0 / 10 | Generic "Contact Us" CTA | Replaced with "Book an Architecture Scoping Session" | 9.5 / 10 |
```
