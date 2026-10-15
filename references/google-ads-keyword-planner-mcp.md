# Google Ads Keyword Planner MCP — Integration and SEO Use Guide

**Research checked:** 14 October 2026. Recheck the official repository and Google Ads API documentation before implementation because MCP tools, API versions, quotas, and access policies can change.

## 1. Official server: what exists vs. what is needed

Official repository: https://github.com/googleads/google-ads-mcp

The official README currently documents three MCP tools:

| Documented official MCP tool | Current purpose | Value to this SEO workflow |
|---|---|---|
| `search` | Query Google Ads account data using the server's search interface | Useful for inspecting accessible account resources/metrics; it is not documented as a wrapper for Keyword Planner RPC methods. |
| `get_resource_metadata` | Discover fields/metadata for a Google Ads API resource | Helps construct valid account reporting queries and inspect resource structures. |
| `list_accessible_customers` | List customer IDs directly accessible to the authenticated user | Helps select the intended Ads customer/account before querying. |

The README also documents these resources:

- `discovery-document` — current API discovery document, including API methods/resources/schemas;
- `metrics` — reporting metric metadata;
- `segments` — reporting segment metadata;
- `release-notes` — current Google Ads API release notes.

**Important:** as of the checked documentation, the official MCP README does **not** list dedicated MCP tools named `get_keyword_ideas`, `generate_keyword_ideas`, `historical_metrics`, `generate_keyword_historical_metrics`, or `location_targeting`. The underlying Google Ads API supports related Keyword Planner and geo-targeting methods, but an API method existing does not mean the MCP server exposes it as a callable tool. Confirm the connected MCP catalog at runtime.

Do not try to fake those calls through `search`. In the Google Ads API, `GenerateKeywordIdeas`, `GenerateKeywordHistoricalMetrics`, `GenerateKeywordForecastMetrics`, and `GenerateAdGroupThemes` belong to `KeywordPlanIdeaService`; they are not ordinary `GoogleAdsService.Search` GAQL queries.

## 2. Underlying official Google Ads API capabilities useful here

The Google Ads API Keyword Planning overview documents four operations on `KeywordPlanIdeaService`:

| API operation | Primary inputs | Useful returned information | SEO use |
|---|---|---|---|
| `GenerateKeywordIdeas` | Keyword seed, URL seed, keyword+URL seed, or site seed; customer; location targets; language; network; optional date range/annotations | Keyword suggestions plus historical metrics such as average monthly searches, competition, top-of-page bid ranges, and optional concept annotations | Main discovery path for seed expansion and relative demand sizing |
| `GenerateKeywordHistoricalMetrics` | Existing keyword list (up to 10,000 keywords/request); geo targets (up to 10); language; network; optional historical date range/options | Average monthly searches; monthly search-volume history (where returned, up to four years); advertiser competition level/index; low/high top-of-page bid ranges; optional average CPC for legacy support | Refresh and compare a curated candidate list under consistent targeting settings |
| `GenerateAdGroupThemes` | Up to 10,000 keywords and existing ad-group resource names | Keyword suggestions matched to ad-group themes plus suggested match type/campaign/group | Optional paid-search organization only. Not a substitute for intent-based SEO clustering. |
| `GenerateKeywordForecastMetrics` | Inline campaign-to-forecast configuration; keyword/ad-group setup; geography, language, budget/bids/bidding strategy and future period | Forecast metrics such as impressions, clicks, cost and, depending on API version/configuration, additional conversion-related estimates | Optional paid-search planning; never present paid forecasts as organic traffic predictions |

Official references:

- Overview: https://developers.google.com/google-ads/api/docs/keyword-planning/overview
- Generate ideas: https://developers.google.com/google-ads/api/docs/keyword-planning/generate-keyword-ideas
- Historical metrics: https://developers.google.com/google-ads/api/docs/keyword-planning/generate-historical-metrics
- Forecast metrics: https://developers.google.com/google-ads/api/docs/keyword-planning/generate-forecast-metrics
- Ad group themes: https://developers.google.com/google-ads/api/docs/keyword-planning/generate-ad-group-themes
- Location targeting: https://developers.google.com/google-ads/api/docs/targeting/location-targeting
- Geo target suggestion: https://developers.google.com/google-ads/api/reference/rpc/latest/GeoTargetConstantService/SuggestGeoTargetConstants
- Access levels and permissible use: https://developers.google.com/google-ads/api/docs/api-policy/access-levels

## 2.1 Complete capability inventory for this SEO use case

The table below separates what the official MCP documents today from the additional typed wrappers this workflow needs. Names in the Proposed MCP tool column are a recommended interface contract; they are **not** callable until the actual MCP server exposes them.

| Priority | MCP tool / operation | Underlying API capability | Use in this SEO workflow | Boundary |
|---|---|---|---|---|
| P0 | `get_keyword_ideas` (proposed) | `KeywordPlanIdeaService.GenerateKeywordIdeas` | Discover variants from keyword, URL, keyword+URL or site seeds; get initial demand metrics in the same response | Requires Keyword Planner access; paginated results; not an organic rank report |
| P0 | `historical_metrics` (proposed; `get_historical_metrics` alias) | `KeywordPlanIdeaService.GenerateKeywordHistoricalMetrics` | Refresh/normalize a curated list under identical market, language, network and date settings | Up to 10,000 keywords and 10 geo targets per request per current docs; close variants may merge |
| P0 | `location_targeting` (proposed) | `GeoTargetConstantService.SuggestGeoTargetConstants` | Resolve a name like country/state/city to official, targetable geo constants before querying | Lookup/suggestion only; this must not add or mutate campaign targeting |
| P0 | `language_targeting` or `get_language_constants` (proposed) | `language_constant` resource lookup | Resolve supported language constants/resource names instead of guessing IDs | Lookup only; do not assume one language from geography |
| P0 when Ads account data is relevant | Existing `search` (documented) | `GoogleAdsService.Search` or supported search interface | Query the user's accessible account for campaign/keyword/search-term performance when the generic tool and account permissions support the resource | Own-account reporting, not competitor account data; not a substitute for the Keyword Planner RPCs |
| P1 | `get_ad_group_themes` (proposed) | `KeywordPlanIdeaService.GenerateAdGroupThemes` | Optional grouping for paid-search ad groups | Suggested ad groups are not the final SEO content clusters |
| P1, paid-search projects only | `get_keyword_forecasts` (proposed) | `KeywordPlanIdeaService.GenerateKeywordForecastMetrics` | Estimate paid clicks/impressions/cost under explicit campaign assumptions | Never use paid forecasts as organic traffic predictions; read-only forecast only |
| Existing | `get_resource_metadata` (documented) | Resource/field metadata | Discover valid fields for supported account queries | Does not create new Keyword Planner RPC access by itself |
| Existing | `list_accessible_customers` (documented) | Accessible customer IDs | Confirm which account can be queried | Do not silently select or expose unrelated customers |
| Optional response fields | `keyword_annotations` inside idea requests | Keyword concept annotations | Add supporting semantic cues for manual/algorithmic clustering | Annotations are hints, not a complete taxonomy |
| Optional account reporting | Existing `search` if it supports the required GAQL/resource and user permissions allow | `search_term_view`, keyword/campaign/ad-group reporting resources | Find converting or high-impression search terms from the client's own paid campaigns to inform content hypotheses | Account-specific; may omit privacy-thresholded/low-volume queries; label the reporting period and conversion attribution |

**Best implementation order:** build the three P0 Keyword Planner wrappers plus language resolution first. Add account search-term insights only where the account is accessible and that data is relevant. Add ad-group themes and forecasts only for paid-search work. Do not add campaign-creation/mutation tools merely to support organic SEO research.

For account search-term insights, use the existing `search` tool only if its schema and supported GAQL/resources are verified. A reasonable read-only query can examine supported `search_term_view`, keyword, ad-group, campaign and date-segment metrics for the authorized customer. This is the customer’s own paid-search performance—not competitor organic keywords—and low-volume/privacy-limited terms may be absent. Do not invent a `get_search_term_insights` tool unless you build and expose it explicitly.

### Suggested call contract (extension only)

These are interface examples for a future wrapper, not commands to call against the currently documented server. Use the exact argument names implemented in the installed server once available.

```json
{
  "customer_id": "<authorized-customer-id>",
  "seed": {
    "keyword_seed": ["ai agent development", "enterprise workflow automation"]
  },
  "geo_target_constants": ["<resolved-geo-resource-name>"],
  "language_constant": "<resolved-language-resource-name>",
  "network": "GOOGLE_SEARCH",
  "historical_range": {"start_year_month": "YYYY-MM", "end_year_month": "YYYY-MM"},
  "include_annotations": true,
  "page_size": 100,
  "page_token": null
}
```

`historical_range` above is a **normalized proposed-wrapper field**, not a verbatim protobuf request shape. The extension must translate it to the correct versioned Google Ads API request fields. The range may be omitted only when the tool explicitly reports the API default used.

#### Proposed input/result contracts by wrapper

| Proposed tool | Required input contract | Important result fields |
|---|---|---|
| `get_keyword_ideas` | Customer ID; exactly one valid seed shape; resolved geo constant(s); resolved language; network; optional historical range/annotations; pagination | Keyword text, close variants, average monthly searches, monthly-series values when available, advertiser competition/index, bid percentiles, annotations, effective request settings, next-page token, API version/time |
| `historical_metrics` | Customer ID; 1–10,000 keyword strings; up to 10 resolved geo targets; language; network; optional historical range and CPC option | Returned keywords/close variants, volume average and monthly series when available, competition/index, bid ranges, optional CPC, effective settings and mapping/notes for deduplication |
| `location_targeting` | One or more location names/resource names; optional ISO country code and locale | Official geo resource name/criterion ID, display name, target type, country, status, and matched query; ambiguity should return multiple suggestions rather than guess |
| `language_targeting` | Optional language name/code/query | Official language resource name, ID, language code, display name, targetable state if provided |
| `get_ad_group_themes` | Customer ID; keyword list; required valid ad-group resource names per API contract | Theme suggestions and match-type hints, with caveat that they are paid-search organization |
| `get_keyword_forecasts` | Explicit future period, geography, language, keyword/ad-group structure, budget, bid strategy and bids required by the chosen API version | Forecast impressions/clicks/cost and any supported conversion estimates, plus all assumptions and API version |

The wrapper should return request settings alongside results: effective market/location, language, network, selected period, API version, observation time, result count, close variants, metrics, annotations (if requested), next-page token, and structured error details. Never log credentials or include unnecessary account identifiers in user-facing reports.

## 3. Targeting controls and metric interpretation

### Keyword seeds

The ideas method supports:

- **Keyword seed:** at least 1 and up to 20 seed keyword strings.
- **URL seed:** one URL; if it yields no ideas, the method can expand to pages on the same domain. It does not use linked-page contents as seed data.
- **Keyword + URL seed:** can produce more ideas than a URL alone.
- **Site seed:** a domain/site seed; official documentation notes it can generate a very large result set (up to 250,000 ideas from public information). Use pagination and filter sensibly rather than pulling the entire set by default.

Keyword-idea responses support pagination (up to 10,000 results per page according to the current docs). Always inspect the next-page token and apply a practical limit consistent with the research goal.

### Geography and language

- Resolve location IDs with the official `GeoTargetConstantService.SuggestGeoTargetConstants` or another supported official geo-target lookup. A UI label such as "Coimbatore" is not itself a geo-target resource name.
- Keyword Planning requests support up to **10 geo target constants** per request; an empty list can indicate all geographies, but don't use all geographies for a localized decision.
- Resolve language constants from official Google Ads API language-constant data. Don't guess IDs.
- Record the chosen country/city/region, language, search network, and observation date in every matrix/report. If comparing markets, run separate, clearly labeled snapshots where needed.

### Network, date range, annotations

- Choose and record `GOOGLE_SEARCH` or `GOOGLE_SEARCH_AND_PARTNERS` deliberately. Do not compare rows obtained under different network settings as if identical.
- Historical options can specify a year/month range; default averages typically reflect the past 12 months. Monthly search-volume history may be available for up to four years. Use the returned range exactly in the report.
- Keyword annotations can add concept/theme information where supported and requested.
- Keyword results can merge close variants; keep returned variant information and don't interpret the returned row count as the number of exact phrases searched.

### Metrics: permitted conclusions

| Field | Correct interpretation | Do not claim |
|---|---|---|
| `avg_monthly_searches` | Google Ads Keyword Planner's estimated average monthly Google Search demand for the configured context/date range | Exact count of every unique human query or forecast of organic clicks |
| `monthly_search_volumes` | Historical monthly search-volume series when returned | Guaranteed future demand |
| `competition` / `competition_index` (0–100) | Advertiser competition for the configured Ads context | Organic ranking difficulty or a Google organic ranking factor |
| `low_top_of_page_bid_micros` / `high_top_of_page_bid_micros` | Top-of-page advertiser bid percentiles; values are represented in micros and must be converted using the API's currency/units correctly | Guaranteed CPC, revenue, conversion rate, or lead value |
| `average_cpc_micros` | Optional average CPC metric when the API supports/requests it | Organic ranking potential |
| `keyword_annotations` | API-provided concept annotations, where requested | A complete semantic topic map by themselves |
| forecast clicks/impressions/cost/conversions | Modeled paid-campaign outcomes for the exact forecast assumptions/date range | Organic traffic/SEO outcome estimates |

Google's planning service has stricter per-minute limits than many reporting services. Cache/store results where permitted and useful; historical metrics refresh monthly, so repeated immediate calls for identical targeting often add little value.

## 4. Recommended MCP extension contract

If the connected official server exposes only the three default tools above, the following are **proposed extension tools**, not claims about current official tools. Prefer implementing them as thin, typed wrappers around the official Google Ads API client and maintain them separately or upstream them only after reviewing the repository's contribution process.

| Proposed MCP tool | Suggested arguments | Result contract / guardrail |
|---|---|---|
| `get_keyword_ideas` (proposed wrapper) | `customer_id`, one seed object (`keyword_seed`, `url_seed`, `keyword_and_url_seed`, or `site_seed`), `geo_target_constants`, `language_constant`, `network`, optional `historical_metrics_options`, optional `keyword_annotations`, `page_size`/`page_token` | Return keyword text/close variants, historical metrics, annotations, targeting metadata, API version, and next-page token. Validate seed combinations and maximums. |
| `historical_metrics` (proposed canonical wrapper; `get_historical_metrics` is an acceptable alias) | `customer_id`, `keywords[]`, `geo_target_constants`, `language_constant`, `network`, optional date range/options, optional aggregate metrics | Return metrics aligned to input/results, note near-exact deduplication, enforce up to 10,000 keywords and up to 10 geo targets per request. |
| `location_targeting` (proposed canonical wrapper; internally calls `SuggestGeoTargetConstants`) | location name/resource name, country code or locale, target-type constraints when supported | Return official geo names, criterion IDs/resource names, target type, country and status. Never fabricate a match. |
| `get_language_constants` (proposed wrapper) | optional filter/query | Return supported language constants and resource names from the official API metadata/data. Could use a verified lookup if a separate tool is not required. |
| `get_ad_group_themes` (proposed wrapper) | `customer_id`, keyword list, target ad-group resource names | Optional only when Ads keyword grouping is useful. Make clear this is for advertising ad groups, not final SEO clusters. |
| `get_keyword_forecasts` (proposed wrapper) | explicit forecast configuration: date range, geo/language, keyword/ad group structure, budget, bid strategy and bids | Return paid forecast metrics plus every assumption. No account mutation. Reject missing assumptions instead of guessing a paid forecast. |

### Implementation requirements for an extension

1. Use the official Google Ads API client/types for the pinned API version; do not implement undocumented endpoints based on guesswork.
2. Check developer-token access level and permissible use before exposing Keyword Planning methods. Current access-level documentation says Explorer access restricts planning methods, including `KeywordPlanIdeaService`; the appropriate access level/approved use is required.
3. Return structured errors for missing credentials, access denial, customer mismatch, quota/rate limit, invalid target, and API-version mismatch. Do not turn failures into empty keyword results.
4. Enforce documented maximums, pagination, caching, backoff/retry for transient quota/rate-limit responses, and result provenance.
5. Default to read-only keyword research; do not add campaign mutation tools as part of this SEO skill.
6. Never put developer tokens, OAuth secrets, refresh tokens or customer credentials in `SKILL.md`, reports, client configs committed to Git, or model-visible logs. Follow the official server's credential-isolation guidance.
7. Expose API version and retrieval timestamp. The API surface can evolve; inspect its discovery document/release notes when updating.

## 5. Workflow for this SEO skill

1. **Confirm tools:** query the active MCP catalog. Record the exact callable tool names. If the Keyword Planner wrappers are absent, use no guessed function names.
2. **Resolve targeting:** business market → official geo-target suggestion → language constant → search network → historical range. For local SEO, compare the actual service area, not a broad country default.
3. **Seed:** add business-offer keywords, service/page URLs, competitor/market language, and useful site URL seeds. Keep seeds categorized by offer, problem, industry, buyer, use case and job-to-be-done.
4. **Discover:** call keyword ideas in manageable batches; paginate selectively; deduplicate while keeping close-variant notes.
5. **Enrich:** use historical metrics for the curated list if a separate consistent snapshot is useful. Capture search volume, monthly trend, advertiser competition, bid percentiles, and context.
6. **Classify:** map each candidate to informational, commercial investigation, transactional, navigational, local or brand intent using live SERPs and business fit.
7. **Assess organic feasibility:** inspect top results independently. Do not substitute advertiser competition for organic difficulty.
8. **Cluster:** group by intent, entity, problem and best page type. An SEO cluster may span several ad groups; don't let ad-group suggestions dictate site architecture.
9. **Prioritize:** calculate the internal opportunity score from the keyword protocol, show confidence and unresolved fields, then use human/business judgment.
10. **Report:** include provenance/settings, metrics, keyword-to-page mapping, recommended next action, and limitations. Keep raw API metrics distinguishable from derived scores.

## 6. Credentials, access, quotas and safety

- Google Ads API requires Google Cloud/API setup, OAuth/authorized credentials and an appropriate developer token/access level. Production and keyword-planning permissions are not automatic merely because the MCP server is installed.
- The official Google Ads MCP repository documents local/package configuration options, including Python/pipx, developer-token configuration where required, Google Ads API enablement and MCP client configuration. Follow its current README instead of hard-coding an old install command into this skill.
- Keyword Planning calls are rate limited more strictly than ordinary API reporting calls. Batch and cache carefully; avoid repeated identical requests.
- Only request the customer/account needed for the task. Report when `list_accessible_customers` has no relevant customer or when credentials lack access. Do not switch accounts silently.
- The server notes that data is exposed to the connected agent/LLM. Treat Ads-account data as private; minimize result scope and do not include irrelevant account details in generated content.
- For organic SEO-only projects, Keyword Planner metrics help estimate demand and commercial context; no Google Ads campaign needs to be created.

## 7. Keyword Planner report template

```markdown
# Google Ads Keyword Planner Snapshot
- Captured at (UTC or local timezone):
- Google Ads API/MCP server version (if known):
- Customer/account reference (mask IDs where suitable):
- Seed type and seed list:
- Location(s)/geo-target resource names:
- Language constant:
- Network:
- Historical date range:
- Method/tool actually executed:
- Result page / next-page token status:
- Known limitations/errors:

| Keyword | Close variants | Avg. monthly searches | Monthly series/range | Ads competition/index | Low top-page bid | High top-page bid | Intent | Organic difficulty | Source label | Confidence | Target page/action |
|---|---|---:|---|---|---:|---:|---|---:|---|---|---|

## Interpretation
- Demand opportunities:
- Commercial/bid signals (not organic difficulty):
- Seasonal/recency signals:
- SERP validation required:
- Unknowns and next actions:
```

## 8. Official-source links

- Google Ads MCP repository: https://github.com/googleads/google-ads-mcp
- Keyword planning overview: https://developers.google.com/google-ads/api/docs/keyword-planning/overview
- Keyword ideas: https://developers.google.com/google-ads/api/docs/keyword-planning/generate-keyword-ideas
- Historical metrics: https://developers.google.com/google-ads/api/docs/keyword-planning/generate-historical-metrics
- Ad group themes: https://developers.google.com/google-ads/api/docs/keyword-planning/generate-ad-group-themes
- Forecast metrics: https://developers.google.com/google-ads/api/docs/keyword-planning/generate-forecast-metrics
- Geo target suggestions: https://developers.google.com/google-ads/api/reference/rpc/latest/GeoTargetConstantService/SuggestGeoTargetConstants
- Access levels/permissible use: https://developers.google.com/google-ads/api/docs/api-policy/access-levels
