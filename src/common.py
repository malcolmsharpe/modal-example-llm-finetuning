import os
from pathlib import PurePosixPath
from typing import Union

import modal

APP_NAME = "example-axolotl"

MINUTES = 60  # seconds
HOURS = 60 * MINUTES

# Axolotl image hash corresponding to main-py3.11-cu121-2.3.1
AXOLOTL_REGISTRY_SHA = (
    "66e62f6ec3d3bb2a8471e830945aeae653cc624ae5c9307967ad84ada1e409ae"
)

ALLOW_WANDB = os.environ.get("ALLOW_WANDB", "false").lower() == "true"

axolotl_image = (
    modal.Image.from_registry(f"axolotlai/axolotl@sha256:{AXOLOTL_REGISTRY_SHA}")
    .pip_install(
        "huggingface_hub==0.26.2",
        "hf-transfer==0.1.8",
        "wandb==0.18.7",
        "fastapi==0.115.5",
        "pydantic==2.9.2",
    )
    .env(
        dict(
            HUGGINGFACE_HUB_CACHE="/pretrained",
            HF_HUB_ENABLE_HF_TRANSFER="1",
            TQDM_DISABLE="true",
            AXOLOTL_NCCL_TIMEOUT="60",
        )
    )
    .entrypoint([])
)

vllm_image = (
    modal.Image.from_registry("nvidia/cuda:12.4.0-base-ubuntu22.04", add_python="3.11")
    .pip_install(
        "vllm==0.6.4.post1",
        "torch==2.5.1",
    )
    .entrypoint([])
)

app = modal.App(
    APP_NAME,
    secrets=[
        modal.Secret.from_name("my-huggingface-secret"),
        modal.Secret.from_dict({"ALLOW_WANDB": os.environ.get("ALLOW_WANDB", "false")}),
        *([modal.Secret.from_name("wandb")] if ALLOW_WANDB else []),
    ],
)

# Volumes for pre-trained models and training runs.
pretrained_volume = modal.Volume.from_name(
    "example-pretrained-vol", create_if_missing=True
)
runs_volume = modal.Volume.from_name("example-runs-vol", create_if_missing=True)
VOLUME_CONFIG: dict[Union[str, PurePosixPath], modal.Volume] = {
    "/pretrained": pretrained_volume,
    "/runs": runs_volume,
}


class Colors:
    """ANSI color codes"""

    GREEN = "\033[0;32m"
    BLUE = "\033[0;34m"
    GRAY = "\033[0;90m"
    BOLD = "\033[1m"
    END = "\033[0m"
