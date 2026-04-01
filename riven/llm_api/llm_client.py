from typing import TYPE_CHECKING, Optional

from riven.llm_api.llm_client_base import LLMClientBase
from riven.schemas.enums import ProviderType

if TYPE_CHECKING:
    from riven.orm import User


class LLMClient:
    """Factory class for creating LLM clients based on the model endpoint type."""

    @staticmethod
    def create(
        provider_type: ProviderType,
        put_inner_thoughts_first: bool = True,
        actor: Optional["User"] = None,
    ) -> Optional[LLMClientBase]:
        """
        Create an LLM client based on the model endpoint type.

        Args:
            provider: The model endpoint type
            put_inner_thoughts_first: Whether to put inner thoughts first in the response

        Returns:
            An instance of LLMClientBase subclass

        Raises:
            ValueError: If the model endpoint type is not supported
        """
        match provider_type:
            case ProviderType.google_ai:
                from riven.llm_api.google_ai_client import GoogleAIClient

                return GoogleAIClient(
                    put_inner_thoughts_first=put_inner_thoughts_first,
                    actor=actor,
                )
            case ProviderType.google_vertex:
                from riven.llm_api.google_vertex_client import GoogleVertexClient

                return GoogleVertexClient(
                    put_inner_thoughts_first=put_inner_thoughts_first,
                    actor=actor,
                )
            case ProviderType.anthropic:
                from riven.llm_api.anthropic_client import AnthropicClient

                return AnthropicClient(
                    put_inner_thoughts_first=put_inner_thoughts_first,
                    actor=actor,
                )
            case ProviderType.bedrock:
                from riven.llm_api.bedrock_client import BedrockClient

                return BedrockClient(
                    put_inner_thoughts_first=put_inner_thoughts_first,
                    actor=actor,
                )
            case ProviderType.together:
                from riven.llm_api.together_client import TogetherClient

                return TogetherClient(
                    put_inner_thoughts_first=put_inner_thoughts_first,
                    actor=actor,
                )
            case ProviderType.azure:
                from riven.llm_api.azure_client import AzureClient

                return AzureClient(
                    put_inner_thoughts_first=put_inner_thoughts_first,
                    actor=actor,
                )
            case ProviderType.xai:
                from riven.llm_api.xai_client import XAIClient

                return XAIClient(
                    put_inner_thoughts_first=put_inner_thoughts_first,
                    actor=actor,
                )
            case ProviderType.zai | ProviderType.zai_coding:
                from riven.llm_api.zai_client import ZAIClient

                return ZAIClient(
                    put_inner_thoughts_first=put_inner_thoughts_first,
                    actor=actor,
                )
            case ProviderType.groq:
                from riven.llm_api.groq_client import GroqClient

                return GroqClient(
                    put_inner_thoughts_first=put_inner_thoughts_first,
                    actor=actor,
                )
            case ProviderType.minimax:
                from riven.llm_api.minimax_client import MiniMaxClient

                return MiniMaxClient(
                    put_inner_thoughts_first=put_inner_thoughts_first,
                    actor=actor,
                )
            case ProviderType.openrouter:
                # OpenRouter uses OpenAI-compatible API, so we can use the OpenAI client directly
                from riven.llm_api.openai_client import OpenAIClient

                return OpenAIClient(
                    put_inner_thoughts_first=put_inner_thoughts_first,
                    actor=actor,
                )
            case ProviderType.deepseek:
                from riven.llm_api.deepseek_client import DeepseekClient

                return DeepseekClient(
                    put_inner_thoughts_first=put_inner_thoughts_first,
                    actor=actor,
                )
            case ProviderType.baseten:
                from riven.llm_api.baseten_client import BasetenClient

                return BasetenClient(
                    put_inner_thoughts_first=put_inner_thoughts_first,
                    actor=actor,
                )
            case ProviderType.fireworks:
                from riven.llm_api.fireworks_client import FireworksClient

                return FireworksClient(
                    put_inner_thoughts_first=put_inner_thoughts_first,
                    actor=actor,
                )
            case ProviderType.chatgpt_oauth:
                from riven.llm_api.chatgpt_oauth_client import ChatGPTOAuthClient

                return ChatGPTOAuthClient(
                    put_inner_thoughts_first=put_inner_thoughts_first,
                    actor=actor,
                )
            case _:
                from riven.llm_api.openai_client import OpenAIClient

                return OpenAIClient(
                    put_inner_thoughts_first=put_inner_thoughts_first,
                    actor=actor,
                )
