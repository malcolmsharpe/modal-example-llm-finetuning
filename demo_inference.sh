set -xeuo pipefail

# The example from the readme.
modal run -q src.inference --prompt "[INST] Using the schema context below, generate a SQL query that answers the question.
CREATE TABLE head (name VARCHAR, born_state VARCHAR, age VARCHAR)
List the name, born state and age of the heads of departments ordered by name. [/INST]"

# Expect:
# [SQL] SELECT name, born_state, age FROM head ORDER BY name [/SQL]
