### Progressive Disclosure 

Skills share Claude's context window with your conversation. When Claude activates a skill, it loads the contents of that SKILL.md into context. But sometimes you need references, examples, or utility scripts that the skill depends on.

Cramming everything into one 2,000-line file has two problems: it takes up a lot of context window space, and it's not fun to maintain.

**Progressive disclosure solves this.** Keep essential instructions in SKILL.md and put detailed reference material in separate files that Claude reads only when needed.

The open standard suggests organizing your skill directory with:

scripts/ — Executable code
references/ — Additional documentation
assets/ — Images, templates, or other data files