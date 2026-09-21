# Agent Systems and Orchestration

Use this reference for agents, multi-agent systems, swarms, parallel LLM calls, Deep Agents, CodeAct, browser agents, LangChain, LangGraph, Skills, Plans, Goals, and subagent spawning.

## Core model

Model an agent as a bounded loop: **plan/think → act → observe → decide → repeat**. Define the goal, success evidence, available tools, state, memory, permissions, budget, termination conditions, and escalation path before choosing a framework.

Represent each task as a typed contract with objective, inputs, outputs, dependencies, authority, deadline, retry policy, provenance, and failure state. Keep planning separate from execution and verification. Never infer success from a tool call that lacks validated output.

## Architectures

Use supervisor-worker, pipeline, peer-to-peer, hierarchical, event-driven, blackboard, debate/critique, or swarm-like topologies only when their coordination benefit exceeds communication and verification cost. Typical roles include advisor, researcher, planner, executor, critic, verifier, retrieval specialist, browser agent, code agent, and safety reviewer.

A Parallel Agent Dispatcher performs bounded fan-out, tracks task IDs, applies concurrency/rate/cost limits, cancels unnecessary work, and aggregates typed results. A Search Strategy Orchestrator chooses search plans, queries, sources, retrieval methods, and stopping conditions; it should not blindly multiply API calls.

## Multi-LLM calls

When using multiple models or providers, define routing criteria, structured output schemas, timeouts, retries, fallback behavior, budget, privacy constraints, and result reconciliation. Preserve model/provider/version metadata and distinguish parallel independent calls from dependent stages. Use map/reduce or fan-out/fan-in only when partial results can be independently verified.

## Memory and context

Separate working state, task state, scratch context, episodic memory, semantic memory, procedural memory, and durable project records. Offload long context to authoritative files, databases, vector stores, graph stores, or object storage with stable IDs and provenance. Retrieve memory as evidence, not truth; check conflicts, staleness, and access rights.

## Framework mapping

LangChain, LangGraph, Skills, PLAN, Goal, Deep Agent, Sub Agent, CodeAct, MCP Server, Context Engineering, Sandbox Environment, and Browser Agent are implementation routes for the durable abstractions above. Read current framework documentation when syntax, supported transports, or version behavior matters. Do not allow framework defaults to silently grant authority, network access, filesystem access, or unbounded recursion.

## CodeAct and browser agents

Run code agents inside explicit sandboxes with filesystem, process, network, time, and package limits. Require tests, review gates, artifact provenance, rollback, and human approval for consequential changes. Browser agents require isolated contexts, authorized targets, bounded navigation, secret isolation, evidence capture, and safe stopping.

## Evaluation

Measure task success, groundedness, tool correctness, cost, latency, unnecessary delegation, failure recovery, reproducibility, safety, and user-visible usefulness. Evaluate each subagent and the assembled system; a successful swarm run does not prove individual capability or production readiness.
