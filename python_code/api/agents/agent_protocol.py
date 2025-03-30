from typing import Protocol, List, Dict, Any

# To set a standard for how all the agents interact with other sytems and each other.
class AgentProtocol(Protocol):
    def get_response(self, messages: List[Dict[str, Any]]) -> Dict[str, Any]:
        ...