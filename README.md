# AI-Native SEO Content Strategy — Refined Workflow

This package is the refined version of the local `ai-seo-content-strategy` skill. It preserves the original strategy, templates and examples while adding a capability-gated tool workflow, evidence rules, competitor/audit orchestration, and a Google Ads Keyword Planner MCP integration guide.

## Start here

1. Load `SKILL.md` as the skill entrypoint.
2. Read `references/keyword-research-protocol.md` for demand/keyword work.
3. Read `references/google-ads-keyword-planner-mcp.md` before assuming Google Ads Keyword Planner tools exist.
4. Read `references/competitor-analysis-protocol.md` for competitive research.
5. Use `references/page-type-templates.md`, `references/content-writing-rules.md` and `references/site-architecture-templates.md` as adaptable patterns, not mandatory rules for every page.
6. Run the self-critique protocol before calling content final.

## Google Ads MCP reality check

The official server is https://github.com/googleads/google-ads-mcp. The repository README currently documents three default tools: `search`, `get_resource_metadata`, and `list_accessible_customers`, plus discovery/metrics/segments/release-notes resources. The default tool list does not document dedicated keyword-planning wrappers such as `get_keyword_ideas`, `get_historical_metrics`, or `location_targeting`.

The underlying Google Ads API does support keyword idea, historical metric, ad-group theme, forecast and geo-target-suggestion operations. To use those from an MCP client, either a connected MCP implementation must expose those specific API methods or the official server must be extended with typed wrappers. The guide distinguishes built-in official tools from proposed wrapper names.

## Script notes

- `scripts/content_scorer.py` is an advisory editorial linter, not a Google ranking score. FAQ, schema, internal-link-count and word-count gates are now conditional on the approved brief. Example:

  ```bash
  python scripts/content_scorer.py draft.md "primary keyword" --min-words 900 --max-words 1600 --require-faq --schema-types Organization,Service --min-internal-links 2
  ```

  Pass only options required by the brief. Run it on the final draft alone—not this skill file, a combined report, or an example that contains both a brief and a page draft.

- `scripts/serp_extractor.py` is designed to run inside a connected Browser Harness environment; its helper functions depend on Browser Harness-provided functions such as `js`, `goto_url`, `wait_for_load` and `new_tab`. It is not a standalone Python scraper. Google SERP/Trends DOM selectors can break; verify extracted observations manually and mark unknown values as Unknown.

## Validation

From the package root, run:

```bash
python -m py_compile scripts/content_scorer.py scripts/serp_extractor.py
python -m unittest discover -s tests -v
```

## Evidence and safety

- No static search-volume estimate or template priority should be reused as current research.
- Always label evidence and record the market, language, location, network, time range and date for Keyword Planner observations.
- Google Ads competition is advertiser competition, not organic SEO difficulty.
- Tool names shown as proposed extensions are not evidence they are installed.
- Do not invent proof, client metrics, testimonials, citations, ranking outcomes or audit results.
