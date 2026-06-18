# Link governance

## Permanent semantic URLs

- Published articles use `/go/<slug>` links.
- A slug is never deleted after publication.
- Renamed concepts redirect to a successor and retain a tombstone explanation.
- Physical page locations may change without breaking article links.

## Automated checks

- `scripts/check_internal_links.py` validates local HTML, CSS, JavaScript, images, and redirects. Internal breakage fails CI.
- `scripts/check_external_links.py` refreshes external status and writes `data/link-health.json`.
- `.github/workflows/check-links.yml` runs on pull requests and pushes.
- `.github/workflows/refresh-link-status.yml` runs weekly and may commit refreshed status.

## External link failures

External failures are warnings until repeated. Prefer DOI, institutional repository, arXiv, HAL, or publisher identifiers. Do not mirror copyrighted material merely to avoid a dead link.
