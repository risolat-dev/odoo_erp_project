test:
	@docker-compose exec -u root web /bin/bash -c " \
		export PYTHONPATH=\$$PYTHONPATH:/mnt/extra-addons && \
		python3 /usr/bin/odoo -d postgres --db_host=db --db_user=odoo --db_password=odoo --stop-after-init \
			-i sale_approval_custom && \
		python3 -m coverage run --source=/mnt/extra-addons \
			--omit='*/__manifest__.py,*/__init__.py,*/tests/*' -m pytest /mnt/extra-addons && \
		python3 -m coverage report -m"