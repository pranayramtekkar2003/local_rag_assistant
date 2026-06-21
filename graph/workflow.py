from langgraph.graph import (
    START,
    END,
    StateGraph
)

from graph.states import GraphState

from graph.Nodes import (
    retrieverNode,
    generateNode
)

def buildGraph():

    builder = StateGraph(GraphState)

    builder.add_node("retrieve", retrieverNode)
    builder.add_node("generate",generateNode)
    
    builder.add_edge(START,"retrieve")
    builder.add_edge("retrieve","generate")
    builder.add_edge("generate",END)

    return builder.compile()