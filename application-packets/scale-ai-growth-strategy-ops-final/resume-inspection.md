# Resume Inspection — Scale AI

Resume inspected: `Dev-Chandra-Patel-Resume-Scale-AI.pdf`  
Original source: `profile/source-files/Resume_Dev_C_Patel.pdf`  
Result: **Use original PDF for this Greenhouse submission, with caveats below.**

## Technical parse check

- PDF type: text-based PDF, not scanned/image-only.
- PDF metadata: Google Docs renderer, 2 pages, tagged, unencrypted.
- Text extraction worked cleanly with `pdftotext`.
- Contact information extracted correctly:
  - Name
  - San Francisco, CA
  - Phone
  - Email
  - LinkedIn
- Standard section headings extracted correctly:
  - SUMMARY
  - PROFESSIONAL EXPERIENCE
  - EDUCATION AND TRAINING
  - ADDITIONAL INFORMATION

## Visual inspection

Both rendered pages are clean, readable, professional, and single-column. The layout is conservative and appropriate for Greenhouse/ATS parsing.

Strengths:

- Clear name/contact block at top.
- Single-column chronology.
- Standard section headers.
- Simple bullet structure.
- Strong quantified achievements in the top third: 26K+ subscribers, ~45% open rates, 8K LinkedIn followers, 30+ events.
- Two-page length is appropriate for 10+ years of technical/operator experience.
- Security clearance appears in Additional Information and is phrased broadly enough for non-cleared private-sector applications.

Potential issues / caveats:

- Bullets use a bullet glyph that extracts as `●` plus a zero-width-looking marker in text. It still parsed, but a generated DOCX/plainer PDF would be slightly safer for stricter ATS systems.
- Resume is broadly strong but not as tightly tailored to Scale AI as the markdown tailored draft. It does not explicitly mention `Growth Strategy & Operations Lead`, `Generative AI`, `SQL`, `Python`, `GTM`, or `revenue expansion` in the top summary.
- For Greenhouse specifically, a clean text-based PDF is acceptable and often preferable because recruiters view the original attachment inline.

## Best-practice research summary

Greenhouse accepts `.doc`, `.docx`, `.pdf`, `.rtf`, and `.txt`. For Greenhouse, a clean text-based PDF is acceptable. Across ATS systems generally, safest formatting is:

- Single column.
- Standard section headers.
- Text-based PDF or DOCX; never scanned/image-only PDF.
- Contact info in body text.
- Consistent dates.
- Keywords from the job description integrated truthfully in summary and experience bullets.
- Avoid tables, text boxes, graphics, and keyword stuffing.

Security clearance best practice:

- It is acceptable to disclose an active clearance when relevant.
- Use general phrasing unless applying to a cleared role.
- Avoid investigation dates, clearance identifiers, classified program names, or agency/system details.
- Recommended general phrasing for this application: `Active U.S. Government security clearance`.
- If specificity is useful: `Active U.S. Government Top Secret clearance; SCI eligible`.

## Recommendation

For the Scale AI Greenhouse application, use:

`application-packets/scale-ai-growth-strategy-ops-final/Dev-Chandra-Patel-Resume-Scale-AI.pdf`

Then, after upload, review the Greenhouse parsed fields before submitting. If Greenhouse mis-parses contact info, dates, or job history, stop and use a generated DOCX/tailored PDF instead.

## Optional improvement before submission

If we want a higher-fit version without changing the visual style too much, generate a tailored PDF/DOCX from `tailored-resume.md` and visually inspect it before replacing the original. This would improve keyword alignment for Scale AI but may take more time and introduces formatting risk unless carefully rendered and inspected.
