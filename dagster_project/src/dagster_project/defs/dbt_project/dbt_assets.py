from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets

from .project import dbt_project

@dbt_assets(manifest=dbt_project.manifest_path)
def dbt_project_dbt_assets(context: AssetExecutionContext, dbt_project: DbtCliResource):
    yield from dbt_project.cli(["build"], context=context).stream()