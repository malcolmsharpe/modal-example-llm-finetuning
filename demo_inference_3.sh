set -xeuo pipefail

# The example from the readme.
modal run -q src.inference --prompt "[INST] Using the schema context below, generate a SQL query that answers the question.
CREATE TABLE records (label VARCHAR, value VARCHAR)
List the label and value of all records. [/INST]"

# Expect:
# [SQL] SELECT label, value FROM records [/SQL]
