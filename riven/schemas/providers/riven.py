from typing import Literal

from pydantic import Field

from riven.constants import DEFAULT_EMBEDDING_CHUNK_SIZE, riven_MODEL_ENDPOINT
from riven.schemas.embedding_config import EmbeddingConfig
from riven.schemas.enums import ProviderCategory, ProviderType
from riven.schemas.llm_config import LLMConfig
from riven.schemas.providers.base import Provider

riven_EMBEDDING_ENDPOINT = "https://embeddings.riven.com/"


class rivenProvider(Provider):
    provider_type: Literal[ProviderType.riven] = Field(ProviderType.riven, description="The type of the provider.")
    provider_category: ProviderCategory = Field(ProviderCategory.base, description="The category of the provider (base or byok)")
    base_url: str = Field(riven_EMBEDDING_ENDPOINT, description="Base URL for the riven API (used for embeddings).")

    async def list_llm_models_async(self) -> list[LLMConfig]:
        return [
            LLMConfig(
                model="riven-free",  # NOTE: renamed
                model_endpoint_type="openai",
                model_endpoint=riven_MODEL_ENDPOINT,
                context_window=30000,
                handle=self.get_handle("riven-free"),
                max_tokens=self.get_default_max_output_tokens("riven-free"),
                provider_name=self.name,
                provider_category=self.provider_category,
            )
        ]

    async def list_embedding_models_async(self):
        return [
            EmbeddingConfig(
                embedding_model="riven-free",  # NOTE: renamed
                embedding_endpoint_type="openai",
                embedding_endpoint=self.base_url,
                embedding_dim=1536,
                embedding_chunk_size=DEFAULT_EMBEDDING_CHUNK_SIZE,
                handle=self.get_handle("riven-free", is_embedding=True),
            )
        ]
