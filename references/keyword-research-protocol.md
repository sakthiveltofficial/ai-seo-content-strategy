# Keyword Research Protocol — Evidence-Led AI-Native SEO

Read this protocol together with [`google-ads-keyword-planner-mcp.md`](google-ads-keyword-planner-mcp.md). Keyword Planner is the preferred first-party demand source when the relevant API/MCP operation is genuinely available; live SERPs and competitor research determine organic intent and feasibility.

## Core rules

- Record **market/location, language, search network, date range, data source, observation date, and result freshness** for metrics.
- Label values `Measured`, `User-provided`, `Calculated`, `Estimated`, `Unknown`, or `N/A`.
- Google Ads Keyword Planner values are configured-market planning estimates. Advertiser competition and bid values are not organic SEO difficulty and must not be described as ranking factors.
- No static volume table or trend list in this repository is current evidence. Re-query it for the user's market.
- Search volume alone never decides the target. Consider offer fit, buying intent, SERP feasibility, margin/deal value, brand strategy and the ability to deliver distinctive content.

## Phase 1: Build a Seed Set

Start with 3–10 seeds from these source groups. For each seed, save the source/context.

1. **Business/offering seeds:** product/service category, buyer role, industry, problem, desired outcome, technology/method, implementation model, alternative, pricing and hiring intent.
2. **First-party site seeds:** homepage/service/product URLs, current blog pages, Search Console queries/pages if provided, support/sales questions, internal search terms and site navigation.
3. **Search seeds:** live autocomplete, related searches, People Also Ask (PAA), ranking page titles/headings and observed SERP modules. Browser selectors can break; verify visible output before using it.
4. **Community/user-language seeds:** recent relevant Reddit/forum/Hacker News/LinkedIn discussions and Product Hunt launches. Record date and market; engagement is a demand signal, not a search-volume metric.
5. **Trend seeds:** Google Trends related/rising queries and fresh publications. Trends scores represent relative interest, not absolute search demand.
6. **Competitor seeds:** direct competitor site URLs, pages visibly ranking for the target queries, and competitor service or category pages.

Do not treat seed expansion as a finished keyword list. Preserve seeds, source labels and expansion paths so unusual ideas can be traced.

## Phase 2: Google Ads Keyword Planner Research

Use only when a relevant Keyword Planner API method is available through an exposed MCP tool or an authorized official UI/API workflow. Follow the availability and implementation rules in the companion MCP guide.

### 2.1 Resolve targeting first

1. Confirm the user's actual target geography. If location-specific, distinguish country, state/region, city/service area and any nearby areas that matter.
2. Resolve location IDs/resource names from Google Ads API geo-target suggestions; do not guess numeric IDs from memory.
3. Resolve the correct language constant; do not assume English when the target audience is multilingual.
4. Choose `GOOGLE_SEARCH` or `GOOGLE_SEARCH_AND_PARTNERS` intentionally and record it. Use consistent settings for comparisons.
5. Select the historical range. The default average is typically based on the past 12 months; custom historical options and monthly series may be available. Save the actual returned period.

Keyword Planning requests accept up to 10 geo-target constants per request. When comparing more locations or market combinations, split the research into clearly labeled requests rather than overloading one result set.

### 2.2 Generate ideas

Where available, call the underlying `KeywordPlanIdeaService.GenerateKeywordIdeas` through its actual exposed MCP wrapper.

Supported source shapes in the underlying API:

- `KeywordSeed`: 1–20 seed keywords.
- `UrlSeed`: a page URL; if no results are found, the method may expand to pages from the same domain. It doesn't use linked pages' contents as seed data.
- `KeywordAndUrlSeed`: keyword list plus URL; often returns more ideas than URL alone.
- `SiteSeed`: a site/domain seed. The API documentation notes it can return a very large number of ideas for public information; paginate and filter responsibly.

Request useful historical metrics and optional keyword annotations where supported. Handle pagination by checking `next_page_token`; do not assume a short first page is the whole result. Start with a practical page/result limit and broaden only when justified by the opportunity.

### 2.3 Enrich a curated list

Use `GenerateKeywordHistoricalMetrics` when a known list needs comparable historical metrics or a refresh. The underlying API supports up to 10,000 keywords per request and up to 10 geo-target constants. Results can merge near-exact variants, so fewer returned entries than submitted phrases is possible.

Capture where returned:

- `avg_monthly_searches`;
- `monthly_search_volumes` and its date span;
- `competition` and `competition_index`;
- `low_top_of_page_bid_micros` and `high_top_of_page_bid_micros`;
- optional `average_cpc_micros` where the request/API supports it;
- close variants and keyword annotations if present.

Convert any `micros` value according to the API's documented currency/unit semantics; don't print the raw integer as a currency value.

### 2.4 Optional Ads-only operations

- **`GenerateAdGroupThemes`:** optionally helps organize keywords into advertising ad groups and match types. Do not use the ads grouping as the final SEO topic cluster.
- **`GenerateKeywordForecastMetrics`:** optionally estimates a future paid campaign based on a configured forecast campaign, targeting, bidding strategy, budget/bids and future dates. Only run when paid media planning is in scope and required assumptions are supplied. Do not use it to forecast organic SEO clicks.

Keyword planning calls have stricter rate limits than many reporting calls. Cache or store repeated results; historical metrics refresh monthly, and repeated calls on identical settings may not add value.

### 2.5 If dedicated Keyword Planner MCP tools are unavailable

1. Inspect the active MCP tool list; save the exact relevant names.
2. Do not pretend generic Google Ads MCP `search` supports `KeywordPlanIdeaService` RPCs. The official server's documented default tools are generic `search`, `get_resource_metadata` and `list_accessible_customers`.
3. Either use the official Google Ads Keyword Planner UI with an authorized account, use another already-approved connection that truly provides the relevant method, or recommend adding the typed wrappers described in the companion guide.
4. Until data is obtained, label volume and related metrics `Unknown` or `Estimated` using a clearly named fallback source. Do not silently substitute made-up volumes.

## Phase 3: Normalize and Interpret Metrics

Use these interpretations consistently:

| Metric | Use | Do not confuse it with |
|---|---|---|
| Average monthly searches | Relative demand sizing under the request's location/language/network/range | Exact count of unique queries or guaranteed organic clicks |
| Monthly search-volume series | Seasonality and past variation, if supplied | Guaranteed future growth |
| Ads competition level/index | Advertiser competition for Google Ads planning | Organic ranking difficulty |
| Top-of-page bid/CPC | Paid advertiser bid/value signal for commercial terms | Conversion rate, margin, ROI or organic ranking potential |
| Google Trends index | Relative search interest within chosen context and period | Absolute query volume |
| Third-party domain/URL strength metric | Vendor-specific authority/link proxy, if sourced | Google's own domain authority score (there is no universal Google DA metric) |
| SERP-derived organic difficulty | Internal estimate from observed competing pages/sites, page types, intent and differentiation | A guaranteed rank probability |

When metrics are missing, conflicting, rounded, heavily aggregated, or based on different settings, preserve that uncertainty. Do not fill blank metrics with a point estimate unless the estimate is explicitly marked and the source/method is stated.

## Phase 4: Classify Intent and Page Type

Assign the dominant intent from observed SERP evidence; secondary intent is allowed when clearly explained.

- **Informational:** definition, explanation, education, troubleshooting, tutorials.
- **Commercial investigation:** comparisons, providers, alternatives, best-of pages, capability evaluation.
- **Transactional:** hire, buy, book, pricing, quote, implementation/service request.
- **Navigational/brand:** brand, product name, login or a known provider.
- **Local:** a query with location/service-area intent and/or a local pack.

Map intent to a likely page type: service/product page, comparison/alternative page, location page, pillar guide, supporting article, docs page, case study (only real/approved proof), tool/template or existing page update. Don't force a blog post for a query dominated by product/service landing pages.

## Phase 5: Assess Organic Feasibility Separately

Review the current SERP for the primary keyword and meaningful variants. Record:

- dominant page type/intent;
- top-ranking URLs and domains;
- first-hand evidence, technical depth, freshness, expertise/trust indicators and original data;
- SERP features and whether they were directly observed;
- estimated backlink/domain strength only when a named data source supplies it;
- whether an existing page on the user's domain already targets the intent;
- specific ways the user's page could be meaningfully more helpful.

Use an internal organic-difficulty scale only if the report defines the scale and evidence. For example, 1 = relatively accessible observed SERP; 10 = very entrenched/strong observed competition. This is a heuristic and not an official Google metric. Do not use Ads competition to set it.

## Phase 6: Priority Scoring Matrix

Score each factor from 0–10, where 10 is strongest:

- **Demand (25%)** — relative measured search demand in the intended market; if only estimates are available, reduce confidence.
- **Business fit and intent (30%)** — fit with the offer, target buyer, revenue/deal value and intent stage.
- **Organic SERP opportunity (25%)** — realistic opening given competing pages, intent match, content quality gap, site capacity and ability to differentiate.
- **Trend momentum (10%)** — current, dated trend evidence; 5 means neutral/uncertain, not automatically rising.
- **Differentiation/proof ability (10%)** — ability to contribute original expertise, first-hand information, useful tools, real proof or a genuinely better page.

**Opportunity Score (0–10)** = `0.25 × Demand + 0.30 × Business Fit + 0.25 × Organic SERP Opportunity + 0.10 × Trend Momentum + 0.10 × Differentiation/Proof Ability`.

This replaces the prior multiply/divide formula, which produced scores outside its intended 1–10 range. The score is a prioritization aid, not a ranking probability or a Google metric.

- **Tier 1 — Target now:** 8.0–10.0, with high/medium confidence and a clear page/action.
- **Tier 2 — Build toward:** 6.0–7.9, or a high-value topic with one significant uncertainty to validate.
- **Tier 3 — Validate/monitor:** 4.0–5.9.
- **Do not prioritize yet:** below 4.0 or weak business fit regardless of volume.

If a factor is unknown, do not invent its score. Report a `Provisional` score with the missing factor, available-weight coverage, and confidence (`High`, `Medium`, `Low`). Provisional scores are not directly comparable with complete scores unless this caveat is shown.

## Phase 7: Semantic and Intent-Based Clustering

Cluster by shared intent, entity, user problem and best page type—not just lexical similarity. A cluster can contain informational and commercial queries, but if SERPs show different intents, split it into separate page targets and link them contextually.

For each cluster, record:

- cluster name and core entity/problem;
- primary keyword and supported variants;
- supporting questions/subtopics;
- observed intent and market;
- primary URL/page type and secondary linked pages;
- canonical/internal-link considerations;
- estimated demand range/volume context and its source;
- organic competition notes and evidence gaps;
- recommended action, priority and confidence.

Avoid creating one page per keyword when one strong page can satisfy the same intent. Avoid combining disparate intents into a single page just to consolidate keywords.

## Phase 8: Trend and Emerging Keyword Identification

Treat AI/MCP/agentic AI/GEO/AEO/LLMOps and similar themes as possible seed candidates, not current trend facts. Test each in the target geography and timeframe.

For each trend candidate, capture:

- Google Trends range, geography, category and relative index pattern;
- date-stamped recent coverage/community examples;
- Keyword Planner demand metrics (if available);
- SERP maturity and competitor coverage;
- business relevance and ability to publish distinctive evidence;
- risks of short-lived terminology or rapidly changing definitions.

Prioritize rising topics only when the trend evidence is current and there is a clear audience/business reason to cover them.

## Phase 9: Category vs. Money Keyword Strategy

- **Category terms** explain the brand positioning (for example, a niche term the business wants to own).
- **Commercial/money terms** describe services, solutions, providers, software, pricing, alternatives or hiring and may express stronger purchase intent.
- **Informational terms** educate prospective buyers and support topical authority and internal journeys.

Build around the measured keyword ecosystem rather than a category phrase alone. Do not attach fixed search volumes (such as `1K/mo` or `6.6K/mo`) to any term unless a current sourced result for the correct market supports it.

## Phase 10: Competitor Keyword and Content-Gap Analysis

For each target domain:

1. Inventory public URLs using a sitemap/site navigation and approved crawling where possible.
2. Inspect relevant page title, meta description, headings, body structure, visible CTA, page type, proof, schema and internal linking.
3. Use a genuinely available SEO dataset to identify ranking queries, overlap, backlinks or traffic estimates; mark unavailable fields `N/A`.
4. Compare coverage by keyword, topic depth, page format, search intent, freshness, buyer journey and AI-answer citability.
5. Confirm whether the user's own site has an existing page that should be improved or merged rather than creating a new URL.
6. Turn each gap into a hypothesis: competitor/page evidence → missing user need → business value → recommended page/action → success metric.

An uncovered topic is not automatically an opportunity. Validate demand, intent and the business's ability to produce the best useful answer before prioritizing it.

## Required Keyword Matrix

| Keyword | Cluster | Target market | Language | Intent | Page type / URL | Avg monthly searches | Monthly trend | Ads competition/index | Bid range | Organic difficulty (heuristic) | SERP opportunity | Trend status | Source label | Observation date | Confidence | Priority score/tier |
|---|---|---|---|---|---|---:|---|---|---|---:|---|---|---|---|---|---|

Add a source/assumptions note under the matrix specifying the Keyword Planner method, targeting parameters, search network and date range. The values above may be `N/A`/`Unknown` when not supported; that's preferable to invented data.

## Output Checklist

- [ ] Target geography/language/network/date settings recorded.
- [ ] Seed phrases and their sources recorded.
- [ ] Keyword Planner tools actually verified available, or fallback explicitly documented.
- [ ] Ads competition kept separate from organic difficulty.
- [ ] Metrics labeled correctly; no static example volume reused as a fact.
- [ ] Search intent corroborated with live SERPs where possible.
- [ ] Keyword clusters map to pages and buyer journey.
- [ ] Numeric priority score formula and known limitations documented.
- [ ] Gaps connect to a business objective and a concrete next action.
