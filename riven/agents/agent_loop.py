from typing import TYPE_CHECKING

from riven.agents.base_agent_v2 import BaseAgentV2
from riven.agents.riven_agent_v2 import rivenAgentV2
from riven.agents.riven_agent_v3 import rivenAgentV3
from riven.groups.sleeptime_multi_agent_v3 import SleeptimeMultiAgentV3
from riven.groups.sleeptime_multi_agent_v4 import SleeptimeMultiAgentV4
from riven.schemas.agent import AgentState
from riven.schemas.enums import AgentType

if TYPE_CHECKING:
    from riven.orm import User


class AgentLoop:
    """Factory class for instantiating the agent execution loop based on agent type"""

    @staticmethod
    def load(agent_state: AgentState, actor: "User") -> BaseAgentV2:
        if agent_state.agent_type in [AgentType.riven_v1_agent, AgentType.sleeptime_agent]:
            if agent_state.enable_sleeptime:
                if agent_state.multi_agent_group is None:
                    # Agent has sleeptime enabled but no group - fall back to non-sleeptime agent
                    from riven.log import get_logger

                    logger = get_logger(__name__)
                    logger.warning(
                        f"Agent {agent_state.id} has enable_sleeptime=True but multi_agent_group is None. "
                        f"Falling back to standard rivenAgentV3."
                    )
                    return rivenAgentV3(
                        agent_state=agent_state,
                        actor=actor,
                    )
                return SleeptimeMultiAgentV4(
                    agent_state=agent_state,
                    actor=actor,
                    group=agent_state.multi_agent_group,
                )
            return rivenAgentV3(
                agent_state=agent_state,
                actor=actor,
            )
        elif agent_state.enable_sleeptime and agent_state.agent_type != AgentType.voice_convo_agent:
            if agent_state.multi_agent_group is None:
                # Agent has sleeptime enabled but no group - fall back to non-sleeptime agent
                from riven.log import get_logger

                logger = get_logger(__name__)
                logger.warning(
                    f"Agent {agent_state.id} has enable_sleeptime=True but multi_agent_group is None. "
                    f"Falling back to standard rivenAgentV2."
                )
                return rivenAgentV2(
                    agent_state=agent_state,
                    actor=actor,
                )
            return SleeptimeMultiAgentV3(agent_state=agent_state, actor=actor, group=agent_state.multi_agent_group)
        else:
            return rivenAgentV2(
                agent_state=agent_state,
                actor=actor,
            )
