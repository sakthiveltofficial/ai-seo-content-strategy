"""Smoke tests for scope-aware content-scorer behavior."""
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from content_scorer import score_content  # noqa: E402


class ContentScorerTests(unittest.TestCase):
    def test_page_specific_gates_are_skipped_when_unspecified(self):
        draft = """[TITLE TAG] AI-native company overview | Example\n[META DESCRIPTION] AI-native company overview for teams building software.\n\n# AI-Native Company Overview\n\n## What it is\nA definition of an AI-native company.\n\n## How it works\nA useful explanation.\n"""
        result = score_content(draft, "ai native company")
        skipped = "\n".join(result["skipped_checks"])
        self.assertIn("FAQ section", skipped)
        self.assertIn("Structured data", skipped)
        self.assertIn("Word count gate", skipped)
        self.assertIn("Internal link count gate", skipped)
        self.assertIn("word_count", result)

    def test_explicit_faq_and_word_range_are_checked(self):
        draft = """[TITLE TAG] AI-native company overview | Example\n[META DESCRIPTION] AI-native company overview for teams building software.\n\n# AI-Native Company Overview\n\n## What it is\nA definition of an AI-native company.\n\n## Frequently Asked Questions\n**What is an AI-native company?**\nA company designed around AI.\n"""
        result = score_content(draft, "ai native company", min_words=10, max_words=100, require_faq=True)
        combined = "\n".join(result["checks"])
        self.assertIn("Has FAQ section when required by brief", combined)
        self.assertIn("Word count within approved brief range", combined)


if __name__ == "__main__":
    unittest.main()
