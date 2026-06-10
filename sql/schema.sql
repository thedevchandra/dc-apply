-- dc-apply local SQLite schema
-- Purpose: local application tracker without modifying the Notion task database.
-- Canonical local DB path: data/dc_apply.sqlite3

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS search_brief (
  id INTEGER PRIMARY KEY CHECK (id = 1),
  primary_role_targets TEXT NOT NULL,
  stage_preferences TEXT NOT NULL,
  domain_preferences TEXT NOT NULL,
  location_preferences TEXT NOT NULL,
  compensation_expectations TEXT NOT NULL,
  operating_mode TEXT NOT NULL,
  privacy_blocklist TEXT NOT NULL,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS roles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  company TEXT NOT NULL,
  role_title TEXT NOT NULL,
  role_type TEXT,
  domain TEXT,
  stage TEXT,
  location TEXT,
  work_mode TEXT,
  compensation TEXT,
  url TEXT,
  source TEXT NOT NULL DEFAULT 'Manual Research',
  priority TEXT NOT NULL DEFAULT 'P2',
  fit_score INTEGER CHECK (fit_score IS NULL OR (fit_score >= 0 AND fit_score <= 100)),
  status TEXT NOT NULL DEFAULT 'Discovered' CHECK (status IN (
    'Discovered', 'Shortlisted', 'Needs Research', 'Ready to Apply', 'Applied',
    'Follow-up Needed', 'Recruiter Screen', 'Interviewing', 'Offer', 'Rejected', 'Archived'
  )),
  resume_variant TEXT CHECK (resume_variant IS NULL OR resume_variant IN (
    'Head of Growth', 'Founding Operator / Chief of Staff', 'Defense / GovTech / DeepTech'
  )),
  pitch_status TEXT NOT NULL DEFAULT 'Not Started' CHECK (pitch_status IN (
    'Not Started', 'Drafted', 'Ready for Review', 'Approved', 'Sent'
  )),
  applied_date TEXT,
  follow_up_date TEXT,
  contact TEXT,
  notes TEXT,
  archived_reason TEXT,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(company, role_title, source)
);

CREATE TABLE IF NOT EXISTS role_scores (
  role_id INTEGER PRIMARY KEY REFERENCES roles(id) ON DELETE CASCADE,
  role_fit INTEGER NOT NULL DEFAULT 0 CHECK (role_fit BETWEEN 0 AND 25),
  domain_fit INTEGER NOT NULL DEFAULT 0 CHECK (domain_fit BETWEEN 0 AND 20),
  location_work_mode_fit INTEGER NOT NULL DEFAULT 0 CHECK (location_work_mode_fit BETWEEN 0 AND 15),
  compensation_fit INTEGER NOT NULL DEFAULT 0 CHECK (compensation_fit BETWEEN 0 AND 15),
  company_stage_fit INTEGER NOT NULL DEFAULT 0 CHECK (company_stage_fit BETWEEN 0 AND 10),
  background_resonance INTEGER NOT NULL DEFAULT 0 CHECK (background_resonance BETWEEN 0 AND 10),
  freshness_likelihood INTEGER NOT NULL DEFAULT 0 CHECK (freshness_likelihood BETWEEN 0 AND 5),
  rationale TEXT,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE VIEW IF NOT EXISTS role_score_totals AS
SELECT
  r.id,
  r.company,
  r.role_title,
  r.priority,
  r.status,
  (
    COALESCE(s.role_fit, 0) +
    COALESCE(s.domain_fit, 0) +
    COALESCE(s.location_work_mode_fit, 0) +
    COALESCE(s.compensation_fit, 0) +
    COALESCE(s.company_stage_fit, 0) +
    COALESCE(s.background_resonance, 0) +
    COALESCE(s.freshness_likelihood, 0)
  ) AS computed_fit_score
FROM roles r
LEFT JOIN role_scores s ON s.role_id = r.id;

CREATE TABLE IF NOT EXISTS application_materials (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  role_id INTEGER NOT NULL REFERENCES roles(id) ON DELETE CASCADE,
  material_type TEXT NOT NULL CHECK (material_type IN ('resume', 'cover_letter', 'founder_outreach', 'recruiter_message', 'notes')),
  file_path TEXT,
  content TEXT,
  status TEXT NOT NULL DEFAULT 'Draft' CHECK (status IN ('Draft', 'Ready for Review', 'Approved', 'Sent', 'Archived')),
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS tasks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  role_id INTEGER REFERENCES roles(id) ON DELETE SET NULL,
  status TEXT NOT NULL DEFAULT 'Todo' CHECK (status IN ('Todo', 'In Progress', 'Done', 'Cancelled')),
  priority TEXT NOT NULL DEFAULT 'P2' CHECK (priority IN ('P0', 'P1', 'P2', 'P3')),
  due_date TEXT,
  notes TEXT,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TRIGGER IF NOT EXISTS roles_set_updated_at
AFTER UPDATE ON roles
FOR EACH ROW
BEGIN
  UPDATE roles SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

CREATE TRIGGER IF NOT EXISTS tasks_set_updated_at
AFTER UPDATE ON tasks
FOR EACH ROW
BEGIN
  UPDATE tasks SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;
