### Configuration and multi-file skills

1. name and description are required — allowed-tools and model are optional but powerful additions. 
2. A good description answers two questions: What does the skill do? When should Claude use it?
3. allowed-tools restricts which tools Claude can use when the skill is active — useful for read-only or security-sensitive workflows

**Progressive disclosure: keep SKILL.md under 500 lines and link to supporting files (references, scripts, assets) that Claude reads only when needed** 

Scripts execute without loading their contents into context — only the output consumes tokens, keeping context efficient