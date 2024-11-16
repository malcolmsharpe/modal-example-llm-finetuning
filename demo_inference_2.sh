set -xeuo pipefail

# An example from the training data.
# {"question": "What are the distinct creation years of the departments managed by a secretary born in state 'Alabama'?", "context": "CREATE TABLE department (creation VARCHAR, department_id VARCHAR); CREATE TABLE management (department_id VARCHAR, head_id VARCHAR); CREATE TABLE head (head_id VARCHAR, born_state VARCHAR)", "answer": "[SQL] SELECT DISTINCT T1.creation FROM department AS T1 JOIN management AS T2 ON T1.department_id = T2.department_id JOIN head AS T3 ON T2.head_id = T3.head_id WHERE T3.born_state = 'Alabama' [/SQL]"}
#         [INST] Using the schema context below, generate a SQL query that answers the question.
#        {input}
#        {instruction} [/INST]
modal run -q src.inference --prompt "[INST] Using the schema context below, generate a SQL query that answers the question.
CREATE TABLE department (creation VARCHAR, department_id VARCHAR); CREATE TABLE management (department_id VARCHAR, head_id VARCHAR); CREATE TABLE head (head_id VARCHAR, born_state VARCHAR)
What are the distinct creation years of the departments managed by a secretary born in state 'Alabama'? [/INST]"

# Expect:
#[SQL] SELECT DISTINCT T1.creation FROM department AS T1 JOIN management AS T2 ON T1.department_id = T2.department_id JOIN head AS T3 ON T2.head_id = T3.head_id WHERE T3.born_state = 'Alabama' [/SQL]
