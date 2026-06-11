# Cohort Skill Improvement Notes — early-stage-and-big-tech-applications

After preparing the P0/P1 growth + AI cohort, recommended skill/workflow improvements:

1. Add a built-in `live_posting_inspection` checklist that records: canonical URL, direct apply URL, HTTP status, open/closed evidence, source snippets, compensation, location, and application route.
2. Add Ashby form extraction support. The Lavendo and Giga pages exposed required fields in embedded Ashby form definitions; automating extraction of required fields/options would speed future packets.
3. Add an ambiguity guard for same-name companies. Concourse produced two plausible companies/roles: Concourse Tech govtech and Concourse AI finance. The skill should explicitly force a company/domain disambiguation section before drafting materials.
4. Add a `hard_filter_risk` section to packets for requirements such as MBB review memos/performance ratings, NYC-only in-office, or below-target compensation.
5. Standardize packet filenames: `README.md`, `job-posting.md`, `application-answers.md`, `recruiter-outreach.md`, `form-inspection.md`, even when an existing packet uses platform-specific names like `greenhouse-form-inspection.md`.
6. Add a no-send/no-submit final checklist to every generated outreach file.
