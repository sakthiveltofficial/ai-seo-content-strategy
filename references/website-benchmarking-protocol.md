# Proposed Content vs. Existing Website Benchmarking Protocol

This protocol defines the repeatable workflow for evaluating a proposed SEO landing page or content draft against an existing target website. It ensures that new content strengthens site architecture, avoids cannibalization, accurately reflects the business's real capabilities, and provides a clear upgrade over incumbent pages.

---

## 1. Operating Principle & Scope Boundaries

### Content Review vs. Live Performance Audit
This protocol is a **structural, topical, and strategic content benchmark**, not a live technical or ranking audit.
- **What this review evaluates:** Search intent fit, keyword allocation, topical depth, service boundaries, internal link coherence, heading clarity, conversion paths, proof validity, and differentiation between pages (especially homepage vs. service page).
- **What this review does NOT infer:** Live rankings, organic clicks, impression share, crawl budget, indexation status, Core Web Vitals, or conversion rates. Those metrics require verified Google Search Console, Google Analytics, or live field telemetry. Never state or imply performance metrics without documented measurement.

---

## 2. The 12 Benchmarking Dimensions

For every proposed page evaluated against an existing website, audit these 12 dimensions:

### 1. Search Intent Alignment
- **Evaluation:** Does the proposed page target the specific intent required by the query (Commercial, Transactional, Informational, Navigational)?
- **Check against existing site:** Does an existing page already serve this intent? If so, does the new page complement, refine, or unnecessarily duplicate that intent?
- **Risk to avoid:** Building a commercial service page for a query that the site already addresses with an existing commercial page, creating split ranking signals.

### 2. Primary and Secondary Keyword Targeting
- **Evaluation:** Are primary and secondary keywords allocated with clear page ownership?
- **Check against existing site:** Does the target keyword overlap with headings, title tags, or meta descriptions on existing URLs?
- **Risk to avoid:** Keyword dilution where multiple pages compete for identical exact-match or close-variant phrases.

### 3. Topical Coverage & Content Completeness
- **Evaluation:** Does the proposed content cover the complete decision lifecycle for the topic?
- **Check against existing site:** What critical technical explanations, use cases, or buyer questions are missing from the current site that the proposed page resolves?
- **Standard:** The new page must address specific gaps identified in research, not merely rephrase existing site copy.

### 4. Heading Hierarchy & Readability
- **Evaluation:** Does the page follow a strict semantic hierarchy (single H1, logical H2 sections, structured H3 subsections)?
- **Check against existing site:** Does the proposed content improve upon the existing site's typographic structure, readability, and skim-test clarity?
- **Standard:** A reader skimming only H2s and H3s must understand the complete story and value proposition.

### 5. Local Relevance & Geographic Context (Where Applicable)
- **Evaluation:** For location-targeted pages, does the content reflect authentic local business context, verified industrial clusters, and real service boundaries?
- **Check against existing site:** Does the site have existing local or branch pages? Does the new page maintain consistency in address, service area, and regional positioning?
- **Risk to avoid:** Template city-swapping where the same paragraphs are repeated with only the city name changed.

### 6. Service Coverage & Boundary Definition
- **Evaluation:** Are the service scope, deliverables, and boundaries precisely defined?
- **Check against existing site:** Does the proposed page clearly define where this service begins and ends relative to adjacent services on the website?
- **Standard:** Prevent overlap between parent pillar pages (e.g., Enterprise AI), core capabilities (e.g., LLM Development), and specialized components (e.g., RAG Development).

### 7. Internal Links & Website Architecture Flow
- **Evaluation:** How does the proposed page integrate into the site's topical graph?
- **Check against existing site:** 
  - Which existing pages must link to this new URL (parent, sibling, supporting blog posts)?
  - Which destination pages does the new page link out to (sub-services, case studies, contact funnels)?
- **Standard:** No orphan pages. Contextual anchor text must describe the destination page accurately without forced repetition.

### 8. Conversion Elements & Buyer Journey
- **Evaluation:** Are calls to action specific, high-intent, and aligned with buyer maturity?
- **Check against existing site:** Does the proposed page improve upon generic CTAs ("Contact Us", "Submit") with engineering-aligned, value-first conversion points?
- **Standard:** The page must provide a primary high-commitment action and an optional secondary low-commitment resource path.

### 9. Trust Signals & Verifiable Proof Inventory
- **Evaluation:** Are customer outcomes, technical benchmarks, and security claims supported by verified evidence?
- **Check against existing site:** Does the new page maintain consistency with approved client case studies, certifications, and partner listings on the existing site?
- **Standard:** Never introduce claims, metrics, or case study outcomes that contradict or exceed what the business has verified.

### 10. Factual Consistency & Technical Accuracy
- **Evaluation:** Are technology stacks, API capabilities, frameworks, and operational methodologies accurate?
- **Check against existing site:** Does the page contradict existing technical documentation, published service tiers, or technology stacks described elsewhere on the domain?
- **Standard:** Stacks and methodologies must be current and reflect the client's actual production capabilities.

### 11. Keyword Cannibalization & Competing URLs
- **Evaluation:** Could the proposed URL cannibalize organic equity from an existing ranking URL?
- **Check against existing site:** Search the target domain for `site:domain.com "keyword"` to identify existing indexed assets.
- **Resolution Strategy:**
  - *Consolidate:* If an existing thin page targets the phrase, update and expand that existing URL rather than creating a competing duplicate.
  - *Differentiate:* If both pages must exist, explicitly separate their primary keywords, user personas, and intent.
  - *Redirect:* If the legacy page is outdated and obsolete, replace it with the new page and mandate a 301 redirect map.

### 12. Homepage vs. Service Page Differentiation
- **Evaluation:** Does the proposed service page maintain a distinct center of gravity separate from the company homepage?
- **Check against existing site:** 
  - The **Homepage** establishes overall company identity, primary positioning, multi-service navigation, and brand-level credibility.
  - The **Service Page** must drill deep into one specific solution, answering granular buyer questions, technical trade-offs, architecture specifications, and specialized delivery workflows.
- **Risk to avoid:** Writing a service page that reads like a mini-homepage or restating the entire company overview.

---

## 3. Benchmarking Workflow Procedure

When conducting a Content vs. Existing Website Benchmark:

1. **Inventory Target Assets:** Record the target URL (new or existing), relevant existing site pages, and primary commercial goal.
2. **Inspect Existing Pages:** Review visible copy, headings, metadata, internal links, and proof points on existing candidate URLs.
3. **Score the 12 Dimensions:** Evaluate the proposed draft or strategy against the existing site using the scorecard below.
4. **Identify Strategic Gaps & Risks:** Highlight cannibalization risks, topical blind spots, or inconsistent messaging.
5. **Issue Prioritized Action Recommendations:** Classify actions as `Consolidate`, `Differentiate`, `Rewrite`, or `Publish New`.

---

## 4. Reusable Website Benchmark Scorecard

| Benchmarking Dimension | Existing Site Status | Proposed Content Status | Gap / Opportunity | Action Required |
|---|---|---|---|---|
| **1. Intent Alignment** | [Current page intent] | [Proposed page intent] | [Alignment or mismatch] | [Keep / Adjust intent] |
| **2. Keyword Targeting** | [Current keywords targeted] | [Proposed primary & secondary] | [Overlap or clear ownership] | [Assign primary ownership] |
| **3. Topical Coverage** | [Breadth/depth of existing coverage] | [Depth of proposed sections] | [Unanswered buyer questions] | [Add missing subtopics] |
| **4. Heading Structure** | [Current H1-H3 hierarchy] | [Proposed semantic hierarchy] | [Readability & skim-test clarity] | [Standardize headings] |
| **5. Local Relevance** | [Current regional coverage] | [Proposed local context] | [Generic text vs authentic local cues] | [Add verified local proof] |
| **6. Service Boundaries** | [Unclear or overlapping scope] | [Explicit inclusions/exclusions] | [Boundary confusion] | [Define scope boundaries] |
| **7. Internal Linking** | [Isolated or unstructured links] | [Contextual link map] | [Missing bidirectional equity] | [Implement link map] |
| **8. Conversion Elements** | [Generic CTAs] | [Action-specific CTAs] | [Conversion friction] | [Upgrade CTA copy/subtext] |
| **9. Trust & Proof** | [Unverified or thin proof] | [Structured proof inventory] | [Missing validation] | [Verify or qualify claims] |
| **10. Factual Consistency** | [Legacy claims or outdated stack] | [Modern technical stack] | [Contradictions across site] | [Harmonize technical facts] |
| **11. Cannibalization** | [Existing competing URLs] | [Proposed URL slug] | [Direct competition risk] | [Consolidate / Differentiate] |
| **12. Page Differentiation** | [Broad homepage-style overview] | [Deep solution-specific focus] | [Lack of specialized depth] | [Deepen technical focus] |

---

## 5. Required Deliverable Format

When a Content-to-Website Benchmark is requested, produce `seo_website_benchmark_{domain}_{page_slug}_{date}.md` containing:
1. Executive Summary & Objective (New URL vs. Existing URL Update).
2. Sourced Evidence Ledger (URLs inspected, dates observed, measurement limitations).
3. The 12-Dimension Completed Scorecard.
4. Keyword Cannibalization & Ownership Map.
5. Prioritized Architectural Recommendations (Immediate, Short-Term, Long-Term).
