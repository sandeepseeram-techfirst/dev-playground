### Skills vs. CLAUDE.md vs. Slash Commands

**What are Agent Skills?**  
Agent Skills are a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows.

Claude Code has several ways to customize behavior. Skills are unique because they're automatic and task-specific. Here's how they compare:

**CLAUDE.md** files load into every conversation. If you want Claude to always use TypeScript's strict mode, that goes in CLAUDE.md.

**Skills** load on demand when they match your request. Claude only loads the name and description initially, so they don't fill up your entire context window. Your PR review checklist doesn't need to be in context when you're debugging — it loads when you actually ask for a review.

**Slash commands** require you to explicitly type them. Skills don't. Claude applies them when it recognizes the situation.

### When to Use Skills
Skills work best for specialized knowledge that applies to specific tasks: 

1. Code review standards your team follows
2. Commit message formats you prefer
3. Brand guidelines for your organization
4. Documentation templates for specific types of docs
5. Debugging checklists for particular frameworks


### Key takeaways
1. A skill is a directory containing a SKILL.md file with metadata (name, description) in frontmatter. 
2. Claude loads only skill names and descriptions at startup, then matches incoming requests against those descriptions using semantic matching. 
3. You get a confirmation prompt before Claude loads the full skill content into context.
4. Priority for name conflicts: Enterprise → Personal → Project → Plugins
5. To update a skill, edit its SKILL.md. To remove one, delete its directory. Always restart Claude Code for changes to take effect. 

### Skill Priority
If you clone a repository that has a skill with the same name as one of your personal skills, which one wins? There's a clear priority order:

1. Enterprise — managed settings, highest priority
2. Personal — your home directory (~/.claude/skills)
3. Project — the .claude/skills directory inside a repository
4. Plugins — installed plugins, lowest priority

This lets organizations enforce standards through enterprise skills while still allowing individual customization. If your company has an enterprise "code-review" skill and you create a personal "code-review" skill with the same name, the enterprise version takes precedence.