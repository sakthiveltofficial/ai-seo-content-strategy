#!/usr/bin/env python3
"""
Content Quality Scorer (heuristic linter, not a search-ranking predictor)
Evaluates draft content against editorial/SEO checks. Run against generated content,
then review false positives against the approved brief and page type.

Usage:
  python scripts/content_scorer.py draft.md "primary keyword" \
      --min-words 900 --max-words 1600 --require-faq \
      --schema-types Organization,Service --min-internal-links 2
Only pass requirements that the approved content brief actually calls for.
"""

import argparse
import re
import sys

def score_content(
    content: str,
    primary_keyword: str,
    *,
    min_words: int | None = None,
    max_words: int | None = None,
    require_faq: bool = False,
    schema_types: list[str] | None = None,
    min_internal_links: int | None = None,
) -> dict:
    """Run advisory checks. Optional gates must match the page's approved brief."""
    
    results = {
        'total_score': 0,
        'max_score': 0,
        'checks': [],
        'warnings': [],
        'errors': [],
        'skipped_checks': [],
        'passed_checks': 0,
        'total_checks': 0,
        'weak_areas': {} # category -> points lost
    }
    
    text_lower = content.lower()
    # Normalize punctuation so variations such as "AI-native" and "AI native"
    # can match in this heuristic check; do not force exact-match phrasing.
    def normalize_phrase(value: str) -> str:
        return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", value.lower())).strip()
    kw_normalized = normalize_phrase(primary_keyword)
    
    current_category = "General"

    def set_category(cat: str):
        nonlocal current_category
        current_category = cat
        if cat not in results['weak_areas']:
            results['weak_areas'][cat] = 0

    def check(name: str, passed: bool, points: int, message: str = ""):
        if isinstance(points, float):
            points = float(points)
        results['total_checks'] += 1
        results['max_score'] += points
        if passed:
            results['passed_checks'] += 1
            results['total_score'] += points
            results['checks'].append(f"✅ [{points}pts] {name}")
        else:
            if current_category not in results['weak_areas']:
                results['weak_areas'][current_category] = 0
            results['weak_areas'][current_category] += points
            
            msg = f"❌ [{points}pts] {name}"
            if message:
                msg += f" — {message}"
            results['checks'].append(msg)
            if points >= 3:
                results['errors'].append(msg)
            else:
                results['warnings'].append(msg)
    
    def skip(name: str, reason: str):
        """Record a not-in-scope check without lowering the draft's score."""
        results['skipped_checks'].append(f"⏭️  {name} — {reason}")

    def warn(message: str):
        results['warnings'].append(f"⚠️  {message}")
    
    # ===== Keyword Placement Checks =====
    set_category("Keyword Placement")
    
    # Title tag presence and keyword
    title_match = re.search(r'(?i)\[TITLE TAG\].*?([^\n]+)', content)
    title_text = title_match.group(1) if title_match else ""
    check("Primary keyword or punctuation-normalized variant in title tag",
          kw_normalized in normalize_phrase(title_text), 5,
          f"Include the target phrase naturally in the title tag if it fits the SERP intent")
    
    title_len = len(title_text.strip('[] '))
    check("Title tag length (50-60 chars)", 45 <= title_len <= 65, 3,
          f"Current: {title_len} chars")
    
    # Meta description
    meta_match = re.search(r'(?i)\[META DESC\w*\].*?([^\n]+)', content)
    meta_text = meta_match.group(1) if meta_match else ""
    check("Primary keyword or punctuation-normalized variant in meta description",
          kw_normalized in normalize_phrase(meta_text), 3,
          "Mention the target phrase naturally when it helps users understand the page")
    
    meta_len = len(meta_text.strip('[] '))
    check("Meta description length (140-160 chars)", 130 <= meta_len <= 165, 2,
          f"Current: {meta_len} chars")
    
    # H1 check
    h1_match = re.search(r'^#\s+(.+)', content, re.MULTILINE)
    h1_text = h1_match.group(1) if h1_match else ""
    check("Primary keyword or punctuation-normalized variant in H1",
          kw_normalized in normalize_phrase(h1_text), 5,
          "Reflect the target topic naturally in the H1; do not force an awkward exact match")
    
    h1_len = len(h1_text)
    check("H1 length (under 70 chars)", h1_len <= 70, 2,
          f"Current: {h1_len} chars")
    
    # Keyword in first 100 words
    words = content.split()
    first_200 = ' '.join(words[:200]).lower()
    check("Primary keyword or punctuation-normalized variant in opening",
          kw_normalized in normalize_phrase(first_200), 4,
          "Mention the target topic naturally in the opening when relevant")
    
    # H2 keyword presence
    h2_matches = re.findall(r'^##\s+(.+)', content, re.MULTILINE)
    h2_with_kw = [h for h in h2_matches if kw_normalized in normalize_phrase(h)]
    check("Target phrase or punctuation-normalized variant in an H2",
          len(h2_with_kw) >= 1, 2,
          "Use in a subheading only where it reads naturally; not every page requires the exact phrase in an H2")
    
    # ===== Structure Checks =====
    set_category("Structure")
    
    content_without_code = re.sub(r"```.*?```", "", content, flags=re.DOTALL)
    h1_lines = re.findall(r"^#\s+.+$", content_without_code, flags=re.MULTILINE)
    check("Has one H1 outside fenced code", len(h1_lines) == 1, 4,
          f"Detected {len(h1_lines)} H1 headings; use one clear page H1 outside code examples")
    
    h2_count = len(h2_matches)
    check("Has 4+ H2 sections", h2_count >= 4, 3,
          f"Current: {h2_count} H2s")
    
    h3_matches = re.findall(r'^###\s+(.+)', content, re.MULTILINE)
    check("Has H3 subsections", len(h3_matches) >= 2, 2)
    
    # FAQ is intent/brief-dependent; do not require it for every page.
    has_faq = bool(re.search(r'(?im)^##\s+.*(faq|frequently asked|questions)', content))
    if require_faq:
        check("Has FAQ section when required by brief", has_faq, 4,
              "Add the FAQ section specified in the approved content brief")
    elif not has_faq:
        skip("FAQ section", "not required by the approved brief")

    if has_faq:
        faq_start = re.search(r'(?im)^##\s+.*(faq|frequently asked|questions)', content)
        faq_content = content[faq_start.start():] if faq_start else content
        faq_questions = re.findall(r'(?m)^.*\?\s*$', faq_content)
        if len(faq_questions) >= 1:
            check("FAQ question coverage", len(faq_questions) >= 5, 2,
                  f"Detected: {len(faq_questions)} question lines; use the brief's required coverage")
        else:
            warn("An FAQ heading exists but question extraction was inconclusive; review manually.")
    
    # ===== Humanization Checks =====
    set_category("Humanization")
    
    # Forbidden openers
    bad_openers = [
        "in today's world", "in today's fast", "in the era of", "as ai continues",
        "welcome to", "at {company", "are you looking", "have you ever wondered",
        "in recent years", "as we move into"
    ]
    opener_para = ' '.join(words[:50]).lower()
    has_bad_opener = any(phrase in opener_para for phrase in bad_openers)
    check("No forbidden opener phrases", not has_bad_opener, 4,
          "Rewrite opening paragraph — avoid generic AI/marketing openers")
    
    # Em-dash overuse (AI tell)
    em_dash_count = content.count('—')
    words_count = len(words)
    em_dash_per_500 = (em_dash_count / max(words_count, 1)) * 500
    check("Em-dash usage (under 2 per 500 words)", em_dash_per_500 <= 2, 2,
          f"Current: {em_dash_per_500:.1f} per 500 words")
    
    # Forbidden phrases
    forbidden = ['seamlessly', 'robust solution', 'revolutionize', 'unprecedented', 
                 'synergy', 'game-changing', 'cutting-edge technology']
    found_forbidden = [f for f in forbidden if f in text_lower]
    check("No forbidden marketing buzzwords", len(found_forbidden) == 0, 3,
          f"Remove: {found_forbidden}")
    
    # Passive voice check (rough)
    passive_patterns = [r'\bwas\s+\w+ed\b', r'\bwere\s+\w+ed\b', r'\bhas been\s+\w+ed\b',
                       r'\bhave been\s+\w+ed\b', r'\bis\s+\w+ed\b']
    passive_count = sum(len(re.findall(p, content)) for p in passive_patterns)
    passive_ratio = passive_count / max(len(re.findall(r'[.!?]', content)), 1)
    check("Passive voice under 15%", passive_ratio < 0.15, 2,
          f"Passive ratio: {passive_ratio:.0%}")
    
    # ===== E-E-A-T Checks =====
    set_category("E-E-A-T")
    
    # Technical terms
    tech_terms = ['langchain', 'langgraph', 'crewai', 'autogen', 'llamaindex', 
                  'llm', 'rag', 'mcp', 'vector', 'embedding', 'inference',
                  'orchestrat', 'agentic', 'retrieval']
    found_tech = [t for t in tech_terms if t in text_lower]
    check("Technical credibility signals (5+ tech terms)", len(found_tech) >= 5, 3,
          f"Add more technical vocabulary. Found: {found_tech}")
    
    # External link signals (mentions of frameworks/sources)
    authority_signals = ['github', 'arxiv', 'research', 'according to', 'study',
                        'report', 'stanford', 'mckinsey', 'gartner']
    found_authority = [s for s in authority_signals if s in text_lower]
    check("E-E-A-T authority signals", len(found_authority) >= 2, 2)
    
    # ===== Positioning & Strategy =====
    set_category("Positioning & Strategy")
    
    # 1. Center-of-gravity check (4 pts)
    sections = re.split(r'^##\s+', content, flags=re.MULTILINE)[1:] # split by H2
    section_lengths = [len(s.split()) for s in sections]
    if section_lengths:
        avg_len = sum(section_lengths) / len(section_lengths)
        max_len = max(section_lengths)
        check("Center-of-gravity check", max_len >= 1.5 * avg_len, 4,
              "Ensure one primary H2 section gets significantly more depth than others")
    else:
        check("Center-of-gravity check", False, 4, "No H2 sections found")
        
    # 2. Proof-before-pitch check (5 pts)
    proof_words = ['built for', 'real enterprise', 'real-world', 'how our', 'live operations', 'production']
    pitch_words = ['our services', 'capabilities', 'what we build', 'what we do']
    
    first_proof_idx = len(text_lower)
    first_pitch_idx = len(text_lower)
    for w in proof_words:
        idx = text_lower.find(w)
        if idx != -1 and idx < first_proof_idx: first_proof_idx = idx
    for w in pitch_words:
        idx = text_lower.find(w)
        if idx != -1 and idx < first_pitch_idx: first_pitch_idx = idx
        
    if first_pitch_idx < len(text_lower):
        check("Proof-before-pitch check", first_proof_idx < first_pitch_idx, 5,
              "Show proof of work before pitching services")
    else:
        check("Proof-before-pitch check", True, 5) # Pass if no pitch found
        
    # 3. Self-proclamation check (4 pts)
    proclamation_words = ['premier', 'leading', '#1', 'best-in-class', 'world-class', 'top-tier', 'industry-leading', 'unmatched', 'unparalleled']
    found_proclamations = [w for w in proclamation_words if w in text_lower]
    check("Self-proclamation check", len(found_proclamations) == 0, 4,
          f"Remove self-promotional words: {found_proclamations}")
          
    # 4. Fake statistics check (4 pts)
    fake_stats_patterns = [r'\d+%\s+of\s+companies', r'studies show', r'research shows', r'according to\s+(?!.*\d{4})']
    fake_stats_found = []
    for pat in fake_stats_patterns:
        matches = re.findall(pat, text_lower)
        if matches: fake_stats_found.extend(matches)
    check("Fake statistics check", len(fake_stats_found) == 0, 4,
          "Cite specific reports/years for statistics or remove them")
          
    # 5. Value-first hero check (4 pts)
    value_words = ['what you get', 'you receive', 'you get', 'delivered to', 'deployed in', 'in 30 days', 'in 60 days', 'in 90 days', 'in days', 'in weeks', 'in x days']
    hero_para = ' '.join(words[:300]).lower()
    has_value_first = any(w in hero_para for w in value_words)
    check("Value-first hero check", has_value_first, 4,
          "Include clear value statements like 'what you get' or 'deployed in' in first 300 words")
          
    # 6. Comparison table safety check (3 pts)
    table_headers = re.findall(r'\|(.*?)\|(?=\n\|[-:]+)', content)
    has_bad_table_header = False
    if table_headers:
        for header_row in table_headers:
            if 'legacy' in header_row.lower(): 
                has_bad_table_header = True
    check("Comparison table safety check", not has_bad_table_header, 3,
          "Ensure comparison tables don't contain own legacy brand in headers")
          
    # 7. AI buzzword density check (3 pts)
    ai_buzzwords = ['autonomous', 'agentic', 'next-generation', 'revolutionary', 'transformative']
    buzzword_count = sum(text_lower.count(w) for w in ai_buzzwords)
    buzzword_density = buzzword_count / max(words_count, 1) * 200
    check("AI buzzword density check", buzzword_density <= 1, 3,
          f"Current: {buzzword_density:.1f} per 200 words")

    # ===== GEO/AEO Readiness =====
    set_category("GEO/AEO Readiness")
    
    # 8. Entity clarity check (3 pts)
    service_indicators = ['platform', 'solution', 'service', 'agency', 'provider', 'software', 'system']
    first_200 = ' '.join(words[:200]).lower()
    has_entity_clarity = any(ind in first_200 for ind in service_indicators)
    check("Entity clarity check", has_entity_clarity, 3,
          "Ensure company name/service type is clearly established in first 200 words")
          
    # 9. Direct answer formatting check (3 pts)
    if h2_matches:
        h2_sections = re.split(r'^##\s+', content, flags=re.MULTILINE)[1:]
        direct_starts = 0
        for sec in h2_sections:
            lines = [line.strip() for line in sec.strip().splitlines() if line.strip()]
            sec_text = '\n'.join(lines)
            first_body_line = lines[1] if len(lines) > 1 else (lines[0] if lines else '')
            if first_body_line and not first_body_line.endswith('?') and not first_body_line.lower().startswith("let's"):
                direct_starts += 1
        direct_ratio = direct_starts / len(h2_sections)
        check("Direct answer formatting check", direct_ratio >= 0.7, 3,
              f"Current: {direct_ratio:.0%} of H2s start with direct answers")
    else:
        check("Direct answer formatting check", False, 3, "No H2 sections found")
        
    # 10. Structured data is optional in a prose draft; test only explicitly expected types.
    if schema_types:
        for schema_type in schema_types:
            pattern = r'"@type"\s*:\s*"' + re.escape(schema_type.strip()) + r'"'
            found_schema = bool(re.search(pattern, content))
            check(f"Expected schema type present: {schema_type.strip()}", found_schema, 2,
                  f"Include/validate {schema_type.strip()} only if it matches visible content and current policies")
    else:
        skip("Structured data checks", "schema types were not explicitly requested; validate page markup separately")

    # ===== Miscellaneous Checks =====
    set_category("Miscellaneous")
    
    # Internal links
    internal_links = re.findall(r'\[.*?\]\((/[^)]+)\)', content)
    if min_internal_links is not None:
        check(f"Has at least {min_internal_links} internal links required by brief",
              len(internal_links) >= min_internal_links, 2,
              f"Detected: {len(internal_links)} internal links")
    else:
        skip("Internal link count gate", "minimum link count not provided; review contextual links against the site map")
    
    # CTA Check
    bad_ctas = ['contact us', 'learn more', 'click here', 'get started', 'read more']
    cta_section = content[content.lower().find('ready to'):] if 'ready to' in text_lower else ''
    has_bad_cta = any(phrase in cta_section.lower() for phrase in bad_ctas)
    check("Specific CTA (not generic)", not has_bad_cta, 3,
          "Use specific CTA text tied to page offer")
    
    # Word count is brief-dependent, not a universal SEO ranking requirement.
    word_count = len([w for w in words if len(w) > 2])
    results['word_count'] = word_count
    if min_words is not None or max_words is not None:
        lower_ok = min_words is None or word_count >= min_words
        upper_ok = max_words is None or word_count <= max_words
        check("Word count within approved brief range", lower_ok and upper_ok, 2,
              f"Current: {word_count}; brief range: {min_words or 'no minimum'}–{max_words or 'no maximum'}")
    else:
        skip("Word count gate", "no brief-specific word range supplied; word count reported for review")
    
    # ===== Calculate Final Score =====
    score_pct = (results['total_score'] / results['max_score'] * 100) if results['max_score'] > 0 else 0
    
    if score_pct >= 95:
        results['grade'] = 'A (95%+) — Very strong heuristic result; still complete evidence and human review'
    elif score_pct >= 90:
        results['grade'] = 'A- (90–94%) — Strong draft; verify evidence, intent and page-specific requirements'
    elif score_pct >= 85:
        results['grade'] = 'B+ (85–89%) — Good base; review flagged issues before finalizing'
    elif score_pct >= 70:
        results['grade'] = 'B (70–84%) — Revision recommended'
    elif score_pct >= 55:
        results['grade'] = 'C (55–69%) — Significant revisions recommended'
    else:
        results['grade'] = 'D (<55%) — Broad revision recommended'
    
    results['score_percentage'] = round(score_pct, 1)
    
    return results

def print_report(results: dict):
    print(f"\n{'='*60}")
    print(f"  SEO CONTENT QUALITY REPORT")
    print(f"{'='*60}")
    print(f"  Score: {results['total_score']}/{results['max_score']} ({results['score_percentage']}%)")
    print(f"  Grade: {results['grade']}")
    print(f"{'='*60}\n")
    
    print("CHECKS:")
    for check in results['checks']:
        print(f"  {check}")
    if results.get('skipped_checks'):
        print("\nSKIPPED / NOT IN SCOPE:")
        for item in results['skipped_checks']:
            print(f"  {item}")
    
    if results['warnings']:
        print(f"\nWARNINGS:")
        for w in results['warnings']:
            print(f"  {w}")
    
    if results['errors']:
        print(f"\nHIGH-WEIGHT CHECKS TO REVIEW (not automatic publication blockers):")
        for e in results['errors']:
            print(f"  {e}")
            
    print(f"\n{'='*60}")
    print("  SUMMARY STATISTICS")
    print(f"{'='*60}")
    print(f"  Total Checks Passed: {results['passed_checks']} / {results['total_checks']}")
    
    print("\n  Top 3 Weakest Areas:")
    sorted_weak = sorted(results['weak_areas'].items(), key=lambda x: x[1], reverse=True)
    for i, (cat, points_lost) in enumerate(sorted_weak[:3]):
        if points_lost > 0:
            print(f"  {i+1}. {cat} (-{points_lost} pts)")
            
    if results['warnings'] or results['errors']:
        print("\n  Suggested Priority Fixes:")
        all_issues = results['errors'] + results['warnings']
        for i, issue in enumerate(all_issues[:5]):
            print(f"  - {issue}")
    
    print(f"\n{'='*60}\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Advisory content linter; not a Google ranking score or publish authorization."
    )
    parser.add_argument("content_file", help="Markdown file containing the draft")
    parser.add_argument("primary_keyword", help="Primary keyword from the approved brief")
    parser.add_argument("--min-words", type=int, default=None,
                        help="Minimum word count from the brief (omit if not applicable)")
    parser.add_argument("--max-words", type=int, default=None,
                        help="Maximum word count from the brief (omit if not applicable)")
    parser.add_argument("--require-faq", action="store_true",
                        help="Require an FAQ section only when the approved brief calls for one")
    parser.add_argument("--schema-types", default="",
                        help="Comma-separated schema types expected in this file; omit if schema is validated separately")
    parser.add_argument("--min-internal-links", type=int, default=None,
                        help="Minimum Markdown internal links required by the brief")
    args = parser.parse_args()

    if args.min_words is not None and args.max_words is not None and args.min_words > args.max_words:
        parser.error("--min-words cannot be greater than --max-words")

    try:
        with open(args.content_file, encoding="utf-8") as file:
            draft = file.read()
    except OSError as exc:
        parser.error(f"could not read content file: {exc}")

    schema_types = [item.strip() for item in args.schema_types.split(",") if item.strip()]
    results = score_content(
        draft,
        args.primary_keyword,
        min_words=args.min_words,
        max_words=args.max_words,
        require_faq=args.require_faq,
        schema_types=schema_types or None,
        min_internal_links=args.min_internal_links,
    )
    print_report(results)
    print("NOTE: This is a heuristic editorial lint report. It does not estimate Google rankings or replace source verification / technical SEO audits.")
