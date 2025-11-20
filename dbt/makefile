run_profile:
	eval "$(direnv hook zsh)"
	direnv allow
	# dbt run --profiles-dir ./.dbt
	dbt run --profiles-dir ./.dbt --target dev
	# dbt run --profiles-dir ./.dbt --target prod
	#

debug:
	dbt debug

generate_docs:
	dbt docs generate --profiles-dir ./.dbt
	dbt docs serve --port 9000

verify_env:
	env | grep DBT
