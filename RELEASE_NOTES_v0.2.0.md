# Diderot MMALS/ML Wiki v0.2.0

## Research chronicle release

This release adds the historical and traceability layer requested for the MMALS research program.

### New public sections

- The MMALS story in six chapters
- Interactive research chronicle with branch, event-type, and provenance filters
- Research branch map with maturity, claim boundary, repositories, and next step
- GitHub repository registry for 20 verified public repositories plus local/planned MMALS repositories
- Publication pipeline separating GitHub publication, arXiv, HAL, DOI, submission, and venue status
- Provenance policy for curating project conversations without exposing raw chat transcripts

### New machine-readable data

- `data/research-events.json`
- `data/branches.json`
- `data/repositories.json`
- `data/publications.json`
- `data/github-live.json`

### Automation

- weekly GitHub public-repository refresh
- internal-link validation preserved
- external-link health refresh preserved

### Scientific boundary

Repository activity and public availability do not automatically change scientific evidence status. Branch maturity remains reviewed metadata.
