#!/usr/bin/env python3
"""
SERP Extractor helpers — Browser Harness context only.
Extracts candidate title/meta/heading, PAA, related-search, schema, and citation
signals from Google SERPs and competitor pages.

Important: this module calls Browser Harness-provided helpers such as `js`,
`goto_url`, `wait_for_load`, and `new_tab`; it is not a standalone web scraper.
Google DOM selectors are volatile. Verify returned values in the live page and
mark a field Unknown when the selector did not observe it. Do not infer missing
SERP features from an empty selector result.
"""

def extract_serp_data():
    """Extract all SERP signals from current Google results page."""
    
    # Extract organic results
    results = js("""
        Array.from(document.querySelectorAll('div[data-sokoban-container] a[href^="http"], \
                                              div.g a[href^="http"]'))
            .filter(a => !a.closest('[data-text-ad]'))
            .slice(0, 10)
            .map(a => ({
                url: a.href,
                title: a.querySelector('h3')?.innerText || a.innerText,
                parent: a.closest('div[data-sokoban-container]')?.innerText?.slice(0, 200) || ''
            }))
    """)
    
    # Extract PAA questions
    paa = js("""
        Array.from(document.querySelectorAll('[data-q]'))
            .map(q => q.getAttribute('data-q'))
            .filter(Boolean)
    """)
    
    # Extract related searches
    related = js("""
        Array.from(document.querySelectorAll('div[data-q], .k8XOCe, a.Q71vJc'))
            .map(el => el.innerText.trim())
            .filter(t => t.length > 0 && t.length < 100)
            .slice(0, 12)
    """)
    
    # Check for featured snippet
    featured = js("""
        const snippet = document.querySelector('[data-attrid="wa:/description"], .ILfuVd, .hgKElc');
        return snippet ? snippet.innerText : null;
    """)
    
    return {
        'organic_results': results,
        'paa_questions': paa,
        'related_searches': related,
        'featured_snippet': featured
    }


def extract_ai_overview():
    """Check if Google AI Overview is present and extract text and sources."""
    ai_overview = js("""
        const aiContainer = document.querySelector('.ai-overview, [data-md="61"]'); // Try common classes or data-md for AI overview
        if (!aiContainer) return null;
        
        const text = aiContainer.innerText || '';
        const sources = Array.from(aiContainer.querySelectorAll('a[href^="http"]'))
                             .map(a => a.href)
                             .filter((value, index, self) => self.indexOf(value) === index);
                             
        return { text: text, sources: sources };
    """)
    return ai_overview


def extract_competitor_content(url):
    """Extract content structure from a competitor page."""
    
    # Navigate to competitor page
    goto_url(url)
    wait_for_load()
    
    # Extract content signals
    data = js("""
        ({
            title: document.title,
            metaDescription: document.querySelector('meta[name="description"]')?.content || '',
            h1: document.querySelector('h1')?.innerText || '',
            h2s: Array.from(document.querySelectorAll('h2')).map(h => h.innerText),
            h3s: Array.from(document.querySelectorAll('h3')).map(h => h.innerText),
            wordCount: document.body.innerText.split(/\\s+/).length,
            hasFAQ: !!document.querySelector('[itemtype*="FAQPage"], [class*="faq"], [id*="faq"]'),
            ctaTexts: Array.from(document.querySelectorAll('a[href*="contact"], a[href*="demo"], \
                                                            button, .cta, [class*="cta"]'))
                        .map(el => el.innerText.trim())
                        .filter(t => t.length > 0 && t.length < 50)
                        .slice(0, 5),
            schemaTypes: Array.from(document.querySelectorAll('script[type="application/ld+json"]'))
                        .map(s => { try { return JSON.parse(s.innerText)['@type']; } catch(e) { return null; } })
                        .filter(Boolean),
            publishDate: document.querySelector('time, [datetime], .date, [class*="date"]')?.getAttribute('datetime') 
                        || document.querySelector('time, .date')?.innerText || '',
            internalLinks: Array.from(document.querySelectorAll('a[href^="/"], a[href*="' + window.location.hostname + '"]'))
                        .length,
            externalLinks: Array.from(document.querySelectorAll('a[href^="http"]'))
                        .filter(a => !a.href.includes(window.location.hostname))
                        .length
        })
    """)
    
    return data


def extract_competitor_service_taxonomy(url):
    """Extract the service taxonomy (nav, footer, headings) from a competitor."""
    goto_url(url)
    wait_for_load()
    
    taxonomy = js("""
        ({
            navLinks: Array.from(document.querySelectorAll('nav a, header a'))
                .map(a => a.innerText.trim())
                .filter(t => t.length > 0 && t.length < 50),
            footerLinks: Array.from(document.querySelectorAll('footer a'))
                .map(a => a.innerText.trim())
                .filter(t => t.length > 0 && t.length < 50),
            h2s: Array.from(document.querySelectorAll('h2')).map(h => h.innerText.trim()),
            h3s: Array.from(document.querySelectorAll('h3')).map(h => h.innerText.trim())
        })
    """)
    return taxonomy


def check_llms_txt(domain):
    """Check if the domain has an /llms.txt file."""
    if not domain.startswith('http'):
        domain = 'https://' + domain
    domain = domain.rstrip('/')
    url = f"{domain}/llms.txt"
    
    goto_url(url)
    wait_for_load()
    
    content = js("document.body.innerText")
    
    if "404" in content.lower() or "not found" in content.lower() or not content.strip():
        return {"exists": False, "content": None}
        
    return {"exists": True, "content": content[:1000]} # Return first 1000 chars


def extract_google_trends(keyword, geo="US", date_range="today 5-y", category=0):
    """Navigate to Google Trends for the requested geography and time range.

    Trends values are relative-interest signals, not absolute keyword volume.
    The selectors below may stop working when Google's page structure changes.
    """
    import urllib.parse
    query = urllib.parse.urlencode({"q": keyword, "date": date_range, "geo": geo, "cat": category})
    url = f"https://trends.google.com/trends/explore?{query}"
    
    goto_url(url)
    wait_for_load()
    
    # Allow time for chart to render
    import time
    time.sleep(3)
    
    trend_data = js("""
        // Extract trend value (0-100 scale)
        const points = Array.from(document.querySelectorAll('.point'));
        const values = points.map(p => parseInt(p.getAttribute('data-y') || '0'));
        const recent = values.slice(-12); // Last 12 data points
        const older = values.slice(0, 12); // First 12 data points
        const recentAvg = recent.reduce((a,b) => a+b, 0) / recent.length;
        const olderAvg = older.reduce((a,b) => a+b, 0) / older.length;
        return {
            trend: recentAvg > olderAvg * 1.2 ? 'Rising' : recentAvg < olderAvg * 0.8 ? 'Declining' : 'Stable',
            recentAvg: Math.round(recentAvg),
            olderAvg: Math.round(olderAvg),
            momentum: Math.round((recentAvg - olderAvg) / Math.max(olderAvg, 1) * 100)
        };
    """)
    
    return trend_data


def check_perplexity_citations(keyword):
    """Check if competitors appear in Perplexity AI search results for keyword."""
    import urllib.parse
    
    goto_url(f"https://www.perplexity.ai/search?q={urllib.parse.quote(keyword)}")
    wait_for_load()
    
    import time
    time.sleep(5)  # Allow AI response to generate
    
    citations = js("""
        Array.from(document.querySelectorAll('a[href^="http"]'))
            .map(a => ({ url: a.href, text: a.innerText.trim() }))
            .filter(c => c.url && !c.url.includes('perplexity.ai'))
            .slice(0, 10)
    """)
    
    return citations


# Main execution example (run via browser-harness)
def run_serp_research(keyword, geo="US", trend_range="today 5-y", top_competitors=3):
    """Run the helper sequence from inside a connected Browser Harness session."""
    import urllib.parse
    search_url = "https://www.google.com/search?" + urllib.parse.urlencode({"q": keyword, "num": 10})
    new_tab(search_url)
    wait_for_load()
    serp_data = extract_serp_data()
    print("SERP Data:", serp_data)

    ai_overview = extract_ai_overview()
    print("AI Overview:", ai_overview)

    for result in serp_data.get('organic_results', [])[:max(0, top_competitors)]:
        url = result.get('url')
        if not url:
            continue
        print(f"Competitor [{url}]:", extract_competitor_content(url))
        print(f"Taxonomy [{url}]:", extract_competitor_service_taxonomy(url))
        try:
            domain = urllib.parse.urlparse(url).netloc
            print(f"llms.txt [{domain}]:", check_llms_txt(domain))
        except Exception as exc:
            print(f"llms.txt check failed for {domain if 'domain' in locals() else url}: {exc}")

    trend = extract_google_trends(keyword, geo=geo, date_range=trend_range)
    print(f"Trend [{keyword}] ({geo}, {trend_range}):", trend)
    citations = check_perplexity_citations(keyword)
    print("Perplexity citation sample:", citations)
    return {"keyword": keyword, "geo": geo, "serp": serp_data, "ai_overview": ai_overview,
            "trend": trend, "citation_sample": citations}


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description="Run inside a connected Browser Harness session; not standalone Python."
    )
    parser.add_argument("keyword", help="Keyword/query to research")
    parser.add_argument("--geo", default="US", help="Google Trends geography code, e.g. IN or US")
    parser.add_argument("--trend-range", default="today 5-y", help="Google Trends date range")
    parser.add_argument("--top-competitors", type=int, default=3)
    args = parser.parse_args()
    run_serp_research(args.keyword, geo=args.geo, trend_range=args.trend_range,
                      top_competitors=args.top_competitors)
