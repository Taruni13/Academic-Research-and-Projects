# Blinkit — Power BI Sales Dashboard

Preview
- Screenshot: `https://drive.google.com/file/d/1Cph1JuwXNFt8VrxyKgPohwvlQ95FZY6P/view?usp=sharing`
- Vedio Link: `https://drive.google.com/file/d/14PE6nzXPZdSxjPwZNL9IRuxuxofyP4q6/view?usp=sharing`

Overview
- Power BI dashboard built from Blinkit sales data showcasing key business metrics and item-level analytics.
- Designed for exploratory analysis and executive summary reporting.

Key visuals (as in attached screenshot)
- KPI cards: Total Sales, Avg Sales, Average Rating, Sum of Item Visibility.
- Gauge: Count of Outlet Location Type with numeric center value.
- Treemap: Count of Outlet Size by Outlet Type.
- Pie chart: Sum of Rating by Item Type (legend with item categories).
- Bar chart: Count of Sales by Item Type (sorted descending).

Repository structure
- powerbi/
  - blinkit-dashboard.pbix — Power BI Desktop file (source)
  - blinkit-dashboard-screenshot.png — static preview image
- data/
  - sample-data.csv — anonymized or representative dataset used to create the report
- docs/ (optional exports and notes)
- README.md
- .gitignore
- .gitattributes (when using Git LFS)
- LICENSE

How to open the report
1. Install Power BI Desktop (Windows). macOS users can run Power BI via Parallels/VM or use Power BI Web for published reports.
2. Open `powerbi/blinkit-dashboard.pbix` in Power BI Desktop.
3. If the report is linked to an external data file, point data connections to `data/sample-data.csv` or your dataset and refresh.

Data and privacy
- Do not commit sensitive or personally identifiable data. Include only anonymized or sample data in `data/`.
- If the original dataset is large or confidential, add a small representative CSV and link to a secure storage location for the full data.

Versioning large files
- If `.pbix` >100 MB, use Git LFS:
  - Install: `brew install git-lfs`
  - Initialize: `git lfs install`
  - Track pbix: `git lfs track "*.pbix"`
  - Commit the generated `.gitattributes` and your large file.

Suggested commits and tags
- Initial commit: Add PBIX, sample data, screenshot, README and license.
- Tag releases when publishing major dashboard updates and attach large PBIX files to GitHub Releases if not stored in Git LFS.

Notes
- Consider adding a short walkthrough in `docs/` describing key measures and DAX formulas used to build the KPIs and visuals.
