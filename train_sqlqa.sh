set -xeuo pipefail

export ALLOW_WANDB=true
modal run --detach src.train --config=config/mistral.yml --data=data/sqlqa.jsonl
