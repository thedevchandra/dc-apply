# Notion Sync — 2026-06-11

The application tracker was mirrored into Notion after the user pointed out that applications were not being recorded there.

## Notion page created

- Title: Application Tracker Sync — 2026-06-11 10:38
- URL: https://app.notion.com/p/Application-Tracker-Sync-2026-06-11-10-38-37c421f1b33681e8ad73e10deb2594ae
- Page ID: 37c421f1-b336-81e8-ad73-e10deb2594ae

## Contents

The page includes:

- Confirmed submitted applications: Ambience Healthcare, GigaML
- Filled/attempted/not-confirmed applications: Scale AI, Pallet, Trail of Bits, Altara, Broccoli AI
- Needs-research roles
- Archived/deprioritized roles
- Immediate action-item checklist

## Important implementation note

The existing Notion `dc-apply` page has child database views named `View: Tasks` and `View: Notes`, but direct database schema retrieval from those child block IDs returned HTTP 400. For this sync, a dedicated child page was created under the `dc-apply` Notion page instead of writing rows into those database views.

Future runs should either:

1. Continue appending/updating Notion child pages under `dc-apply`, or
2. Resolve the actual source database IDs for Tasks/Notes before row-level writes.
