# TODO - Export PDF Route

## Task
Add a perfect `export_pdf` route in `app.py` so any generated report downloads as PDF.

## Steps
- [x] 1. Analyze the codebase (reports route, helpers, reportlab usage)
- [x] 2. Get plan approval
- [x] 3. Add helper to recompute report data (shared logic)
- [x] 4. Add `export_pdf` route that generates the PDF via reportlab
- [x] 5. Wire up / verify the reports.html "Download PDF" button link
- [x] 6. Test the route (syntax compile check passed)

## Task 2 - Export Excel
- [x] 1. Restore missing export_excel route (fixes reports page 500 error)
- [x] 2. Reports page loads without error (route registered & app reloads cleanly)
