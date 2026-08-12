#!/usr/bin/env python3

import re
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "design-review"


class RepositoryIntegrityTests(unittest.TestCase):
    def test_required_skill_files_exist(self):
        self.assertTrue((SKILL / "SKILL.md").is_file())
        self.assertTrue((SKILL / "agents" / "openai.yaml").is_file())

    def test_skill_frontmatter(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
        self.assertIsNotNone(match, "SKILL.md must start with YAML frontmatter")
        frontmatter = match.group(1)
        fields = [line.split(":", 1)[0] for line in frontmatter.splitlines() if ":" in line]
        self.assertEqual(fields, ["name", "description"])
        self.assertIn("name: design-review", frontmatter)

    def test_text_files_are_utf8(self):
        extensions = {".md", ".yaml", ".yml", ".py", ".ps1", ".json", ".txt"}
        for path in ROOT.rglob("*"):
            if path.is_file() and path.suffix.lower() in extensions and ".git" not in path.parts:
                with self.subTest(path=path.relative_to(ROOT)):
                    path.read_text(encoding="utf-8")

    def test_markdown_relative_links_resolve(self):
        pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
        for path in ROOT.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            for target in pattern.findall(text):
                if "://" in target or target.startswith("#") or target.startswith("mailto:"):
                    continue
                clean_target = target.split("#", 1)[0]
                with self.subTest(path=path.relative_to(ROOT), target=target):
                    self.assertTrue((path.parent / clean_target).exists())

    def test_installable_skill_contains_no_tests_or_caches(self):
        forbidden_parts = {"__pycache__", "tests", "dist"}
        for path in SKILL.rglob("*"):
            with self.subTest(path=path.relative_to(SKILL)):
                self.assertFalse(forbidden_parts.intersection(path.parts))
                self.assertFalse(path.suffix in {".pyc", ".pyo"})

    def test_release_archive_is_clean_when_present(self):
        archive = ROOT / "dist" / "design-review-v1.0.0.zip"
        if not archive.exists():
            self.skipTest("Release archive has not been built")
        with zipfile.ZipFile(archive) as package:
            names = package.namelist()
        self.assertIn("design-review/SKILL.md", [name.replace("\\", "/") for name in names])
        for name in names:
            normalized = name.replace("\\", "/")
            with self.subTest(name=normalized):
                self.assertTrue(normalized.startswith("design-review/"))
                self.assertNotIn("/__pycache__/", normalized)
                self.assertNotRegex(normalized, r"(^|/)test_[^/]*\.py$")
                self.assertNotRegex(normalized, r"\.py[co]$")


if __name__ == "__main__":
    unittest.main()
