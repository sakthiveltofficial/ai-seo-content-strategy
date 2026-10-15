---
name: webnox-team
label: Webnox Team
purpose: Presentation format for final website copy and SEO landing-page content.
---

# Webnox Team — Website Content Output Format

## 1. Purpose and boundary

This file defines **format and page-structure conventions only**. It does not replace the main `SKILL.md`, keyword research, the approved content brief, competitor research, SEO validation, evidence requirements, or writing rules. The main skill remains authoritative.

Use the examples and structures below as a flexible content-output system for Webnox-style page drafts. Keep the output implementation-friendly and easy for an SEO/content team to review. Adapt the page outline to the actual page purpose, service, industry, location, buyer intent, and research—not every page needs every section.

Do not reuse facts, numbers, awards, client names, testimonials, locations, project outcomes, timelines, or performance claims from reference examples as proof for a new page. Only include claims independently supplied or verified for the current project.

## 2. Common formatting conventions

Use the following labels where relevant:

- `URL Slug: /example-page/`
- `SEO Title: [Title]`
- `Meta Description: [Description]`
- `H1: [Primary page heading]`
- `H2: [Major section heading]`
- `H3: [Subsection heading]`
- `H4: [Optional nested item or proof-point heading]`
- `CTA: [Primary CTA]`
- `Secondary CTA: [Secondary CTA]`
- `[Client logo / project visual / approved image]` for an asset requirement
- `[Verified proof point]` or `[Source required]` only during planning; resolve or remove before a draft is labeled publish-ready.

Prefer a plain page-content sequence with clear whitespace and `---` between major page blocks when it improves handoff. Keep heading labels explicit (for example, `H2:`) so the receiving team can identify the intended heading hierarchy. Use bullets for concise feature lists, numbered steps for processes, and Markdown tables when a true comparison is required.

A normal page-copy deliverable starts with the URL slug and metadata, then the H1/hero content, then the selected page sections, and then the closing CTA. Do not add keyword research tables or internal audit commentary inside publish-ready page copy. Supply those as separate research deliverables under the main skill's workflow.

## 3. Page-type selection rule

Select the best-fit pattern below based on the page type agreed in the content brief. Combine patterns only when the page genuinely serves more than one purpose. Do not treat this file as a requirement to create industry, location, or competitor pages that the research did not justify.

## 4. Service or commercial landing page

Use for a main service page or a specific service offering.

```markdown
URL Slug: /[service-slug]/
SEO Title: [Primary service keyword and brand, within an appropriate title length]
Meta Description: [Clear service value proposition and next step]

H1: [Primary service keyword framed around the customer outcome]

[Short hero subheading: what the service helps the customer accomplish]

[One concise introductory paragraph explaining the offer, audience, and business problem.]

CTA: [Primary conversion action]
Secondary CTA: [Secondary conversion action, if useful]

---

H2: [What the service does / business outcome]
[Direct, plain-language explanation of the service and best-fit customer need.]

H2: [Services or capabilities included]
[Short section introduction, where useful.]

H3: [Service/capability 1]
[Description focused on the function, use case, or deliverable.]

H3: [Service/capability 2]
[Description focused on a distinct use case or deliverable.]

H3: [Service/capability 3]
[Add only relevant capabilities supported by the strategy.]

H2: [Proof, real workflows, projects, or implementation examples]
[Use only verified project evidence, approved testimonials, or clearly labeled illustrative workflows. Include the source or approval reference in the working brief—not as invented proof in the live copy.]

H2: [Why this approach / differentiators]
[Explain specific evidence-backed differences rather than unsupported superlatives.]

H2: [Process: from discovery to delivery]
H3: 01. [Step name]
[What happens and what the client receives.]
H3: 02. [Step name]
[What happens and what the client receives.]
H3: 03. [Step name]
[What happens and what the client receives.]
[Add or remove steps to fit the real delivery process.]

H2: [Relevant technology, integrations, or delivery options]
[Group into H3/H4 categories only when useful; include only technologies the team can substantiate.]

H2: Frequently Asked Questions About [Service]
### [Question aligned with real buyer intent?]
[Direct answer. Include an FAQ only when research shows useful questions; avoid filler FAQs.]

H2: [Final outcome-led CTA heading]
[Brief closing statement tying the service to the problem and next step.]
CTA: [Primary CTA]
Secondary CTA: [Secondary CTA]
```

### Optional blocks for service pages

Add only if useful and supported:

- **Company experience / proof strip:** approved years, client counts, countries served, awards, certifications, or verified operational metrics. Record the source and validation date in the content brief.
- **Projects / case studies:** project name, domain/use case, challenge, solution, capabilities, verified outcome, and project link/CTA.
- **Technology stack:** group models, frameworks, data systems, integrations, infrastructure, and monitoring; avoid implying every listed technology is used in every engagement.
- **Industry applications:** include the industries that match the service and researched audience. For detailed industry intent, use the industry-page pattern instead.

## 5. Industry-specific service or solution page

Use when the main intent is both a defined industry and a service/use case (for example, a service tailored to manufacturing or healthcare). Make the industry relevance specific rather than swapping the industry name into generic copy.

```markdown
URL Slug: /[industry]-[service-slug]/
SEO Title: [Industry + service keyword]
Meta Description: [Industry-specific outcome and CTA]

H1: [Service for the target industry]
[Hero subheading naming the main operational problem or use case.]
[Short introduction connecting the service to the industry's workflows without unsupported claims.]

CTA: [Primary CTA]
Secondary CTA: [Secondary CTA]

---

H2: [Industry problem, workflow, or business context]
[Describe the verified or well-sourced context relevant to the target audience.]

H2: [Industry-specific use cases]
H3: [Use case / workflow 1]
[Problem → how the solution fits → practical value.]
H3: [Use case / workflow 2]
[Problem → how the solution fits → practical value.]
H3: [Use case / workflow 3]
[Include only use cases in scope.]

H2: [Solutions / capabilities for this industry]
[Group services around the industry's workflows, not a generic service list.]

H2: [Data, system, compliance, or integration considerations]
[Describe only verified capabilities; do not claim certification or regulatory compliance without evidence.]

H2: [Relevant project, proof, or implementation approach]
[Use approved proof or describe a clearly labeled illustrative workflow.]

H2: [Implementation process]
[Use the applicable process steps from the main brief.]

H2: Frequently Asked Questions About [Industry + Service]
[Answer researched industry-specific questions directly.]

H2: [Closing CTA heading]
[Close with the outcome relevant to this industry.]
CTA: [Primary CTA]
```

## 6. Location or local service page

Use only when the business genuinely serves the location and the location page has a distinct user purpose. Do not generate near-duplicate doorway pages by changing city names alone.

```markdown
URL Slug: /[service]-[location-slug]/
SEO Title: [Service + location]
Meta Description: [Service, relevant location context, and next step]

H1: [Service in / for the target location]
[Intro that clearly states the offering and the actual service-area relationship.]

CTA: [Primary CTA]
Secondary CTA: [Optional secondary CTA]

---

H2: [Service] for Businesses in [Location]
[Explain the service and its relevance to the local audience.]

H2: [Local customer needs or use cases]
[Use substantiated local industry or customer context; do not invent location-specific demand statistics.]

H2: [Services available in [Location]]
[Include only services and coverage that are actually offered.]

H2: [Relevant local work, projects, or customer proof]
[Include only verified examples whose use on this page is approved.]

H2: [How the engagement works]
[Explain consultation, remote/on-site availability, delivery, and support only where confirmed.]

H2: [Why choose this provider for this requirement]
[Use specific, evidenced differentiators; do not rely on generic local superiority claims.]

H2: Frequently Asked Questions About [Service] in [Location]
[Answer relevant questions on coverage, delivery, timelines, and engagement terms using confirmed information.]

H2: [Closing CTA]
CTA: [Primary CTA]
```

**Location-specific fields to verify before drafting:** genuine service-area coverage, office/address details if mentioned, availability of on-site support, local case studies, named local clients, regional language support, and any local regulatory or market claims. Leave out unverified items.

## 7. Competitor comparison or alternative page

Use only when the strategy supports a comparison query and there is enough current evidence to compare the offerings fairly. Keep the page useful rather than disparaging the competitor.

```markdown
URL Slug: /[brand]-vs-[competitor-or-alternatives]/
SEO Title: [Brand vs Competitor / Alternatives to Competitor]
Meta Description: [Accurate statement of what the comparison helps readers decide]

H1: [Brand] vs [Competitor]: [Decision or use-case angle]
[Brief scope note: what is compared, the observation date, and the intended reader.]
[Answer-first summary stating the main fit distinction, grounded in evidence.]

CTA: [Relevant primary CTA]

---

H2: [Brand] and [Competitor]: Overview
[Neutral descriptions based on official sources or verified product/service pages.]

H2: [Key differences]
| Comparison factor | [Brand] | [Competitor] | Evidence / notes |
|---|---|---|---|
| [Factor] | [Verified value] | [Verified value or Unknown] | [Source and observation date] |

H2: [Where each option may fit best]
H3: [Brand] may fit teams that need [evidence-supported fit]
[Explain fit with factual capabilities and caveats.]
H3: [Competitor] may fit teams that need [evidence-supported fit]
[Explain fit fairly and without unsupported negative claims.]

H2: [Capabilities, scope, or service approach]
[Discuss only factors relevant to the search intent and decision.]

H2: [Questions to ask before choosing]
[Practical decision criteria; distinguish facts from recommendations.]

H2: Frequently Asked Questions
[Answer genuine comparison questions.]

H2: [Closing CTA]
[Offer a next step related to the reader's evaluation process.]
CTA: [Primary CTA]
```

Source every comparative claim. Use `Unknown` or `Not publicly stated` when a factor cannot be confirmed. Do not invent competitor shortcomings, pricing, customer counts, ranking results, or capabilities. Do not use a comparison table to label the client's own historical offering or domain negatively.

## 8. Homepage or primary category page

Use for the main company page or a high-level category hub. Keep the main positioning dominant and service links subordinate to it.

```markdown
SEO Title: [Brand + primary category / value proposition]
Meta Description: [Company summary and main customer outcome]

H1: [Company positioning and core customer outcome]
[Short explanation of whom the business serves and what it helps them do.]
CTA: [Primary CTA]
Secondary CTA: [Secondary CTA]

H2: [Core positioning supported by experience]
[Explain the company's approach and fit. Add verified metrics only if relevant.]

H2: [Main services / solution pillars]
H3: [Pillar 1]
[Concise description and link/CTA to the relevant service page.]
H3: [Pillar 2]
[Concise description and link/CTA to the relevant service page.]
[Add only the pillars justified by the site architecture.]

H2: [Selected projects / products / real workflows]
[Use approved examples with clear capabilities and evidence.]

H2: [Who we help / industry applications]
[Include only relevant industries or audience groups.]

H2: [Why work with us]
[Evidence-backed differentiators rather than broad, unsupported praise.]

H2: [Delivery process]
[Summarize the actual working process.]

H2: [Closing CTA]
CTA: [Primary CTA]
Secondary CTA: [Secondary CTA]
```

A homepage/category page can omit detailed technical stacks, long service descriptions, or FAQs when they would distract from the main positioning. Link to dedicated pages instead.

## 9. Blog, pillar guide, or supporting article

Use for informational or educational content. Preserve the main skill's source/citation standards and query intent. Do not force a service-page structure onto an article.

```markdown
URL Slug: /[article-slug]/
SEO Title: [Clear query-aligned title]
Meta Description: [Accurate promise of what the reader will learn]

H1: [Article title]
[Optional concise dek/subheading describing the reader benefit.]
[Intro: establish context and answer the question early.]

H2: [Direct answer / definition]
[Answer the central query clearly and succinctly.]

H2: [Why it matters / context]
[Evidence-backed context, definitions, limitations, or audience relevance.]

H2: [How it works / main framework]
H3: [Component or step 1]
[Explanation, example, or evidence.]
H3: [Component or step 2]
[Explanation, example, or evidence.]

H2: [Practical examples / implementation considerations]
[Clearly distinguish documented examples from hypothetical illustrations.]

H2: [Comparisons, alternatives, or trade-offs]
[Include only if relevant to the search intent.]

H2: [Conclusion / practical next steps]
[Summarize the useful takeaway.]

H2: Frequently Asked Questions
[Optional; use only when questions add value and can be answered accurately.]

CTA: [Contextually relevant next step, if appropriate]
```

Use sources and references in the article body where they support material claims. Keep the CTA proportionate to the reader's intent; an informational article need not use the same sales-heavy CTAs as a service landing page.

## 10. Project, solution, and case-study blocks

When a page includes a project or case study, use this compact reusable block:

```markdown
H3: [Project / solution name]
[Category / industry / use case]

**Challenge:** [Verified description of the problem or clearly marked illustrative scenario.]
**Solution:** [What was actually built or implemented.]
**Key capabilities:** [Capabilities confirmed by project materials.]
**Outcome:** [Verified outcome and measurement context, or omit if not available.]
CTA: [View Project / Read Case Study / Discuss a Similar Project]
```

Do not turn capabilities into measurable outcomes unless evidence supports the outcome. Where the source provides an outcome, preserve its exact scope and units and include context where needed.

## 11. Process, technology, industry, and trust modules

These are reusable format modules, not mandatory sections for every page.

### Process module

```markdown
H2: [Process title]
H3: 01. [Step name]
[Action taken and output/deliverable.]
H3: 02. [Step name]
[Action taken and output/deliverable.]
H3: 03. [Step name]
[Action taken and output/deliverable.]
```

Use the actual process approved in the content brief. Do not promise delivery timelines that have not been confirmed.

### Technology module

```markdown
H2: [Technology heading]
[Short explanation of technology selection based on project requirements.]
H3: [Category]
[Verified tools, platforms, and integrations separated by a consistent delimiter or concise bullets.]
```

Only list tools the business uses or can credibly provide. Avoid implying that every client project uses every item.

### Industry-list module

```markdown
H2: [Industry applications heading]
H3: [Industry 1]
[Industry-specific applications relevant to the current service.]
H3: [Industry 2]
[Industry-specific applications relevant to the current service.]
```

Use industry modules on a general service page only when they support the page's core positioning. Use a dedicated industry page when the audience and query intent warrant deeper detail.

### Trust / proof module

```markdown
H2: [Evidence or experience heading]
[Verified proof point 1 — include context and source in the working brief.]
[Verified proof point 2 — include context and source in the working brief.]
[Approved client logos, certifications, reviews, or project links where available.]
```

Do not fill this module with generic numeric claims merely to make a page appear authoritative. If no suitable proof is available, use a factual explanation of process or capability instead.

## 12. FAQ and final CTA conventions

- Use an FAQ heading in the form `H2: Frequently Asked Questions About [Topic]` when an FAQ helps the page and the research supports it.
- Format each question as `H3: [Question]`, followed by a direct, self-contained answer.
- Do not invent FAQs just to add page length. Do not force FAQ schema; schema eligibility is governed by the main skill's validation rules.
- End commercial pages with a brief, outcome-oriented close and explicit CTA labels. Use primary and secondary CTAs only when they serve distinct next steps.
- CTA labels should describe the actual action (for example, discuss a project, request an assessment, view a project). Do not invent contact channels, forms, consultation terms, pricing, availability, or guarantees.

## 13. Publish-ready output rules

Before returning final content:

1. Preserve the approved target keyword, intent, market, page purpose, and primary positioning.
2. Apply the relevant format pattern only; remove irrelevant modules and repetitive sections.
3. Ensure the H1, section labels, CTA labels, metadata and URL slug are clearly distinguished.
4. Resolve or remove all draft placeholders. If a required business fact is missing, ask for it or omit that claim rather than filling it with a guess.
5. Verify page-specific claims, company figures, project details, testimonial permission, local coverage, competitor comparisons, and all quantitative proof against the evidence inventory.
6. Retain links and citations needed for fact-checking in the working/content handoff. Do not present internal audit notes as page copy.
7. Return the final copy in the selected format, then provide any separate research/audit notes in their normal report format when the task calls for them.

**Reminder:** this format controls how Webnox-style page content is organized and labeled. The main `SKILL.md` controls research, strategy, evidence, quality, and whether each section belongs on the page.
