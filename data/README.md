# Local SQLite Tracker

This repo has a local SQLite tracker at:

```text
data/dc_apply.sqlite3
```

It is intentionally separate from Notion so we can track roles and application prep without changing the existing Notion task database too much.

## Initialize / reseed

```bash
python3 scripts/init_db.py
```

The seed script is idempotent for the search brief and role list.

## Inspect roles

```bash
sqlite3 data/dc_apply.sqlite3 \
  "SELECT priority, company, role_title, status, fit_score FROM roles ORDER BY priority, fit_score DESC;"
```

## Tables

- `search_brief` — current career-search strategy.
- `roles` — application opportunities.
- `role_scores` — detailed 100-point scoring rubric.
- `application_materials` — drafted resumes, cover letters, outreach, and notes.
- `tasks` — local review/prep tasks, separate from Notion Tasks.

## Notion policy

Do not mutate the existing Notion Tasks database for routine local tracking. If Notion sync is needed later, sync from this SQLite database into a dedicated Applications database or a small number of explicit review tasks.
