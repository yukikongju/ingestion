run_profile:
	eval "$(direnv hook zsh)"
	direnv allow
	dbt run --profiles-dir ./.dbt
	# dbt run --profiles-dir ./.dbt --target dev
	# dbt run --profiles-dir ./.dbt --target prod
	#

verify_env:
	env | grep DBT
