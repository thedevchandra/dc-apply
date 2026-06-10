#!/usr/bin/env python3
"""Initialize/seed the local dc-apply SQLite tracker."""
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "dc_apply.sqlite3"
SCHEMA = ROOT / "sql" / "schema.sql"

SEARCH_BRIEF = {
    "id": 1,
    "primary_role_targets": "Head of Growth; Founding Operator / Chief of Staff; Product Management Leader",
    "stage_preferences": "Early-stage startups first; large tech second; mid-market / scale-up third",
    "domain_preferences": "Defense tech; GovTech; National security; Deep tech; Frontier AI; AI governance; AI infrastructure / devtools",
    "location_preferences": "San Francisco hybrid top preference; also Los Angeles, San Diego, Austin, NYC; in-office acceptable for the right opportunity",
    "compensation_expectations": "$180K-$250K base + meaningful equity for early-stage roles; flexible cash for exceptional upside; $250K-$400K+ TC for later-stage / large tech",
    "operating_mode": "Prepare applications and materials for Dev's review before submission; later transition approved categories to autonomous submission",
    "privacy_blocklist": "Context VC / context.vc",
}

ROLES = [
    ("Scale AI", "Growth Strategy & Operations Lead", "Growth Strategy / Ops", "AI", "Large Tech", "San Francisco", "Hybrid", "$180,800-$226,000 USD", None, "Jack & Jill", "P0", 88, "Head of Growth", "Strong SF hybrid AI growth/ops fit; brand and scale are compelling."),
    ("Concourse", "Head of Growth", "Head of Growth", "GovTech, AI", "Early-stage", "Remote", "Remote", "~$200K-$350K+ est", None, "Jack & Jill", "P0", 87, "Head of Growth", "Direct Head of Growth fit with gov software angle."),
    ("Concourse", "Chief of Staff", "Chief of Staff", "GovTech, AI", "Early-stage", "Remote", "Remote", None, None, "Jack & Jill", "P0", 84, "Founding Operator / Chief of Staff", "Gov software and founder-adjacent operating role."),
    ("Lavendo", "Chief of Staff – AI Governance", "Chief of Staff", "AI Governance", "Unknown", "San Francisco", "In office", "$250,000-$300,000", None, "Jack & Jill", "P1", 82, "Defense / GovTech / DeepTech", "AI governance plus SF location and strong compensation."),
    ("GigaML", "Chief Of Staff", "Chief of Staff", "AI", "Early-stage", "San Francisco", "In office", "~$180K-$400K+ est", None, "Jack & Jill", "P1", 80, "Founding Operator / Chief of Staff", "SF AI Chief of Staff role, likely strong operator fit."),
    ("Ambience Healthcare", "Chief of Staff", "Chief of Staff", "Vertical AI SaaS", "Growth", "San Francisco", "Hybrid", "~$250K-$400K+ est", None, "Jack & Jill", "P1", 78, "Founding Operator / Chief of Staff", "SF hybrid AI healthcare role with high ownership."),
    ("Broccoli AI", "Strategy & Operations Lead, Special Projects", "Strategy & Operations", "AI", "Early-stage", "San Francisco", "In office", "~$250K-$400K+ est", None, "Jack & Jill", "P1", 77, "Founding Operator / Chief of Staff", "Special projects/operator role in SF AI startup."),
    ("Pallet", "Chief of Staff", "Chief of Staff", None, "Early-stage", "San Francisco", "In office", "$175,000-$250,000", None, "Jack & Jill", "P2", 73, "Founding Operator / Chief of Staff", "SF Chief of Staff role; comp is acceptable but domain needs research."),
    ("Trail of Bits", "Chief of Staff", "Chief of Staff", "Security, Deep Tech", "Unknown", "Remote", "Remote", "~$175K-$250K est", None, "Jack & Jill", "P1", 79, "Defense / GovTech / DeepTech", "Security/deep-tech credibility and remote flexibility."),
    ("Altara", "Chief of Staff", "Chief of Staff", None, "Early-stage", "San Francisco", "In office", "~$180K-$250K+ est", None, "Jack & Jill", "P2", 72, "Founding Operator / Chief of Staff", "SF CoS role; requires domain/company research."),
    ("Knowtex", "Chief of Staff", "Chief of Staff", "AI", "Early-stage", "San Francisco", "Hybrid", "$180K-$250K base + equity est", None, "Jack & Jill", "P1", 78, "Founding Operator / Chief of Staff", "SF hybrid AI CoS role with comp in target range."),
    ("Darkhive, Inc", "Chief of Staff", "Chief of Staff", "Defense Tech", "Early-stage", "San Antonio / Remote unclear", "Remote", "~$250K-$400K+ est", None, "Jack & Jill", "P3", 60, "Defense / GovTech / DeepTech", "Archived/deprioritized because role appeared gone and/or location did not fit."),
]

TASKS = [
    ("Review initial priority role list", None, "Todo", "P0", "Confirm top roles before drafting materials."),
    ("Approve Head of Growth resume direction", None, "Todo", "P0", "Use Startup Intros growth, community, AI distribution, and GTM systems."),
    ("Approve Founding Operator / Chief of Staff resume direction", None, "Todo", "P0", "Use fundraising, company-building, Navy leadership, executive briefs, and ops cadence."),
    ("Approve Defense / GovTech / DeepTech resume direction", None, "Todo", "P1", "Use TS clearance, Naval Reactors, submarine maintenance, Booz Allen/SUBLANT, and CSIS."),
]

DB.parent.mkdir(parents=True, exist_ok=True)
with sqlite3.connect(DB) as con:
    con.execute("PRAGMA foreign_keys = ON")
    con.executescript(SCHEMA.read_text())
    con.execute(
        """INSERT INTO search_brief (
            id, primary_role_targets, stage_preferences, domain_preferences,
            location_preferences, compensation_expectations, operating_mode, privacy_blocklist
        ) VALUES (:id, :primary_role_targets, :stage_preferences, :domain_preferences,
            :location_preferences, :compensation_expectations, :operating_mode, :privacy_blocklist)
        ON CONFLICT(id) DO UPDATE SET
            primary_role_targets=excluded.primary_role_targets,
            stage_preferences=excluded.stage_preferences,
            domain_preferences=excluded.domain_preferences,
            location_preferences=excluded.location_preferences,
            compensation_expectations=excluded.compensation_expectations,
            operating_mode=excluded.operating_mode,
            privacy_blocklist=excluded.privacy_blocklist,
            updated_at=CURRENT_TIMESTAMP
        """,
        SEARCH_BRIEF,
    )
    for company, role_title, role_type, domain, stage, location, work_mode, compensation, url, source, priority, fit_score, resume_variant, notes in ROLES:
        status = "Archived" if company == "Darkhive, Inc" else "Shortlisted"
        archived_reason = "Role appeared gone and/or San Antonio location was not a fit." if company == "Darkhive, Inc" else None
        con.execute(
            """INSERT INTO roles (
                company, role_title, role_type, domain, stage, location, work_mode, compensation, url,
                source, priority, fit_score, status, resume_variant, notes, archived_reason
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(company, role_title, source) DO UPDATE SET
                role_type=excluded.role_type,
                domain=excluded.domain,
                stage=excluded.stage,
                location=excluded.location,
                work_mode=excluded.work_mode,
                compensation=excluded.compensation,
                url=excluded.url,
                priority=excluded.priority,
                fit_score=excluded.fit_score,
                status=excluded.status,
                resume_variant=excluded.resume_variant,
                notes=excluded.notes,
                archived_reason=excluded.archived_reason,
                updated_at=CURRENT_TIMESTAMP
            """,
            (company, role_title, role_type, domain, stage, location, work_mode, compensation, url, source, priority, fit_score, status, resume_variant, notes, archived_reason),
        )
    for title, role_id, status, priority, notes in TASKS:
        con.execute(
            """INSERT INTO tasks (title, role_id, status, priority, notes)
            SELECT ?, ?, ?, ?, ?
            WHERE NOT EXISTS (SELECT 1 FROM tasks WHERE title = ?)
            """,
            (title, role_id, status, priority, notes, title),
        )
    con.commit()

with sqlite3.connect(DB) as con:
    role_count = con.execute("SELECT COUNT(*) FROM roles").fetchone()[0]
    task_count = con.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]
    print(f"Initialized {DB}")
    print(f"roles={role_count} tasks={task_count}")
