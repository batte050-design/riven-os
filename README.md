# riven (formerly MemGPT)

Build AI with advanced memory that can learn and self-improve over time.

* [riven Code](https://docs.riven.com/riven-code): run agents locally in your terminal
* [riven API](https://docs.riven.com/quickstart/): build agents into your applications

## Get started in the CLI

Requires [Node.js 18+](https://nodejs.org/en/download)

1. Install the [riven Code](https://github.com/riven-ai/riven-code) CLI tool: `npm install -g @riven-ai/riven-code`
2. Run `riven` in your terminal to launch an agent with memory running on your local computer

When running the CLI tool, your agent help you code and do any task you can do on your computer.

riven Code supports [skills](https://docs.riven.com/riven-code/skills) and [subagents](https://docs.riven.com/riven-code/subagents), and bundles pre-built skills/subagents for advanced memory and continual learning. riven is fully model-agnostic, though we recommend Opus 4.5 and GPT-5.2 for best performance (see our [model leaderboard](https://leaderboard.riven.com/) for our rankings).

## Get started with the riven API

Use the riven API to integrate stateful agents into your own applications.
riven has a full-featured agents API, and a Python and Typescript SDK (view our [API reference](https://docs.riven.com/api)).

### Installation

TypeScript / Node.js:
```bash
npm install @riven-ai/riven-client
```

Python:
```bash
pip install riven-client
```

### Hello World example

Below is a quick example of creating a stateful agent and sending it a message (requires a [riven API key](https://app.riven.com)).
See the full [quickstart guide](https://docs.riven.com/quickstart) for complete documentation.

TypeScript:
```typescript
import riven from "@riven-ai/riven-client";

const client = new riven({ apiKey: process.env.riven_API_KEY });

// Create your agent
const agentState = await client.agents.create({
  model: "openai/gpt-5.2",
  memory_blocks: [
    {
      label: "human",
      value:
        "Name: Timber. Status: dog. Occupation: building riven, infrastructure to democratize self-improving superintelligence",
    },
    {
      label: "persona",
      value:
        "I am a self-improving superintelligence. Timber is my best friend and collaborator.",
    },
  ],
  tools: ["web_search", "fetch_webpage"],
});

console.log("Agent created with ID:", agentState.id);

// Send your agent a message
const response = await client.agents.messages.create(agentState.id, {
  input: "What do you know about me?",
});

for (const message of response.messages) {
  console.log(message);
}
```

Python:
```python
from riven_client import riven
import os

client = riven(api_key=os.getenv("riven_API_KEY"))

# Create your agent
agent_state = client.agents.create(
    model="openai/gpt-5.2",
    memory_blocks=[
        {
          "label": "human",
          "value": "Name: Timber. Status: dog. Occupation: building riven, infrastructure to democratize self-improving superintelligence"
        },
        {
          "label": "persona",
          "value": "I am a self-improving superintelligence. Timber is my best friend and collaborator."
        }
    ],
    tools=["web_search", "fetch_webpage"]
)

print(f"Agent created with ID: {agent_state.id}")

# Send your agent a message
response = client.agents.messages.create(
    agent_id=agent_state.id,
    input="What do you know about me?"
)

for message in response.messages:
    print(message)
```

## Contributing

riven is an open source project built by over a hundred contributors from around the world. There are many ways to get involved in the riven OSS project!

* [**Join the Discord**](https://discord.gg/riven): Chat with the riven devs and other AI developers.
* [**Chat on our forum**](https://forum.riven.com/): If you're not into Discord, check out our developer forum.
* **Follow our socials**: [Twitter/X](https://twitter.com/riven_AI), [LinkedIn](https://www.linkedin.com/in/riven), [YouTube](https://www.youtube.com/@riven-ai)

---

***Legal notices**: By using riven and related riven services (such as the riven endpoint or hosted service), you are agreeing to our [privacy policy](https://www.riven.com/privacy-policy) and [terms of service](https://www.riven.com/terms-of-service).*
