*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/Agent.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class Agent

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.Presentable](Presentable.md "class in com.anylogic.engine")

[com.anylogic.engine.Utilities](Utilities.md "class in com.anylogic.engine")

com.anylogic.engine.Agent

All Implemented Interfaces:
:   `AgentConstants`, `CodeValueExecutor`, `EnvironmentConstants`, `IMaintenanceable`, `com.anylogic.engine.internal.Child`, `UtilitiesMath`, `UtilitiesRandom`, `UtilitiesString`, `Serializable`

Direct Known Subclasses:
:   `FlowchartBlock`

---

```
public class Agent
extends Utilities
implements com.anylogic.engine.internal.Child, IMaintenanceable
```

This is a base class for all agent classes created by the user.
Agent is the main building block of AnyLogic models; it can have
parameters, variables, ports, events, statecharts and embedded agents
and/or agent populations.
Agent is the unit of dynamic creation of destruction.
Agent may dynamically obtain extensions (which will increase
memory footprint of agent), see [`ext(Class)`](#ext(java.lang.Class))

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.Agent)

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final Object` | `_ARRIVAL_message_xjal` | This variable *shouldn't be accessed by user*: it is used internally by AnyLogic and may be renamed/removed in future |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Agent()` | Create constructor.  This is a way for e.g. |
| `Agent(Engine engine, Agent owner, AgentList<?> ownerPopulation)` | Constructs the agent, sets up its owner and list (if replicated). |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static Engine` | `_initGetEngine_xjal(Agent owner)` | *This method shouldn't be called by user.* It is public due to technical reasons. |
| `void` | `addAgentToContents(Agent agent)` | Adds a given agent to the contents of this agent. |
| `void` | `addEntityToContents(Agent agent)` | Deprecated. please use [`addAgentToContents(Agent)`](#addAgentToContents(com.anylogic.engine.Agent)) |
| `void` | `addExt_xjal(AgentExtension ext)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future* |
| `String` | `agentInfo()` |  |
| `Iterable<Agent>` | `agents()` | Returns the collection of all agents registered in this space. |
| `List<? extends Agent>` | `agentsInRange(double distance)` | Returns the unsorted list of agents (from the [population](#getPopulation()) this agent lives in), which are within the given `distance` from this agent |
| `List<? extends Agent>` | `agentsInRange(double distanceInUnits, LengthUnits units)` | Returns the unsorted list of agents (from the [population](#getPopulation()) this agent lives in), which are within the given `distance` from this agent |
| `final <T extends Agent> List<T>` | `agentsInRange(Iterable<T> agents, double distance)` | Returns the unsorted list of agents from the given collection which are within the given `distance` from this agent |
| `final <T extends Agent> List<T>` | `agentsInRange(Iterable<T> agents, double distanceInUnits, LengthUnits units)` | Returns the unsorted list of agents from the given collection which are within the given `distance` from this agent |
| `void` | `applyLayout()` | Rearranges agents in this space according to the selected layout type. |
| `void` | `applyNetwork()` | Discards all existing connections and establishes new connection network according to the current network settings. |
| `void` | `applyNetwork(Random r)` | Discards all existing connections and establishes new connection network according to the current network settings, using the specified random number generator, if required by network type. |
| `boolean` | `areStepsEnabled()` | Tests if the time steps are enabled. |
| `void` | `assignInitialConditions_xjal()` | *This method shouldn't be normally called by user.*  This function assigns initial conditions for stocks and for flow aux variables |
| `boolean` | `connectTo(Agent a)` | Creates a bi-directional connection between this agent and a given other agent. |
| `<T extends Agent> List<T>` | `contents()` |  |
| `final void` | `create()` | Creates the agent embedded objects; also calls user's [`onBeforeCreate()`](#onBeforeCreate()) at the beginning and [`onCreate()`](#onCreate()) at the end. |
| `void` | `createAndStart(Agent anyAgent)` | Assigns the owner of the agent to the top-level agent of the model, creates the internal structure of the agent (internally embedded agents, statecharts etc.) and starts it (thus its statechart and events start living). |
| `final void` | `createAsEmbedded()` | Internal method to be called for embedded agents inside [`doCreate()`](#doCreate()) of an upper-level agent. |
| `void` | `createUsdObjects()` |  |
| `FlowchartBlock` | `currentBlock()` | Returns the current flowchart block this agent is being processed in. |
| `void` | `deleteSelf()` | Removes this agent from the agent population (replicated agent list) it belongs to. |
| `void` | `deliver(Object msg, Agent dest)` | Deprecated. this function is deprecated since AnyLogic 8.9.2. |
| `void` | `deliver(Object msg, MessageDeliveryType mode)` | Delivers a message to an agent or a group of agents, as specified by the mode parameter immediately during this method call. |
| `void` | `deliverToAllAgentsInside(Object msg)` | Deprecated. |
| `void` | `deliverToAllConnected(Object msg)` | Deprecated. this function is deprecated since AnyLogic 8.9.2. |
| `void` | `deliverToAllNeighbors(Object msg)` | Deprecated. this function is deprecated since AnyLogic 8.9.2. |
| `void` | `deliverToRandomAgentInside(Object msg)` | Deprecated. |
| `void` | `deliverToRandomConnected(Object msg)` | Deprecated. this function is deprecated since AnyLogic 8.9.2. |
| `void` | `deliverToRandomNeighbor(Object msg)` | Deprecated. this function is deprecated since AnyLogic 8.9.2. |
| `void` | `disableSteps()` | Disables time steps. |
| `boolean` | `disconnectFrom(Agent a)` | Disconnects this agent from another given agent. |
| `void` | `disconnectFromAll()` | Disconnects the agent from all other agents. |
| `double` | `distanceByRoute(Agent other)` | Calculates the distance from this agent to another one by route.  Only for agents in GIS space. |
| `double` | `distanceTo(double x, double y)` | Calculates the distance from this agent to a given point in continuous 3D or GIS space. |
| `double` | `distanceTo(double x, double y, double z)` | Calculates the distance from this agent to a given point in continuous space. |
| `double` | `distanceTo(double x, double y, double z, LengthUnits units)` | Calculates the distance from this agent to a given point in continuous space. |
| `double` | `distanceTo(double x, double y, LengthUnits units)` | Calculates the distance from this agent to a given point in continuous 3D or GIS space. |
| `double` | `distanceTo(Agent other)` | Calculates the distance from this agent to another one in continuous 3D space or GIS space.  In case of GIS space returns distance measured in meters |
| `double` | `distanceTo(Agent other, LengthUnits units)` | Calculates the distance from this agent to another one in continuous 3D space or GIS space.  In case of GIS space returns distance measured in meters |
| `double` | `distanceTo(Point p)` | Calculates the distance from this agent to a given point. |
| `double` | `distanceTo(Point p, LengthUnits units)` | Calculates the distance from this agent to a given point. |
| `void` | `doAfterCreate()` | Internal callback to perform additional "after all agents created" actions. |
| `void` | `doCreate()` | Creates the agent embedded objects.  If there are any embedded objects, this method should be implemented in subclass to instantiate them, setup their parameters and call `agent.createAsEmbedded()` method on each `agent`. |
| `void` | `doFinish()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons. |
| `void` | `doStart()` | Starts activities (e.g. |
| `void` | `drawLinksToAgents(boolean underAgents, LinkToAgentAnimator animator)` | This method automatically generated by AnyLogic. |
| `void` | `enableSteps(double stepDuration)` | Enables discrete time steps with a given duration. |
| `RuntimeException` | `error(Throwable cause, String errorText)` | Signals an error during the model run by throwing a RuntimeException with errorText preceded by the agent full name. |
| `RuntimeException` | `errorInModel(Throwable cause, String errorText)` | Signals an model logic error during the model run by throwing a ModelException with errorText preceded by the agent full name.  This method differs from `error()` in the way of displaying error message: model logic errors are 'softer' than other errors, they use to happen in the models and signal the modeler that model might need some parameters adjustments. |
| `double` | `evaluateRateOf(EventRate e)` | Evaluates the rate expression of a rate event.  Must be implemented in a subclass if there are any rate events. |
| `double` | `evaluateRateOf(TransitionRate t)` | Evaluates the rate expression of a rate transition.  Must be implemented in a subclass if there are any rate transitions. |
| `double` | `evaluateTimeoutOf(EventTimeout e)` | Evaluates timeout expression of a timeout event.  Must be implemented in a subclass if there are any timeout events. |
| `double` | `evaluateTimeoutOf(TransitionTimeout t)` | Evaluates timeout expression of a timeout transition.  Must be implemented in a subclass if there are any timeout transitions. |
| `void` | `executeActionOf(EventCondition e)` | Executes action of a condition event.  Implementation in a subclass can be skipped if the action(s) are empty. |
| `void` | `executeActionOf(EventRate e)` | Executes action of a rate event.  Implementation in a subclass can be skipped if the action(s) are empty. |
| `void` | `executeActionOf(EventTimeout e)` | Executes action of a timeout event.  Implementation in a subclass can be skipped if the action(s) are empty. |
| `void` | `executeActionOf(Statechart<?> s)` | Executes startup action of a statechart: calls actions of the statechart entry point, entry action of initial states, starts the corresponding transitions, etc., and sets up the initially active simple state.  Must be implemented in a subclass if there are any statecharts. |
| `void` | `executeActionOf(TransitionCondition t)` | Executes action of a condition transition.  Implementation in a subclass can be skipped if the action(s) are empty. |
| `void` | `executeActionOf(TransitionMessage t, int msg)` | Executes action of a message transition for int message type - depends on the message.  Implementation in a subclass can be skipped if the action(s) are empty. |
| `void` | `executeActionOf(TransitionMessage t, Object msg)` | Executes action of a message transition for Object message type - depends on the message.  Implementation in a subclass can be skipped if the action(s) are empty. |
| `void` | `executeActionOf(TransitionRate t)` | Executes action of a rate transition.  Implementation in a subclass can be skipped if the action(s) are empty. |
| `void` | `executeActionOf(TransitionTimeout t)` | Executes action of a timeout transition.  Implementation in a subclass can be skipped if the action(s) are empty. |
| `boolean` | `executeOnReceiveActionOf(Port<?,?> p, Object msg)` | Executes action code associated with a message being received at a port. |
| `boolean` | `executeOnSendActionOf(Port<?,?> p, Object msg)` | Executes action associated with a message being sent via a port. |
| `final <T extends AgentExtension> T` | `ext(Class<T> c)` | Returns an extension of given type. |
| `boolean` | `finishSimulation()` | Engine command applicable only in RUNNING or PAUSED state (in other states does nothing and returns `false`). |
| `void` | `formulasExecute_xjal()` | *This method shouldn't be normally called by user.*  Executes formulas defined in this agent. |
| `Agent` | `getAgentAtCell(int r, int c)` | Returns the agent located in the cell with a given row and column, or null. |
| `Agent` | `getAgentNextToMe(CellDirection dir)` | Returns the agent next to this agent in a given direction, if any. |
| `SpaceType` | `getAgentSpaceType()` | Returns type of space where this agent lives, if this is an agent and it has spatial information. |
| `int` | `getAgentTypeId()` | Deprecated. |
| `AgentAnimationSettings` | `getAnimationSettingsOf(Agent ao)` | Returns the animation settings of a simple (not replicated) embedded object.  Must be implemented in a subclass if there are any embedded objects. |
| `AgentAnimationSettings` | `getAnimationSettingsOf(AgentList<?> aocollection)` | Returns the animation settings of a replicated embedded object.  Must be implemented in a subclass if there are any replicated embedded objects. |
| `double` | `getBlockEnterTime()` | Returns the time this agent entered its current flowchart block. |
| `int` | `getC()` | Returns the column of the agent's cell. |
| `int` | `getCameras3D(Map<String,Camera3D> output)` | Adds all [`Camera3D`](presentation/Camera3D.md "class in com.anylogic.engine.presentation") of this agent to the given map `output`, if it is not `null`.  Default implementation does nothing and returns `0`. |
| `Color` | `getColor()` | Returns the color of the item's **default** animation shape. |
| `Agent` | `getConnectedAgent(int index)` | Returns the connected agent with a given index. |
| `<T extends Agent> List<T>` | `getConnections()` | Returns a collection of agents connected to this agent (bi-directionally), or empty collection if there have not been any connections yet. |
| `int` | `getConnectionsNumber()` | Returns the number of agents connected to this agent. |
| `<T extends Enum<T> & IStatechartState<?, T>> T` | `getContainerStateOf(T state)` | Deprecated. |
| `ConveyorNetwork[]` | `getConveyorNetworks()` | Returns array of conveyor networks located in this agent, or empty array |
| `AgentList<Agent>` | `getDefaultPopulation()` | Returns the default population (contained in top-level agent) or `null` if root couldn't be found |
| `int` | `getDifferentialFlatEquationsCount_xjal()` | *This method shouldn't be normally called by user.* |
| `Set<DynamicEvent>` | `getDynamicEvents()` | Returns the set of all currently existing dynamic events of this agent. |
| `List<Object>` | `getEmbeddedObjects()` | Creates and returns a list of embedded objects if there are any, null if there are none. |
| `Engine` | `getEngine()` | Returns the simulation engine where this object belongs to. |
| `Agent` | `getEnvironment()` | Deprecated. |
| `SpaceType` | `getEnvironmentSpaceType()` | Deprecated. |
| `IExperimentHost` | `getExperimentHost()` | Returns the experiment host object of the model, or some dummy object with no functionality if there is none. |
| `double` | `getFirstOccurrenceTime(EventTimeout e)` | Returns the (absolute) time of first occurrence of a timeout event (of Once or Cyclic mode). |
| `double` | `getFlowchartEntryTime()` | Returns the time the entity has entered the first block in the flowchart, or `Double.NaN` if this agent hasn't yet visited any flowchart |
| `final String` | `getFullName()` | Returns the name of the agent prefixed by the path from the top-level agent to this one. |
| `double` | `getGISHeading()` | Returns current heading angle (measured in radians CW, starting from North direction) of agent moving in GIS space. |
| `ShapeGISMap` | `getGISMap()` | Returns [`ShapeGISMap`](presentation/ShapeGISMap.md "class in com.anylogic.engine.presentation") object used in this GIS space.  Throws error if space type is different from GIS. |
| `double` | `getHeight()` | Returns the height of the agent (measured in meters) - used by conveyors and other blocks which require it during processing. |
| `double` | `getHeight(LengthUnits units)` | Returns the height of the agent (measured in the given units) - used by conveyors and other blocks which require it during processing. |
| `int` | `getId()` | Returns the unique identifier of this agent in the context of the model run |
| `int` | `getIdOf(Statechart<?> s)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons.  Returns some ordinal number of this statechart in the agent type (like id, among all statecharts, respecting agent type inheritance) |
| `int` | `getIndex()` | For a **list-based** agent population, returns its index in the list, otherwise returns `-1`. |
| `int` | `getInitialAlgebraicFlatEquationsCount_xjal()` | *This method shouldn't be normally called by user.* |
| `int` | `getInitialFormulaFlatEquationsCount_xjal()` | *This method shouldn't be normally called by user.* |
| `String` | `getInspectionWindowString()` | Returns string for inspection window content |
| `SDIntegrationManager` | `getIntegrationManager_xjal()` | *This method shouldn't be normally called by user.*  Returns static integration manager defined in derived classes. |
| `double` | `getLat()` | Deprecated. use getLatitude() |
| `double` | `getLatitude()` | Returns the current (up-to-date) latitude of the agent in continuous GIS space. |
| `LayoutType` | `getLayoutType()` | Returns the layout type. |
| `double` | `getLength()` | Returns the length of the agent (measured in meters) - used by conveyors and other blocks which require it during processing. |
| `double` | `getLength(LengthUnits units)` | Returns the length of the agent (measured in the given units) - used by conveyors and other blocks which require it during processing. |
| `Level` | `getLevel()` | Returns the level this agent lives in, actual for agents in continuous space. |
| `Level[]` | `getLevels()` | Returns array of levels located in this agent, or empty array |
| `LinkToAgentCollection<? extends Agent,? extends Agent>` | `getLinkToAgentStandard_xjal()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `double` | `getLon()` | Deprecated. use getLongitude() |
| `double` | `getLongitude()` | Returns the current (up-to-date) longitude of the agent in continuous GIS space. |
| `EventTimeout.Mode` | `getModeOf(EventTimeout e)` | Returns mode of a timeout event: Cyclic, Once, User.  Must be implemented in a subclass if there are any timeout events. |
| `final String` | `getName()` | Returns the name of this agent, i.e. |
| `String` | `getNameOf(Agent ao)` | Returns the name of a simple (not replicated) embedded object.  Must be implemented in a subclass if there are any embedded objects. |
| `String` | `getNameOf(AgentList<?> aocollection)` | Returns the name of a replicated embedded object.  Must be implemented in a subclass if there are any replicated embedded objects. |
| `String` | `getNameOf(EventCondition e)` | Returns the name of a condition event.  Must be implemented in a subclass if there are any condition events. |
| `String` | `getNameOf(EventRate e)` | Returns the name of a rate event.  Must be implemented in a subclass if there are any rate events. |
| `String` | `getNameOf(EventTimeout e)` | Returns the name of a timeout event.  Must be implemented in a subclass if there are any timeout events. |
| `String` | `getNameOf(Port<?,?> p)` | Returns the name of a port.  Must be implemented in a subclass if there are any ports. |
| `String` | `getNameOf(Statechart<?> s)` | Returns the name of a statechart.  Must be implemented in a subclass if there are any statecharts. |
| `String` | `getNameOf(TransitionCondition t)` | Returns the name of a condition transition.  Must be implemented in a subclass if there are any condition transitions. |
| `String` | `getNameOf(TransitionMessage t)` | Returns the name of a message transition.  Must be implemented in a subclass if there are any message transitions. |
| `String` | `getNameOf(TransitionRate t)` | Returns the name of a rate transition.  Must be implemented in a subclass if there are any rate transitions. |
| `String` | `getNameOf(TransitionTimeout t)` | Returns the name of a timeout transition.  Must be implemented in a subclass if there are any timeout transitions. |
| `String` | `getNameOfState(IStatechartState<?,?> state)` | Returns the name of a statechart state.  Must be implemented in a subclass if there are any states. |
| `final <T extends Agent> T` | `getNearestAgent(Iterable<T> agents)` | Returns the nearest agent from the given collection |
| `final <T extends Agent> T` | `getNearestAgentByRoute(Iterable<T> agents)` | Returns the nearest agent from the given collection. |
| `Agent[]` | `getNeighbors()` | Returns the array of neighbor agents, subject to the current neighborhood type (Euclidean - {N,S,E,W}, Moore - also {..,NW,NW,SE,SW}) |
| `INetwork` | `getNetwork()` | Returns the network this agent lives in, actual for agents in continuous space. |
| `double` | `getNetworkConnectionRange()` | Returns the range of agent connections. |
| `double` | `getNetworkConnectionsPerAgent()` | Returns the average (or exact) number of connections per agent. |
| `double` | `getNetworkNeighborLinkProbability()` | Returns the probability of an agent connection to be a neighbour. |
| `INode` | `getNetworkNode()` | Returns the network node this agent currently is located in, actual for agents in continuous space. |
| `INetwork[]` | `getNetworks()` | Returns array of networks located in this agent, or empty array |
| `int` | `getNetworkScaleFreeM()` | Returns the M parameter of a scale free network. |
| `NetworkType` | `getNetworkType()` | Returns the network type. |
| `Agent` | `getOwner()` | Returns the owner agent that encapsulates this one, null if this is the top-level agent in the model. |
| `ShapeEmbeddedObjectPresentation` | `getOwnerShape()` | Returns the shape on owner's presentation, this object presentation belongs to.  May return `null` if this object's presentation isn't located anywhere or when it has no own presentation (e.g. |
| `<T> T` | `getParameter(String name)` | Returns the value of parameter with the given name.  This method should be overridden in subclasses.  Throws error if there is no parameter with the given name. |
| `String[]` | `getParameterNames()` | Returns array of all not dynamic parameter names. |
| `void` | `getPhaseVector_xjal(double[] D, int idxD, double[] A, int idxA)` | *This method shouldn't be normally called by user.*  Assigns given arrays with current variables values |
| `void` | `getPhaseVectorForInitialConditions_xjal(double[] A, int idxA)` | *This method shouldn't be normally called by user.*  Assigns given arrays with current variables values (the function is used while solving initial conditions loops) |
| `AgentList<?>` | `getPopulation()` | For agent population returns the List of agents embedded in the owner object where this agent belongs to, `null` if the object is not replicated |
| `Position` | `getPosition()` | Returns the current (up-to-date) x, y (and z in case of 3D space) coordinate of the agent in continuous space and its orientation as well. |
| `Position` | `getPosition(Position out)` | Returns the current (up-to-date) x, y (and z in case of 3D space) coordinate of the agent in continuous space and its orientation as well. |
| `double` | `getPresentationScaleOnOwnerSpace()` | Returns the scale of the agent presentation animation on its space or `1.0` if space isn't defined |
| `ShapeTopLevelPresentationGroup` | `getPresentationShape()` |  |
| `int` | `getR()` | Returns the row of the agent's cell. |
| `RailwayNetwork[]` | `getRailwayNetworks()` | Returns array of railway networks located in this agent, or empty array |
| `Agent` | `getRandomConnectedAgent()` | Returns the randomly chosen connected agent. |
| `AgentList<?>` | `getReplicatedCollection()` | Deprecated. This method may be removed in the next release. |
| `AgentList<?>` | `getReplicatedList()` | For agent population returns the List of agents embedded in the owner object where this agent belongs to, `null` if the object is not replicated |
| `void` | `getRightPart_xjal(double[] DR, int idxDR, double[] AR, int idxAR)` | *This method shouldn't be normally called by user.*  Calculates right parts of differential equations and algebraic equations to the given arrays |
| `void` | `getRightPartForInitialConditions_xjal(double[] AR, int idxAR)` | *This method shouldn't be normally called by user.*  Returns right part while solving algebraic loops in initial conditions |
| `RoadNetwork[]` | `getRoadNetworks()` | Returns array of road networks located in this agent, or empty array |
| `Agent` | `getRootAgent()` | Returns the top-level agent or `null` if root couldn't be found |
| `double` | `getRotation()` | Returns the current rotation angle (in radians) of the agent in continuous 3D space or GIS space. |
| `IRouteProvider` | `getRouteProvider()` | Returns the provider of routes for agent movement |
| `int` | `getRuntimeAlgebraicFlatEquationsCount_xjal()` | *This method shouldn't be normally called by user.* |
| `int` | `getRuntimeFormulaFlatEquationsCount_xjal()` | *This method shouldn't be normally called by user.* |
| `Scale` | `getScale()` | Returns the scale used by the space of this agent.  The default scale is 10 pixels per meter |
| `Agent` | `getSpace()` | Returns the agent representing space this agent lives in |
| `SpaceType` | `getSpaceType()` | Returns agent space type, if this agent acts as a space for other agents, and has spatial information. |
| `double` | `getSpeed()` | Returns the current value of the agent speed in continuous/GIS space. |
| `double` | `getSpeed(SpeedUnits units)` | Returns the current value of the agent speed in continuous/GIS space. |
| `Statechart` | `getStatechartOf(TransitionCondition t)` | Returns the statechart where the condition transition belongs to.  Must be implemented in a subclass if there are any condition transitions. |
| `Statechart` | `getStatechartOf(TransitionMessage t)` | Returns the statechart where the message transition belongs to.  Must be implemented in a subclass if there are any message transitions. |
| `Statechart` | `getStatechartOf(TransitionRate t)` | Returns the statechart where the rate transition belongs to.  Must be implemented in a subclass if there are any rate transitions. |
| `Statechart` | `getStatechartOf(TransitionTimeout t)` | Returns the statechart where the timeout transition belongs to.  Must be implemented in a subclass if there are any timeout transitions. |
| `double` | `getTargetLat()` | Returns the latitude of the target location if moving, otherwise current latitude in GIS space, measured in degrees (-90 ... |
| `double` | `getTargetLon()` | Returns the longitude of the target location if moving, otherwise current longitude in GIS space, measured in degrees (-180 ... |
| `double` | `getTargetX()` | Returns the x of the target location if moving, otherwise current x in continuous 3D space or GIS space.  In case of GIS space this is the latitude, measured in degrees (-90 ... |
| `double` | `getTargetY()` | Returns the y of the target location if moving, otherwise current y in continuous 3D space or GIS space.  In case of GIS space this is the longitude, measured in degrees (-180 ... |
| `double` | `getTargetZ()` | Returns the z of the target location if moving, otherwise current z in continuous space. |
| `UsdContext` | `getUsdContext()` |  |
| `double` | `getVelocity()` | Deprecated. this function is deprecated since AnyLogic 7.1. |
| `double` | `getVerticalRotation()` | Returns the current vertical rotation angle of the agent in 3D space. |
| `double` | `getWidth()` | Returns the width of the agent (measured in meters) - used by conveyors and other blocks which require it during processing. |
| `double` | `getWidth(LengthUnits units)` | Returns the width of the agent (measured in the given units) - used by conveyors and other blocks which require it during processing. |
| `double` | `getX()` | Returns the current (up-to-date) x coordinate of the agent in continuous space. |
| `Point` | `getXYZ()` | Returns the current (up-to-date) x, y (and z in case of 3D space) coordinate of the agent in continuous space. |
| `Point` | `getXYZ(Point out)` | Returns the current (up-to-date) x, y (and z in case of 3D space) coordinate of the agent in continuous space. |
| `double` | `getY()` | Returns the current (up-to-date) y coordinate of the agent in continuous space. |
| `double` | `getZ()` | Returns the current (up-to-date) z coordinate of the agent in continuous space. |
| `void` | `goToPopulation(AgentList newPopulation)` | Changes the population of agent. |
| `void` | `highlight(boolean yes)` | Turns on/off highlighting of this agent animation. |
| `void` | `instantiateBaseStructure_xjal()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons. |
| `boolean` | `inState(IStatechartState<?,?> state)` | Returns `true` if the corresponding statechart of this agent is at the specified state, i.e. |
| `boolean` | `isAgent()` | Returns `true` if this is at least an informational agent (may be with or without spatial properties). |
| `boolean` | `isAutomaticHorizontalRotation()` | Returns `true` if agent is set to be rotated during movement, `false` otherwise |
| `boolean` | `isAutomaticVerticalRotation()` | Returns `true` if agent is set to be rotated (in vertical direction, along Z-axis) during movement in 3D, `false` otherwise.  The returned value has no effect if [`isAutomaticHorizontalRotation()`](#isAutomaticHorizontalRotation()) is `false` |
| `boolean` | `isConnectedTo(Agent a)` | Tests if this agent is connected to a given other agent. |
| `boolean` | `isEmbeddedAgentPresentationVisible(Agent embeddedAgent)` | **This method is internal and shouldn't be called by user.**  This method works only for single embedded objects (not population) inside this agent.  *Method may be removed/renamed in future.* It is public due to technical reasons. |
| `boolean` | `isEnvironment()` | Deprecated. |
| `boolean` | `isLoggingToDB(LoggingType loggingType)` | Returns `true` if this agent and its internals may log their data/changes/activity to AnyLogic built-in database (logging options are configurable in the properties of Database / Log in the Projects tree inside AnyLogic) |
| `boolean` | `isLoggingToDB(EventOriginator e)` | Return `true` if the given event (or dynamic event) is logged to database (note that this may be overridden by logging settings of Agent).  Default implementation returns `true`. |
| `boolean` | `isMoving()` | Tests if the agent is currently moving in continuous 3D space or GIS space. |
| `boolean` | `isNextCellInsideSpace(CellDirection dir)` | Returns `true` if there is an adjacent cell in a given direction. |
| `boolean` | `isPublicPresentationDefined()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons. |
| `boolean` | `isReplicated()` | Returns `true` if this object is embedded in its owner as replicated, i.e. |
| `boolean` | `isSpacePositionSet_xjal()` | Deprecated. |
| `void` | `jumpTo(double x, double y)` | Instantly moves the agent to a given location in continuous 3D or GIS space. |
| `void` | `jumpTo(double x, double y, double z)` | Instantly moves the agent to a given location. |
| `void` | `jumpTo(INode node)` | Instantly moves the agent to a given network location. |
| `void` | `jumpTo(INode node, Point location)` | Instantly moves the agent to a given network location. |
| `void` | `jumpTo(Point location)` | Instantly moves the agent to a given location without. |
| `void` | `jumpTo(String geographicPlace)` | Finds first geographic point on the Earth and calls method jumpTo(latitude, longitude) with coordinates of the found point |
| `void` | `jumpToCell(int r, int c)` | Moves the agent into a cell with the given row and column. |
| `boolean` | `jumpToRandomEmptyCell()` | Finds a random empty cell and places the agent there. |
| `<T extends Enum<T> & IStatechartState<?, T>> void` | `logToDB(Statechart<T> statechart, Transition transition, T fromState)` | If logging enabled this method will be called in `#exitState(short, Transition, boolean, Statechart)` method |
| `<T extends Enum<T> & IStatechartState<?, T>> void` | `logToDBEnterState(Statechart<T> statechart, T state)` | If logging enabled this method will be called in `#exitState(short, Transition, boolean, Statechart)` method |
| `<T extends Enum<T> & IStatechartState<?, T>> void` | `logToDBExitState(Statechart<T> statechart, T state)` | If logging enabled this method will be called in `#exitState(short, Transition, boolean, Statechart)` method |
| `void` | `markParametersAreSet()` | This methods should be used to mark agents created using no-argument constructor as having all the parameters set. |
| `void` | `moveTo(double x, double y)` | Starts movement in the direction of the given target location in continuous 3D or GIS space.  "On arrival" code is executed when movement is finished. |
| `void` | `moveTo(double x, double y, double z)` | Starts movement in the direction of the given target location in continuous 3D.  "On arrival" code is executed when movement is finished. |
| `void` | `moveTo(double x, double y, double z, Path3D path)` | Starts movement in the direction of the given target location in continuous 3D space along a given path. |
| `void` | `moveTo(double x, double y, Path2D path)` | Starts movement in the direction of the given target location in continuous 3D space along a given path. |
| `void` | `moveTo(Agent agent)` | Starts movement in the direction of the given agent.  "On arrival" code is executed when movement is finished. |
| `void` | `moveTo(Attractor attractor)` | Starts movement to the given attractor.  "On arrival" code is executed when movement is finished. |
| `void` | `moveTo(INode node)` | Starts movement to the given network node.  "On arrival" code is executed when movement is finished. |
| `void` | `moveTo(INode node, Point location)` | Starts movement to the given network node.  "On arrival" code is executed when movement is finished. |
| `void` | `moveTo(Point location)` | Starts movement in the direction of the given target location in continuous 3D.  "On arrival" code is executed when movement is finished. |
| `void` | `moveTo(Point location, Path3D path)` | Starts movement in the direction of the given target location in continuous 3D space along a given path. |
| `void` | `moveTo(String geographicPlace)` | Finds first geographic point on the Earth and calls method moveTo(latitude, longitude) with coordinates of the found point |
| `void` | `moveToInTime(double x, double y, double tripTime)` | Starts movement in the direction of the given target location in continuous 3D or GIS space.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(double x, double y, double z, double tripTime)` | Starts movement in the direction of the given target location in continuous 3D.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(double x, double y, double z, double tripTime, TimeUnits units)` | Starts movement in the direction of the given target location in continuous 3D.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(double x, double y, double z, Path3D path, double tripTime)` | Starts movement in the direction of the given target location in continuous 3D space along a given path. |
| `void` | `moveToInTime(double x, double y, double z, Path3D path, double tripTime, TimeUnits units)` | Starts movement in the direction of the given target location in continuous 3D space along a given path. |
| `void` | `moveToInTime(double x, double y, double tripTime, TimeUnits units)` | Starts movement in the direction of the given target location in continuous 3D or GIS space.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(double x, double y, Path2D path, double tripTime)` | Starts movement in the direction of the given target location in continuous 3D space along a given path. |
| `void` | `moveToInTime(double x, double y, Path2D path, double tripTime, TimeUnits units)` | Starts movement in the direction of the given target location in continuous 3D space along a given path. |
| `void` | `moveToInTime(Agent agent, double tripTime)` | Starts movement in the direction of the given agent.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(Agent agent, double tripTime, TimeUnits units)` | Starts movement in the direction of the given agent.  Changes the speed of the agent in order to reach target in `tripTime`.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(Attractor attractor, double tripTime)` | Starts movement to the given attractor.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(Attractor attractor, double tripTime, TimeUnits units)` | Starts movement to the given attractor.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(INode node, double tripTime)` | Starts movement to the given network node.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(INode node, double tripTime, TimeUnits units)` | Starts movement to the given network node.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(INode node, Point location, double tripTime)` | Starts movement to the given network node.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(INode node, Point location, double tripTime, TimeUnits units)` | Starts movement to the given network node.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(Point location, double tripTime)` | Starts movement in the direction of the given target location.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(Point location, double tripTime, TimeUnits units)` | Starts movement in the direction of the given target location.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToInTime(Point location, Path3D path, double tripTime)` | Starts movement in the direction of the given target location in continuous 3D space along a given path. |
| `void` | `moveToInTime(Point location, Path3D path, double tripTime, TimeUnits units)` | Starts movement in the direction of the given target location in continuous 3D space along a given path. |
| `void` | `moveToNearestAgent(Iterable<? extends Agent> agents)` | Starts movement to the nearest agent from the given collection. |
| `void` | `moveToNearestAgent(Iterable<? extends Agent> agents, double tripTime)` | Starts movement to the nearest agent from the given collection. |
| `void` | `moveToNextCell(CellDirection dir)` | Moves the agent to an adjacent cell in a given direction. |
| `void` | `moveToStraight(double x, double y)` | Starts straight movement (ignoring network/routes) in the direction of the given target location.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToStraight(double x, double y, double z)` | Starts straight movement (ignoring network) in the direction of the given target location.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToStraight(Agent agent)` | Starts straight movement (ignoring network/routes) in the direction of the given agent.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToStraight(Point location)` | Starts straight movement (ignoring network/routes) in the direction of the given target location.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToStraightInTime(double x, double y, double z, double tripTime)` | Starts straight movement (ignoring network) in the direction of the given target location.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToStraightInTime(double x, double y, double z, double tripTime, TimeUnits units)` | Starts straight movement (ignoring network) in the direction of the given target location.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToStraightInTime(Point location, double tripTime)` | Starts straight movement (ignoring network/routes) in the direction of the given target location.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `moveToStraightInTime(Point location, double tripTime, TimeUnits units)` | Starts straight movement (ignoring network/routes) in the direction of the given target location.  Changes the speed of the agent in order to reach target in `tripTime` model time units.  "On arrival" code is executed when movement is finished. |
| `void` | `nothingChanged()` | If called during an event execution, prevents the engine from calling [`onChange()`](#onChange()) of the agent that originated the event. |
| `void` | `onAfterStepEnvironment()` | A callback that is called when at the end of every step after the agents have performed all their step actions. |
| `void` | `onArrival()` | A callback that is called when the agent arrives to the target location after movement initiated by moveTo() in continuous 2D space. |
| `void` | `onBeforeCreate()` | Is called at the very start of create() method, i.e. |
| `void` | `onBeforeStep()` | A callback that is called at the beginning of every step in discrete time before onStep() of any agent is called. |
| `void` | `onBeforeStepEnvironment()` | A callback that is called at the beginning of every step before the agents are asked to perform any their step actions. |
| `void` | `onChange()` | Notification to the agent meaning "some of your data may have changed during this event". |
| `void` | `onCreate()` | Is called at the very end of create() method, i.e. |
| `void` | `onDestroy()` | Must be called when the agent is dynamically disposed. |
| `void` | `onEngineFinished()` | Is called by the engine when it finishes running and is intended to wrap up a single simulation run (e.g. |
| `void` | `onEnterFlowchartBlock(Agent oldBlock, Agent block)` | A callback that is called when the agent enters flowchart block (being an 'entity') |
| `void` | `onExitFlowchartBlock(Agent block)` | A callback that is called when the agent exits flowchart block (being an 'entity') |
| `void` | `onOwnerChanged_xjal()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons. |
| `void` | `onReceive(Object msg, Agent sender)` | A callback that is called when the agent receives a message from another agent. |
| `void` | `onReleaseResource(Agent unit)` | A callback that is called when the agent releases resource |
| `void` | `onSeizeResource(Agent unit)` | A callback that is called when the agent seizes resource |
| `void` | `onStartup()` | Is called after all activities are started in the object (initial events are scheduled) and onStartup() has been called for the embedded objects, but before any steps are made. |
| `void` | `onStep()` | A callback that is called at every step in discrete time after onStep() of any agent is called. |
| `boolean` | `pauseSimulation()` | Engine command applicable only in RUNNING state (in other states does nothing and returns `false`). |
| `void` | `putPhaseVector_xjal(double[] D, int idxD, double[] A, int idxA)` | *This method shouldn't be normally called by user.*  Assigns variables values from the given arrays |
| `void` | `putPhaseVectorForInitialConditions_xjal(double[] A, int idxA)` | *This method shouldn't be normally called by user.*  Assigns variables values from the given arrays (the function is is used while solving initial conditions loops) |
| `Agent` | `randomAgentInside()` | Returns a randomly chosen agent in the space or `null` if there are no agents |
| `Agent` | `randomAgentInside(Random r)` | Returns a randomly chosen agent in the space or `null` if there are no agents. |
| `CellPosition` | `randomEmptyCell()` | Tries to find a pseudo-randomly located empty cell and return its row and column in the array with two elements.  The current implementation is 100% fairly random. |
| `Point` | `randomPointOfSpace()` | Returns the random location in the space |
| `void` | `receive(Object msg)` | Deprecated. this function is deprecated since AnyLogic 8.9.2. |
| `boolean` | `removeAgentFromContents(Agent agent)` | Removes the given agent from the contents of this agent. |
| `boolean` | `removeEntityFromContents(Agent agent)` | Deprecated. please use [`removeAgentFromContents(Agent)`](#removeAgentFromContents(com.anylogic.engine.Agent)) |
| `boolean` | `removeExt_xjal(AgentExtension ext)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future*.  This method removes the given extension if it is found in this agent and return `true` if it was successfully removed |
| `void` | `removeFromFlowchart()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* It is public due to technical reasons. |
| `void` | `removeUsdObjects()` |  |
| `Agent` | `resourceUnitOfPool(Agent pool)` | Returns the first occurrence of resource unit of a given pool among the seized resource units, or `null` if not found. |
| `<T extends Agent> List<T>` | `resourceUnits()` | Returns the list of resource units seized by the entity, or empty list if there are none. |
| `<T extends Agent> List<T>` | `resourceUnitsOfPool(Agent pool)` | Returns resource units currently seized by this entity from the given `ResourcePool` block |
| `<T extends Agent> List<T>` | `resourceUnitsOfSeize(Agent seize)` | Return resource units currently seized by this entity in the given `Seize` block |
| `final void` | `restoreCollection_xjal(AgentList<?> collection)` | Deprecated. |
| `void` | `restoreConnections_xjal(List<?> connections)` | Deprecated. |
| `void` | `restoreOwner(Object owner)` | Deprecated. |
| `boolean` | `runSimulation()` | Engine command applicable only in PAUSED state (in other states does nothing and returns `false`). |
| `void` | `send(Object msg, Agent dest)` | Sends a message to a given agent. |
| `void` | `send(Object msg, MessageDeliveryType mode)` | Sends a message to an agent or a group of agents, as specified by the mode parameter. |
| `void` | `sendToAll(Object msg)` | Sends a message to all agents in the same space this agent lives in. |
| `void` | `sendToAllAgentsInside(Object msg)` | Sends a message to all agents in the space. |
| `void` | `sendToAllConnected(Object msg)` | Sends a message to all connected agents. |
| `void` | `sendToAllNeighbors(Object msg)` | Sends a message to all neighbors. |
| `void` | `sendToRandom(Object msg)` | Sends a message to a randomly chosen agent in the same space this agent lives in. |
| `void` | `sendToRandomAgentInside(Object msg)` | Sends a message to a random agent in the space, if there are any agents. |
| `void` | `sendToRandomConnected(Object msg)` | Sends a message to a randomly chosen connected agent. |
| `void` | `sendToRandomNeighbor(Object msg)` | Sends a message to a randomly chosen neighbor. |
| `void` | `setAgentSpaceType(SpaceType spaceType)` | Sets this agent to live in the space of the given type.  Will throw an error if agent already has different space type |
| `void` | `setAutomaticHorizontalRotation(boolean yes)` | Tells agent to rotate automatically during movements. |
| `void` | `setAutomaticVerticalRotation(boolean yes)` | Tells agent to rotate automatically (in vertical direction, along Z-axis) during movements in 3D.  Has no effect if [`isAutomaticHorizontalRotation()`](#isAutomaticHorizontalRotation()) is `false` |
| `void` | `setCell(int r, int c)` | Puts the agent into a given cell. |
| `void` | `setColor(Color color)` | Sets the color of the item's **default** animation shape.  For custom agent type animation shapes, please use setFillColor and other setters. |
| `void` | `setDestroyed()` | Marks this object as subject to destruction after the current step is finished. |
| `void` | `setDimensions(double lengthInMeters, double widthInMeters, double heightInMeters)` | Sets the length, width, height of the agent |
| `void` | `setDimensions(double lengthInUnits, double widthInUnits, double heightInUnits, LengthUnits units)` | Sets the length, width, height of the agent |
| `void` | `setEngine(Engine engine)` | Sets the simulation engine for the object. |
| `void` | `setEnvironment(Agent env)` | Deprecated. |
| `void` | `setHeight(double heightInMeters)` | Sets the height of the agent |
| `void` | `setHeight(double heightInUnits, LengthUnits units)` | Sets the height of the agent |
| `void` | `setId(int id)` |  |
| `void` | `setLatLon(double latitude, double longitude)` | Sets the coordinates of the agent location. |
| `void` | `setLayoutType(LayoutType type)` | Sets the layout type. |
| `void` | `setLength(double lengthInMeters)` | Sets the length of the agent. |
| `void` | `setLength(double lengthInUnits, LengthUnits units)` | Sets the length of the agent. |
| `void` | `setLevel(Level level)` | Sets this agent to live in the level, actual for agents in continuous space. |
| `void` | `setLocation(Agent agent)` | Takes position of given agent and sets it to this agent. |
| `void` | `setLocation(Attractor attractor)` | Sets the current network location for the agent |
| `void` | `setLocation(INode node)` | *This method is used for initialization only, for dynamic assignment, please use [`jumpTo(INode)`](#jumpTo(com.anylogic.engine.markup.INode)).*  Sets the coordinates of the agent location and *puts it into network node (if network is defined)*.  Should only be used to initialize the agent location. |
| `void` | `setLocation(Point point)` | *This method is used for initialization only, for dynamic assignment, please use [`jumpTo(Point)`](#jumpTo(com.anylogic.engine.Point)).*  Sets the coordinates of the agent location.  Should only be used to initialize the agent location. |
| `void` | `setLocationRandomInside(INode node)` | *This method is used for initialization only, for dynamic assignment, please use [`jumpTo(INode)`](#jumpTo(com.anylogic.engine.markup.INode)).*  Sets the coordinates of the agent location to the randomly chosen point inside the given node and *puts it into network node (if network is defined)*.  Should only be used to initialize the agent location. |
| `void` | `setNetwork(INetwork network)` | Sets this agent to live in the network, actual for agents in continuous and GIS space. |
| `void` | `setNetworkAllInRange(double connectionRange)` | Sets network type to the one when agents are connected if the distance between them is not longer that a given one. |
| `void` | `setNetworkNode(Attractor attractor)` | Sets the current network location for the agent |
| `void` | `setNetworkNode(INode node)` | Sets the current network location for the agent |
| `void` | `setNetworkNode(INode node, Point position)` | Deprecated. |
| `void` | `setNetworkRandom(double connectionsPerAgent)` | Sets network type to random with a given average number of connections per agent. |
| `void` | `setNetworkRingLattice(int connectionsPerAgent)` | Sets network type to ring lattice. |
| `void` | `setNetworkScaleFree(int m)` | Sets the network type to "scale free". |
| `void` | `setNetworkSmallWorld(int connectionsPerAgent, double neighborLinkProbability)` | Sets network type to "small world". |
| `void` | `setNetworkUserDefined()` | Sets network type to user-defined. |
| `boolean` | `setParameter(String name, Object value, boolean callOnChange)` | Sets the value to parameter with the given name.  This method should be overridden in subclasses. |
| `void` | `setParametersToDefaultValues()` | Sets all *not dynamic* parameters to their default values.  This method must be implemented in a subclass, during code generation, and it *must call super method*.  This method is designed to be used in [custom experiments](ExperimentCustom.md "class in com.anylogic.engine") for easier setup of top-level agent in certain situations. |
| `void` | `setPosition(Position position)` | *This method is used for initialization only, for dynamic assignment, please use [`jumpTo(double, double)`](#jumpTo(double,double)).*  Sets the coordinates and orientation of the agent location.  Should only be used to initialize the agent location. |
| `void` | `setRotation(double rotation)` | Sets the rotation angle (in radians) of the agent animation in continuous 3D space or GIS space. |
| `void` | `setRouteProvider(IRouteProvider routeProvider)` | Stops agent if it is moving. |
| `void` | `setSpace(Agent space)` | Sets the space for agent. |
| `void` | `setSpeed(double speedInMPS)` | Changes speed of the agent in continuous/GIS space (measured in meters per second).  If the agent is moving, it continues moving with the new speed. |
| `void` | `setSpeed(double speedInUnits, SpeedUnits units)` | Changes speed of the agent in continuous/GIS space (measured in the given units).  If the agent is moving, it continues moving with the new speed. |
| `void` | `setupExt_xjal(AgentExtension ext)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future* |
| `void` | `setupInitialConditions_xjal(Class<?> callerClass)` | *This method shouldn't be normally called by user.* |
| `void` | `setupSpace(double width, double height)` | Sets the space to the given dimensions. |
| `void` | `setupSpace(double width, double height, double zHeight)` | Sets the space to the given dimensions. |
| `void` | `setupSpace(double width, double height, int rows, int columns, NeighborhoodType neighborhoodType)` | Sets the space type to discrete with the given dimensions and neighbourhood type. |
| `void` | `setupSpace(ShapeGISMap gisMap)` | Sets the space to GIS space to be based on given `gisMap`. |
| `void` | `setVelocity(double v)` | Deprecated. this function is deprecated since AnyLogic 7.1. |
| `void` | `setVerticalRotation(double rotation)` | Sets the vertical rotation (angle in radians), along Z-axis of the agent animation in 3D space. |
| `void` | `setWidth(double widthInMeters)` | Sets the width of the agent |
| `void` | `setWidth(double widthInUnits, LengthUnits units)` | Sets the width of the agent |
| `void` | `setXY(double x, double y)` | Sets the coordinates of the agent location. |
| `void` | `setXYZ(double x, double y, double z)` | *This method is used for initialization only, for dynamic assignment, please use [`jumpTo(double, double)`](#jumpTo(double,double)).*  Sets the coordinates of the agent location in continuous 3D space.  Should only be used to initialize the agent location. |
| `void` | `setXYZ(Point location)` | *This method is used for initialization only, for dynamic assignment, please use [`jumpTo(double, double)`](#jumpTo(double,double)).*  Sets the coordinates of the agent location in continuous 3D space.  Should only be used to initialize the agent location. |
| `double` | `spaceCellHeight()` | Returns the height of the cell in discrete space. |
| `double` | `spaceCellWidth()` | Returns the width of the cell in discrete space. |
| `int` | `spaceColumns()` | Returns the number of columns in the space. |
| `double` | `spaceHeight()` | Returns the height of continuous or discrete space. |
| `int` | `spaceRows()` | Returns the number of rows in the space. |
| `double` | `spaceWidth()` | Returns the width of continuous or discrete space. |
| `double` | `spaceZHeight()` | Returns the height of space along Z-axis. |
| `final void` | `start()` | Starts activities (e.g. |
| `final void` | `startAsEmbedded()` | Internal method to be called for embedded agents inside [`doStart()`](#doStart()) of an upper-level agent. |
| `<T extends Enum<T> & IStatechartState<?, T>> boolean` | `stateContainsState(T compstate, T simpstate)` | Deprecated. |
| `void` | `stop()` | Stops movement in continuous 3D or GIS space. |
| `boolean` | `stopSimulation()` | Engine command applicable only in any non-IDLE state (in IDLE state does nothing and returns `false`). |
| `void` | `swapWithAgent(Agent anotherAgent)` | Swaps the cell location of this agent with another agent. |
| `void` | `swapWithCell(int r, int c)` | Swaps this agent with an agent at the cell with the given row and column. |
| `void` | `swapWithNextCell(CellDirection dir)` | Swaps the agent with an agent at the adjacent cell in a given direction. |
| `boolean` | `testConditionOf(EventCondition e)` | Tests the condition expression of a condition event.  Must be implemented in a subclass if there are any condition events. |
| `boolean` | `testConditionOf(TransitionCondition t)` | Tests the condition expression of a transition event.  Must be implemented in a subclass if there are any condition transitions. |
| `boolean` | `testGuardOf(TransitionCondition t)` | Tests the guard expression of a condition transition.  Implementation in a subclass can be skipped if the guard(s) are empty. |
| `boolean` | `testGuardOf(TransitionMessage t)` | Tests the guard expression of a message transition.  Implementation in a subclass can be skipped if the guard(s) are empty. |
| `boolean` | `testGuardOf(TransitionRate t)` | Tests the guard expression of a rate transition.  Implementation in a subclass can be skipped if the guard(s) are empty. |
| `boolean` | `testGuardOf(TransitionTimeout t)` | Tests the guard expression of a timeout transition.  Implementation in a subclass can be skipped if the guard(s) are empty. |
| `boolean` | `testMessageOf(TransitionMessage t, Object msg)` | Tests the message received by the statechart against the trigger description of a message transition - for Object message type.  Must be implemented in a subclass if there are any message transitions. |
| `final double` | `timeToArrival()` | Returns the time to arrival to the target location in continuous 2D space or GIS space, in model-time units.  If the agent is not moving, returns 0. |
| `final double` | `timeToArrival(TimeUnits units)` | Returns the time to arrival to the target location in continuous 2D space or GIS space, in model-time units.  If the agent is not moving, returns 0. |
| `double` | `toLengthUnits(double lengthInPixels, LengthUnits units)` | Converts the given pixel length to the length units (using scale of this agent which acts as 'Space') |
| `double` | `toPixels(double lengthInUnits, LengthUnits units)` | Converts the length in the given length units to pixels (using scale of this agent which acts as 'Space') |
| `String` | `toString()` | Returns a (possibly, multi-line) textual information on the agent. |
| `final <T extends AgentExtension> T` | `tryExt(Class<T> c)` | Returns an extension of given type only if this object already contains such extension. |
| `void` | `warning(String warningText)` | Signals a warning during the model run with warningText preceded by the agent full name.  Warnings may be turned off in the AnyLogic preferences (runtime section) or by API: [`AnyLogicRuntimePreferences.setEnableWarnings(Boolean)`](AnyLogicRuntimePreferences.md#setEnableWarnings(java.lang.Boolean)).  This method checks against numerous warnings output: In case of multiple warnings having equal `warningText`, only the first 10 of them are displayed. |
| `void` | `warning(String warningTextFormat, Object... args)` | Signals a warning during the model run with warningText preceded by the agent full name. |
