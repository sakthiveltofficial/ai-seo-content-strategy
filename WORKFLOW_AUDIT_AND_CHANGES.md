# Workflow Audit and Refinement Notes

**Source reviewed:** uploaded `ai-seo-content-strategy.zip` (SKILL.md, six original reference files, two scripts, and two example files).  
**Refinement date:** 14 October 2026.  
**Purpose:** improve the workflow in-place without discarding the existing AI-native positioning, site-architecture patterns, humanized writing rules, or editorial self-critique framework.

## Findings in the original package

1. **The two specialist repositories were referenced, but not operationally routed.** `SKILL.md` linked `claude-seo` and mentioned a `claude-seo` framework, but did not specify which capability should own the site audit, which should own competitor/content-gap work, or how to confirm those skills are installed.
2. **Google Ads Keyword Planner was not a defined data source.** The original keyword protocol listed the Keyword Planner UI alongside third-party free tools but had no integration contract, targeting settings, metric interpretation, access requirements, pagination/rate limiting, or MCP availability checks.
3. **Official MCP tool availability could be misread.** The Google Ads API has keyword-planning RPCs, but the official `googleads/google-ads-mcp` README currently documents generic `search`, `get_resource_metadata`, and `list_accessible_customers` tools—not dedicated `get_keyword_ideas`, historical-metrics, or location-targeting MCP tools. The refined guide makes this boundary explicit and documents the wrappers that would need to be exposed.
4. **The previous opportunity formula was mathematically inconsistent with its thresholds.** `(Volume × Intent × Competition Gap) / 3` can exceed the intended 1–10 scale (for three 10s it returns 333.3), while thresholds assumed a maximum of 10. Replaced with a weighted average across five 0–10 factors, with provisional scoring when factors are unknown.
5. **Paid and organic competition could be confused.** Google Ads Keyword Planner competition describes advertiser competition. The revised workflow requires a separate organic-feasibility estimate from observed SERPs/pages and keeps CPC/bid data as commercial/paid signals.
6. **Static example search volumes/trend labels could be reused as facts.** The original files included fixed illustrative values such as `1K/mo`, `6.6K/mo`, `12.1K/mo`, and static labels like "rising" or "highest ROI". Those values are now placeholders or explicitly marked as hypotheses to revalidate by market/date.
7. **The original content-scoring script applied universal gates.** It could penalize pages for missing FAQs, requiring both Organization and FAQPage schema, having fewer than three internal links, or having fewer than 1,500 words even when the brief did not call for them. It also called high-weight failures "critical issues" and described a high score as "publish immediately." The refined script makes these gates opt-in/brief-dependent, reports skipped checks, and labels its score as an advisory heuristic.
8. **The original SERP helper had a hard-coded US Trends URL and a literal primary-keyword placeholder.** It also relies on Browser Harness-only helpers. The refined helper accepts a geography and range and makes the runtime/selector limitations explicit; it still requires an actual connected Browser Harness session and manual verification of dynamic page selectors.
9. **Some content rules overgeneralized style patterns into universal requirements.** Fixed FAQ counts, fixed links-per-word, mandatory identical schema on every page, fixed evidence quotas and measured outcomes in every proof section could encourage low-value or invented content. These are now conditional on the actual search intent, page goal and available evidence.
10. **Audit recommendations lacked a formal closeout loop.** The revised workflow requires re-running the relevant check after an authorized fix and marking the outcome verified/not fixed/not re-tested.
11. **The example content contained specific numbers and delivery-time promises that could be mistaken for proof.** The example is now labeled as a structure/tone example, and the most salient unverified values are converted to evidence placeholders.

## Refined workflow at a glance

1. Preflight the actual tool catalog and credentials; don't silently install tools or assume a repo URL means a skill is installed.
2. Collect business, audience, target market/language, site/page and goal context, asking only for blocking unknowns.
3. Run a dated market pulse and locale-bound live SERP scan; separate business competitors from SERP/content competitors.
4. Resolve Google Ads location/language/network/date parameters and collect keyword ideas/historical metrics only through actually available Keyword Planner tools.
5. Assess organic SERP feasibility separately from Ads competition; cluster by intent, entity, problem and page type; score opportunities with the corrected formula.
6. Run specialist competitor/content-gap analysis and applicable technical/on-page/schema/GEO audits.
7. Map each target cluster to a page and internal-link architecture; build a dated editorial calendar tied to business value.
8. Generate a content brief and draft using real/approved evidence, not invented case studies or statistics.
9. Run the local content linter and 11-dimension self-critique; validate technical/structured-data claims against current policies.
10. Deliver only relevant reports with tool provenance, evidence labels, observation dates, limits and next actions.
11. For website fixes, verify the actual outcome with a relevant rerun before calling the issue closed.

## Google Ads Keyword Planner use-case mapping

| Use case | Underlying official API capability | MCP status in official README checked 2026-10-14 | In this workflow |
|---|---|---|---|
| Expand seed phrases | `KeywordPlanIdeaService.GenerateKeywordIdeas` | No dedicated tool documented | Primary discovery capability if a typed MCP wrapper/authorized API path is available |
| Get historical volumes, monthly values, Ads competition and bid ranges | `KeywordPlanIdeaService.GenerateKeywordHistoricalMetrics`; metrics also accompany idea results | No dedicated tool documented | Proposed `historical_metrics` wrapper for curated list/history refresh; use the ideas response for first-pass filtering |
| Resolve a location by name | `GeoTargetConstantService.SuggestGeoTargetConstants` | No dedicated location-targeting tool documented | Proposed `location_targeting` wrapper; never guess IDs |
| Resolve language targets | Google Ads API language constants/resources | No dedicated language tool documented | Proposed lookup wrapper or validated constant lookup |
| Group advertising keywords into themes | `KeywordPlanIdeaService.GenerateAdGroupThemes` | No dedicated tool documented | Optional Ads grouping; not the site's SEO taxonomy |
| Forecast paid campaign outcomes | `KeywordPlanIdeaService.GenerateKeywordForecastMetrics` | No dedicated tool documented | Optional only for paid-search planning with explicit assumptions; not organic traffic prediction |
| Query Ads account resources/metadata | `GoogleAdsService.Search` via generic MCP | `search`, `get_resource_metadata`, and `list_accessible_customers` documented | Can inform strategy from the user’s own eligible account data where query/resource access is supported; not a replacement for keyword-planning RPCs |

## Validation performed on this package

- Python syntax-compiled `scripts/content_scorer.py` and `scripts/serp_extractor.py`.
- Ran unit smoke tests for conditional scorer gates (see `tests/test_content_scorer.py`).
- Ran the scorer against the combined example file as a diagnostic; it correctly shows why a combined brief/example should not be treated as a raw page draft. The README now explicitly says to run it on the actual draft alone and to use the brief-specific options.
- Checked current public documentation for the official Google Ads MCP tool inventory and official Google Ads Keyword Planning operations. No Google Ads account was accessed and no live keyword metrics were requested as part of this package refinement.

## Source links checked

- Official Google Ads MCP: https://github.com/googleads/google-ads-mcp
- Keyword Planning overview: https://developers.google.com/google-ads/api/docs/keyword-planning/overview
- Generate Keyword Ideas: https://developers.google.com/google-ads/api/docs/keyword-planning/generate-keyword-ideas
- Historical metrics: https://developers.google.com/google-ads/api/docs/keyword-planning/generate-historical-metrics
- Ad group themes: https://developers.google.com/google-ads/api/docs/keyword-planning/generate-ad-group-themes
- Forecast metrics: https://developers.google.com/google-ads/api/docs/keyword-planning/generate-forecast-metrics
- Geo targeting: https://developers.google.com/google-ads/api/docs/targeting/location-targeting
- Access levels/permissible use: https://developers.google.com/google-ads/api/docs/api-policy/access-levels
- `claude-seo`: https://github.com/AgriciDaniel/claude-seo
- `aaron-marketing-skills`: https://github.com/aaron-he-zhu/aaron-marketing-skills

## Important limitation

This package defines the intended workflow and integration contract; it does not install or run `claude-seo`, Aaron Marketing Skills, Browser Harness, or a modified Google Ads MCP server on the user's computer. The Keyword Planner calls will work only when a connected MCP/API client exposes them and Google Ads API access is authorized.
