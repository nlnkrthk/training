from typing import TypedDict

from langgraph.graph import StateGraph, START, END


# State
class State(TypedDict):
    user_input: str
    intent: str
    response: str


# Supervisor node
def supervisor(state):
    user_input = state["user_input"].lower()

    if "internet" in user_input or "network" in user_input:
        return {"intent": "network"}

    elif "bill" in user_input or "charge" in user_input:
        return {"intent": "billing"}

    return {"intent": "unknown"}


# Network node
def network_node(state):
    return {
        "response": "Network diagnostics completed."
    }


# Billing node
def billing_node(state):
    return {
        "response": "Billing resolution completed."
    }


# Routing function
def route(state):
    if state["intent"] == "network":
        return "network"

    elif state["intent"] == "billing":
        return "billing"

    return "unknown"


# Create graph
graph = StateGraph(State)


# Add nodes
graph.add_node("supervisor", supervisor)
graph.add_node("network", network_node)
graph.add_node("billing", billing_node)


# Add edges
graph.add_edge(START, "supervisor")

graph.add_conditional_edges(
    "supervisor",
    route,
    {
        "network": "network",
        "billing": "billing",
        "unknown": END
    }
)

graph.add_edge("network", END)
graph.add_edge("billing", END)


# Compile
app = graph.compile()


# Run
result = app.invoke({
    "user_input": "Check for duplicate charges",
    "intent": "",
    "response": ""
})

print(result)