# Form Inspection — Trail of Bits Workable

No submission was made.

## Access

- Official URL: https://apply.workable.com/trailofbits/j/339AC566C5/
- Public page accessible.
- Workable API checked: `https://apply.workable.com/api/v1/accounts/trailofbits/jobs/339AC566C5`
- API status: `state: published`, `approvalStatus: approved`.

## Form visibility

The static Workable page and public job API exposed posting details but not application form questions. Attempts to locate common form/question endpoints returned 404 or app shell HTML. The application form likely renders client-side once the apply flow is opened.

## Expected standard fields

Based on Workable norms, expect:

- Resume upload
- Name
- Email
- Phone
- Location
- LinkedIn / website
- Cover letter or message, possibly optional
- Work authorization / sponsorship
- EEOC demographic fields, veteran status, disability self-ID, possibly optional/prefer-not-to-answer

## Recommended defaults

- Work authorization: U.S. citizen; authorized to work in U.S.; no sponsorship required.
- Location: San Francisco, CA; open to remote U.S.
- Veteran: Yes if required.
- Disability: Prefer not to answer if required.
- Demographics: follow user defaults; avoid unnecessary disclosure.
- Clearance: do not over-disclose unless asked; use general `active U.S. Government security clearance` if relevant.

## Blockers / notes

- Before final submission, user should open the Workable apply form and check for any custom questions about technical/security engineering background, AI tooling, remote work, compensation, or restrictive agreements.
- Do not infer or answer restrictive-agreement questions without user confirmation.
