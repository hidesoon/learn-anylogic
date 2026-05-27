*来源 (Source): <https://anylogic.help/advanced/functions/info.html>*

---

# Information functions

:   | Function | Description |
    | --- | --- |
    | String getName(Agent agent) | Returns the name of the agent or ”null” if the given agent does not exist. This is a convenient function for formatting name of some agent when it may be null.   agent — the name of the agent, may be null |
    | String getFullName(Agent agent) | Returns the name of the agent prefixed by the path from the top-level agent to this agent. Returns ”null” if the given agent does not exist. This is a convenient function for formatting name of some agent when it may be null.   agent — the name of the agent, may be null |
    | String briefInfoOn(Object object) | Returns a brief one-line textual information on the given object. Supports most frequently used types: most numeric types, Color, Date, Agent, HyperArray, collections, events, transitions, etc. If the argument type is not supported, returns its default toString(). If the argument is null, returns ”null”.   object — the object to provide information on |
    | String inspectOf(Object object) | Returns the textual information on the object that can be displayed in the multi-line inspect window. This information is an extended version of what is given by briefInfoOn() function.   object — the object being inspected |
