### Progressive Disclosure 

**Organize complex skills using progressive disclosure and multi-file structures.**

Skills share Claude's context window with your conversation. When Claude activates a skill, it loads the contents of that SKILL.md into context. But sometimes you need references, examples, or utility scripts that the skill depends on.

Cramming everything into one 2,000-line file has two problems: it takes up a lot of context window space, and it's not fun to maintain.

**Progressive disclosure solves this.** Keep essential instructions in SKILL.md and put detailed reference material in separate files that Claude reads only when needed.

The open standard suggests organizing your skill directory with:

scripts/ — Executable code
references/ — Additional documentation
assets/ — Images, templates, or other data files

### Using Scripts Efficiently
Scripts in your skill directory can run without loading their contents into context. The script executes and only the output consumes tokens. The key instruction to include in your SKILL.md is to tell Claude to run the script, not read it.

This is particularly useful for:

1. Environment validation
Data transformations that need to be consistent
Operations that are more reliable as tested code than generated code