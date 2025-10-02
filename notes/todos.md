# Todos

- BQ Utils
    * [ ] Get BQ Table from Table Path
    * [ ] 
- CI/CD
    * [X] staging and prod can only be changed via PR
    * need to make PR to merge staging->prod and dev->staging
    * staging can only be merged from dev; prod can only be merged from staging
    * when prod is merged, merge prod into staging and dev

- How will backfill be handled?
- Store extraction in bucket
- Only touch transformation jobs and run test on them
- Merge prod -> staging -> prod once a month (backmerging)
- Split => DE owns Extract; DS owns transformation

