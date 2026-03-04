FROM odoo:17.0
USER root
RUN pip install pytest-odoo pytest-cov
USER odoo