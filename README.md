
data flow by dagster dbt dlt

# .venv

``` bash
uv sync
```

# dbt project

## profiles.yml

create ./dbt_project/profiles.yml

``` yaml
dbt_project:
  target: dev
  outputs:
    dev:
      type: clickhouse
      host: <>
      port: <>
      user: <>
      password: <>
      schema: dataflow_dev
```

## dagster project

``` bash

cd dagster_project

dg list defs


dg dev
```

visit: http://localhost:3000