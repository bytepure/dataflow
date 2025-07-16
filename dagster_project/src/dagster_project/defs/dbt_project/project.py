import dagster as dg

from pathlib import Path
from dagster_dbt import DbtProject, DbtCliResource

dbt_project_dir = Path(__file__).joinpath("..", "..", "..","..","..","..", "dbt_project").resolve()

dbt_resource = DbtCliResource(project_dir=dbt_project_dir)

dbt_project = DbtProject(
    project_dir=dbt_project_dir,
    # packaged_project_dir=Path(__file__).joinpath("..", "..", "dbt-project").resolve(),
)

@dg.definitions
def resources():
    return dg.Definitions(
        # Provide the dictionary of resources to `Definitions`
        resources={
            "dbt_project": dbt_resource,
        }
    )
