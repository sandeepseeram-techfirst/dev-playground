### Configuration and multi-file skills

1. name and description are required — allowed-tools and model are optional but powerful additions. 
2. A good description answers two questions: What does the skill do? When should Claude use it?
3. allowed-tools restricts which tools Claude can use when the skill is active — useful for read-only or security-sensitive workflows

**Progressive disclosure: keep SKILL.md under 500 lines and link to supporting files (references, scripts, assets) that Claude reads only when needed** 

Scripts execute without loading their contents into context — only the output consumes tokens, keeping context efficient. 

### Skill Metadata Fields
The agent skills open standard supports several fields in the SKILL.md frontmatter. Two are required, and the rest are optional:

1. name (required) — Identifies your skill. Use lowercase letters, numbers, and hyphens only. Maximum 64 characters. Should match your directory name.
2. description (required) — Tells Claude when to use the skill. Maximum 1,024 characters. This is the most important field because Claude uses it for matching.
3. allowed-tools (optional) — Restricts which tools Claude can use when the skill is active.
4. model (optional) — Specifies which Claude model to use for the skill.

### Example
---
name: codebase-onboarding
description: Helps new developers understand the system works.
allowed-tools: Read, Grep, Glob, Bash
model: sonnet
---