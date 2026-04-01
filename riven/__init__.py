import os
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("riven")
except PackageNotFoundError:
    # Fallback for development installations
    __version__ = "0.16.7"

if os.environ.get("riven_VERSION"):
    __version__ = os.environ["riven_VERSION"]

# Import sqlite_functions early to ensure event handlers are registered (only for SQLite)
# This is only needed for the server, not for client usage
try:
    from riven.settings import DatabaseChoice, settings

    if settings.database_engine == DatabaseChoice.SQLITE:
        from riven.orm import sqlite_functions  # noqa: F401
except ImportError:
    # If sqlite_vec is not installed, it's fine for client usage
    pass

# # imports for easier access
from riven.schemas.agent import AgentState as AgentState
from riven.schemas.block import Block as Block
from riven.schemas.embedding_config import EmbeddingConfig as EmbeddingConfig
from riven.schemas.enums import JobStatus as JobStatus
from riven.schemas.file import FileMetadata as FileMetadata
from riven.schemas.job import Job as Job
from riven.schemas.riven_message import rivenErrorMessage as rivenErrorMessage, rivenMessage as rivenMessage, rivenPing as rivenPing
from riven.schemas.riven_stop_reason import rivenStopReason as rivenStopReason
from riven.schemas.llm_config import LLMConfig as LLMConfig
from riven.schemas.memory import (
    ArchivalMemorySummary as ArchivalMemorySummary,
    BasicBlockMemory as BasicBlockMemory,
    ChatMemory as ChatMemory,
    Memory as Memory,
    RecallMemorySummary as RecallMemorySummary,
)
from riven.schemas.message import Message as Message
from riven.schemas.organization import Organization as Organization
from riven.schemas.passage import Passage as Passage
from riven.schemas.source import Source as Source
from riven.schemas.tool import Tool as Tool
from riven.schemas.usage import rivenUsageStatistics as rivenUsageStatistics
from riven.schemas.user import User as User
