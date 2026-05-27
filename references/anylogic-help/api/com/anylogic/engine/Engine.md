*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/Engine.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class Engine

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.Engine

All Implemented Interfaces:
:   `Serializable`

---

```
public final class Engine
extends Object
implements Serializable
```

The simulation engine that drives the model execution. The engine maintains
the event queue, the default random number generator, etc. Although there is
one engine per simulation, it is designed to have no static data, so
there may exist several concurrent simulations in one JVM, in particular, one
simulation can invoke the other, etc.
The engine behavior and usage patterns are best described with a statechart with
states IDLE, PAUSED, RUNNING, FINISHED, ERROR, PLEASE\_WAIT. The normal usage
pattern of the engine controlled by the Presentation GUI is like this:
`Engine engine = new Engine(); // -> IDLE; random number generator is initialized
Agent root = new RootAgent( engine, null, null );
...//setup parameters of root
engine.start( root ); // -> PAUSED
engine.run(); // -> RUNNING; launches execution in a new thread, calls the experiment back on finish
...
engine.pause(); // -> PAUSED
engine.step(); // -> PAUSED
engine.run(); // -> RUNNING
...
engine.stop(); // -> IDLE completely destroys the model
...
Agent root2 = new RootAgent2( engine, null, null );
...etc.`
The engine state PLEASE\_WAIT means the engine is executing a non-interruptible
single command, such as pause(), step(), or stop().
If you do not need multithreading and wish to run the model as fast as possible
(i.e. in virtual time mode only) in the controlling thread, you may call runFast()
instead of run(). runFast() ignores any synchronization, therefore you should not
access the model data (e.g. call drawing of agents) concurrently with
runFast().

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.Engine)

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static enum` | `Engine.EventSelectionMode` | Simultaneous event selection mode constants |
| `static enum` | `Engine.ModelType` | The type of the model, returned by Engine. |
| `static enum` | `Engine.SolverDAEType` | The solver type for mixed differential-algebraic equations |
| `static enum` | `Engine.SolverNAEType` | The solver type for algebraic equations |
| `static enum` | `Engine.SolverODEType` | The solver type for ordinary differential equations |
| `static enum` | `Engine.State` | The state of the Engine |

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final Engine.State` | `ERROR` |  |
| `static final Engine.EventSelectionMode` | `EVENT_SELECTION_DETERMINISTIC` | Deprecated. Use [`EVENT_SELECTION_LIFO`](#EVENT_SELECTION_LIFO) or [`EVENT_SELECTION_FIFO`](#EVENT_SELECTION_FIFO) instead |
| `static final Engine.EventSelectionMode` | `EVENT_SELECTION_FIFO` | Deterministic selection mode (first in - first out) constant for [`setSimultaneousEventsSelectionMode(EventSelectionMode)`](#setSimultaneousEventsSelectionMode(com.anylogic.engine.Engine.EventSelectionMode))  Offers good performance, simultaneous events are executed in the same order they were scheduled.  This is the *default* mode used by engine |
| `static final Engine.EventSelectionMode` | `EVENT_SELECTION_LIFO` | Deterministic selection mode (last in - first out) constant for [`setSimultaneousEventsSelectionMode(EventSelectionMode)`](#setSimultaneousEventsSelectionMode(com.anylogic.engine.Engine.EventSelectionMode))  Offers good performance, simultaneous events are executed in the reverse to the order they were scheduled |
| `static final Engine.EventSelectionMode` | `EVENT_SELECTION_RANDOM` | Random selection mode constant for [`setSimultaneousEventsSelectionMode(EventSelectionMode)`](#setSimultaneousEventsSelectionMode(com.anylogic.engine.Engine.EventSelectionMode))  This mode is slower than [`EVENT_SELECTION_FIFO`](#EVENT_SELECTION_FIFO) or [`EVENT_SELECTION_LIFO`](#EVENT_SELECTION_LIFO)  This mode utilises the [default random number generator](#getDefaultRandomGenerator()) of the Engine. |
| `static final Engine.State` | `FINISHED` |  |
| `static final Engine.State` | `IDLE` |  |
| `static final Engine.ModelType` | `MODEL_TYPE_CONTINUOUS` |  |
| `static final Engine.ModelType` | `MODEL_TYPE_DISCRETE` |  |
| `static final Engine.ModelType` | `MODEL_TYPE_HYBRID` |  |
| `static final Engine.ModelType` | `MODEL_TYPE_UNKNOWN` |  |
| `static final Engine.State` | `PAUSED` |  |
| `static final Engine.State` | `PLEASE_WAIT` |  |
| `static final Engine.State` | `RUNNING` |  |
| `static final Engine.SolverDAEType` | `SOLVER_DAE_EULER_NEWTON` |  |
| `static final Engine.SolverDAEType` | `SOLVER_DAE_RK45_NEWTON` |  |
| `static final Engine.SolverNAEType` | `SOLVER_NAE_CLASSIC_NEWTON` |  |
| `static final Engine.SolverNAEType` | `SOLVER_NAE_FAST_NEWTON` |  |
| `static final Engine.SolverNAEType` | `SOLVER_NAE_MODIFIED_NEWTON` |  |
| `static final Engine.SolverODEType` | `SOLVER_ODE_EULER` |  |
| `static final Engine.SolverODEType` | `SOLVER_ODE_RK4` |  |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Engine()` | Constructs the engine and sets the seed of the default random number generator to 0.  Normally this constructor calls are generated automatically by AnyLogic.   For *AnyLogic Professional* users: in custom experiments please use [`ExperimentCustom.createEngine()`](ExperimentCustom.md#createEngine()) method instead of this constructor to create and obtain new instance of the engine |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Date` | `date()` | Returns the current model date with respect to the start time/date and the model time unit. |
| `long` | `dateInMillis()` | Returns the current model date milliseconds with respect to the start time/date and the model time unit. |
| `double` | `dateToTime(Date d)` | Converts the given date to model time with respect to the start date, start time and model time unit settings |
| `void` | `disableWarning(String warningType)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `RuntimeException` | `error(String errorText)` | Signals an error during the model run by throwing a RuntineException with the given text. |
| `RuntimeException` | `error(Throwable cause, String errorText)` | Signals an error during the model run by throwing a RuntineException with the given text. |
| `RuntimeException` | `errorInModel(String errorText)` | Signals an model logic error during the model run by throwing a [`ModelException`](ModelException.md "class in com.anylogic.engine") with the given text.  This method differs from `error()` in the way of displaying error message: model logic errors are 'softer' than other errors, they use to happen in the models and signal the modeler that model might need some parameters adjustments. |
| `RuntimeException` | `errorInModel(Throwable cause, String errorText)` | Signals an model logic error during the model run by throwing a [`ModelException`](ModelException.md "class in com.anylogic.engine") with the given text.  This method differs from `error()` in the way of displaying error message: model logic errors are 'softer' than other errors, they use to happen in the models and signal the modeler that model might need some parameters adjustments. |
| `boolean` | `finish()` | Terminates the model after execution of current event. |
| `void` | `flushSnapshotCache()` | Clears cache with contents of recently loaded snapshot file  NB: cache is automatically cleared on new snapshot loading |
| `int` | `getAmPm()` | Indicates whether the hour of the current model date with respect to the start time/date and the model time unit is before (`AM`) or after (`Utilities.PM`) noon.  This method is used for the 12-hour clock.  E.g., at 10:04:15.250 PM the result is `Utilities.PM`. |
| `double` | `getATOL()` | Returns absolute tolerance of the numeric engine. |
| `DatabaseLogState` | `getDatabaseLogState()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `Date` | `getDate()` | Deprecated. Use [`date()`](#date()) instead |
| `int` | `getDayOfMonth()` | Returns the day of the month of the current model date with respect to the start time/date and the model time unit.  The first day of the month has value 1. |
| `int` | `getDayOfWeek()` | Returns the day of the week of the current model date with respect to the start time/date and the model time unit.  Returned value is one of: `Utilities.SUNDAY` `Utilities.MONDAY` `Utilities.TUESDAY` `Utilities.WEDNESDAY` `Utilities.THURSDAY` `Utilities.FRIDAY` `Utilities.SATURDAY` |
| `int` | `getDayOfYear()` | Returns the day of the year of the current model date with respect to the start time/date and the model time unit.  The first day of the year has value 1. |
| `Random` | `getDefaultRandomGenerator()` | Returns the currently used default random number generator. |
| `long` | `getEventCount()` | Returns the number of currently scheduled events. |
| `Experiment<?>` | `getExperiment()` | Returns the experiment controlling the model execution.  *This method isn't designed for AnyLogic Cloud, also returns `null` for custom experiments* |
| `ExperimentCustom` | `getExperimentCustom()` | Returns the custom experiment controlling the model execution.  Returns `null` for other types of experiments |
| `IExperimentHost` | `getExperimentHost()` | Returns the experiment host object associated with this engine, or some dummy object with no functionality if there is none. |
| `int` | `getHour()` | Returns the hour of the morning or afternoon of the current model date with respect to the start time/date and the model time unit.  This method is used for the 12-hour clock.  Noon and midnight are represented by 0, not by 12.  E.g., at 10:04:15.250 PM the result is 10. |
| `int` | `getHourOfDay()` | Returns the hour of day of the current model date with respect to the start time/date and the model time unit.  This method is used for the 24-hour clock.  E.g., at 10:04:15.250 PM the result is 22. |
| `double` | `getHTOL()` | Returns fixed step of the numeric engine. |
| `InspectionWindowColorTheme` | `getInspectionWindowColorTheme()` | Returns color theme for all inspection windows |
| `int` | `getMillisecond()` | Returns the millisecond within the second of the current model date with respect to the start time/date and the model time unit.  E.g., at 10:04:15.250 PM the result is 250. |
| `int` | `getMinute()` | Returns the minute within the hour of the current model date with respect to the start time/date and the model time unit.  E.g., at 10:04:15.250 PM the result is 4. |
| `ModelDatabase` | `getModelDatabase()` | Returns the the database of this model |
| `ModelProperties` | `getModelProperties()` | Returns the model properties of this model |
| `Engine.ModelType` | `getModelType()` | Returns the type of model being executed:  MODEL\_TYPE\_UNKNOWN - the model is either empty or it is too early to judge  MODEL\_TYPE\_DISCRETE - the model so far had at least one discrete event and no equations  MODEL\_TYPE\_CONTINUOUS - the model so far had at equation and no discrete events  MODEL\_TYPE\_HYBRID the model had both events and equations |
| `int` | `getMonth()` | Returns the month of the current model date with respect to the start time/date and the model time unit.  This is a calendar-specific value.  The first month of the year in the Gregorian and Julian calendars is `JANUARY` which is 0; the last depends on the number of months in a year.  Possible values: `Utilities.JANUARY` `Utilities.FEBRUARY` `Utilities.MARCH` `Utilities.APRIL` `Utilities.MAY` `Utilities.JUNE` `Utilities.JULY` `Utilities.AUGUST` `Utilities.SEPTEMBER` `Utilities.OCTOBER` `Utilities.NOVEMBER` `Utilities.DECEMBER` `Utilities.UNDECIMBER` *(indicates the thirteenth month of the year.* |
| `double` | `getNextEventTime()` | Returns the time of the earliest event scheduled so far. |
| `double` | `getNextStepTime()` | Returns the time which will be after the next [`step()`](#step()) execution If the model is about to finish, returns `-infinity`.  Special cases: in system-dynamics models the result may depend on the selected accuracy in system-dynamics models some conditional events may occur based on the value obtained from numerical solver within the step. |
| `IExperimentHost` | `getPresentation()` | Deprecated. this method will be removed in the next releases. |
| `double` | `getProgress()` | Returns the progress of the simulation: the part of model time simulated so far in case the stop time is set, or `-1` if it is not set. |
| `boolean` | `getRealTimeMode()` | Returns `true` if the current execution mode is real time, `false` if virtual time. |
| `double` | `getRealTimeScale()` | Returns the currently set real time scale of model execution, i.e. |
| `Agent` | `getRoot()` | Returns the top-level agent setup for the engine (the topmost level agent from which the model creation and execution starts). |
| `double` | `getRTOL()` | Returns relative tolerance of the numeric engine. |
| `int` | `getRunCount()` | Returns the number of the current simulation run, more precisely the number of times the model was destroyed. |
| `long` | `getRunTimeMillis()` | Returns the real duration of the simulation run in milliseconds, excluding pause times. |
| `int` | `getSecond()` | Returns the second within the minute of the current model date with respect to the start time/date and the model time unit.  E.g., at 10:04:15.250 PM the result is 15. |
| `Engine.SolverDAEType` | `getSolverDAE()` | Returns solver type for mixed differential-algebraic equations |
| `Engine.SolverNAEType` | `getSolverNAE()` | Returns solver type for algebraic equations |
| `Engine.SolverODEType` | `getSolverODE()` | Returns solver type for ordinary differential equations |
| `Date` | `getStartDate()` | Returns the date corresponding to the start time of the simulation. |
| `double` | `getStartTime()` | Returns the currently set start time - the model time at which the simulation starts, by default it is 0. |
| `double` | `getStartTime(TimeUnits units)` | Returns the currently set start time - the model time at which the simulation starts, by default it is 0. |
| `long` | `getStartTimeMillis()` | Returns the result of a call to System.currentTimeMillis() at the simulation start. |
| `Engine.State` | `getState()` | Returns the current state of the engine:  IDLE - no model is set for execution, doing nothing  PAUSED - model is set and have started, ready to run or make a step  RUNNING - in the loop of model execution invoked by run() or runFast()  FINISHED - the model execution is finished OK, but the model is not yet destroyed  ERROR - the model execution is finished with error, the model is not yet destroyed  PLEASE\_WAIT - in the process of executing a non-interruptible command like pause(), step() or stop()  The state is however not guaranteed as may be modified concurrently. |
| `long` | `getStep()` | Returns the number of events executed by the engine. |
| `Date` | `getStopDate()` | Returns the date corresponding to the stop time, null if the stop time is infinity. |
| `double` | `getStopTime()` | Returns the currently set stop time - the model time at which the simulation should stop, or `+infinity` if stop time is not set. |
| `double` | `getStopTime(TimeUnits units)` | Returns the currently set stop time - the model time at which the simulation should stop, or `+infinity` if stop time is not set. |
| `double` | `getTime()` | Deprecated. Use [`time()`](#time()) instead. |
| `TimeUnits` | `getTimeUnit()` | Returns the real time units currently set as the model time units. |
| `double` | `getTTOL()` | Returns time tolerance of the numeric engine. |
| `static String` | `getVersion()` |  |
| `final Number` | `getVMethods()` |  |
| `int` | `getYear()` | Returns the year of the current model date with respect to the start time/date and the model time unit.  This is a calendar-specific value |
| `void` | `interruptRunFast(Runnable callback)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `boolean` | `isCalendarDateUsed()` | Returns `true` if calendar dates (e.g. |
| `boolean` | `isCloudProbablyPresent()` |  |
| `static boolean` | `isDebugging()` | Returns `true` if the model is started in the debug mode from AnyLogic |
| `boolean` | `isEventAwareSolver()` | Returns the current setting used by System Dynamics solver in the models having both System Dynamics equations and Discrete Event parts. |
| `boolean` | `isInspectionWindowsVisible()` |  |
| `boolean` | `isLoadedFromSnapshot()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `boolean` | `isPackage3DResourcesLocatedinJar(String packagePrefix)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `boolean` | `isRealTimeMaintained()` | *This method is not designed to be called by user*  is public due to technical reasons |
| `boolean` | `isStopping()` | Deprecated. |
| `boolean` | `isTestExperiment()` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `Agent` | `loadRootObjectFromSnapshot(String snapshotFileName)` | Loads and sets top-level agent from the given snapshot with caching contents of snapshot file (for performance speed-up)  This method supports loading from snapshots created with any experiment with animation (i.e. |
| `Agent` | `loadRootObjectFromSnapshot(String snapshotFileName, boolean cacheSnapshot)` | Loads and sets top-level agent from the given snapshot with optional caching contents of snapshot file (for performance speed-up)  This method supports loading from snapshots created with any experiment with animation (i.e. |
| `boolean` | `pause()` | Engine command applicable only in RUNNING state (in other states does nothing and returns `false`). |
| `void` | `registerAgentWithEquations(Agent ao)` | Registers given agent with equations in Engine equations solver. |
| `void` | `registerDelay(VariableDelay variableDelay)` | Registers given delay in Engine equations solver. |
| `void` | `resetBeforeStart()` | This method should be called from custom experiments which use logging to database.  Resets state variables which may be accessed by root parameters setup before [`start(Agent)`](#start(com.anylogic.engine.Agent)) is called.  **This method does nothing if state isn't [`IDLE`](#IDLE)** |
| `boolean` | `run()` | Engine command applicable only in PAUSED state (in other states does nothing and returns `false`). |
| `boolean` | `runFast()` | Runs the model in the fastest possible way in the same (calling) thread. |
| `boolean` | `runFast(double pauseTime)` | Calls [`runFast()`](#runFast()) but pauses the model execution at the specified model time and returns `true`  If the model finishes (because of stop time or finish() method called) before the `pauseTime`, the method runs the model until the finish moment only. |
| `void` | `runFastInterruptible(double pauseTime)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `saveRootObjectSnapshot(String snapshotFileName)` | Saves top-level agent and current state of this Engine to a snapshot file with the given name. |
| `void` | `setATOL(double atol)` | Sets the absolute tolerance of the numeric engine. |
| `void` | `setDefaultRandomGenerator(Random r)` | Changes the default random number generator. |
| `void` | `setEventAwareSolver(boolean eventAwareSolver)` | This setting is actual for models having both System Dynamics equations and Discrete Event parts. |
| `void` | `setExperiment(Experiment<?> ex)` | Sets the experiment that will be controlling the model execution. |
| `void` | `setExperimentHost(IExperimentHost h)` | Sets the object that will be host the model execution (animation and controls). |
| `void` | `setHTOL(double htol)` | Sets the fixed step of the numeric engine. |
| `void` | `setInspectionWindowColorTheme(InspectionWindowColorTheme theme)` | Set color theme for all inspection windows |
| `void` | `setInspectionWindowsVisible(boolean visible)` |  |
| `void` | `setLoadedFromSnapshot(boolean loadedFromSnapshot)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `setPresentation(IExperimentHost p)` | Deprecated. this method will be removed in the next releases. |
| `void` | `setRealTimeMode(boolean on)` | Sets the virtual or real time execution mode. |
| `void` | `setRealTimeScale(double scale)` | Sets the desired real time scale of model execution, i.e. |
| `void` | `setRTOL(double rtol)` | Sets the relative tolerance of the numeric engine. |
| `void` | `setSimultaneousEventsSelectionMode(Engine.EventSelectionMode mode)` | Sets the mode of event selection among simultaneous events (if any occur). |
| `void` | `setSolverDAE(Engine.SolverDAEType solverDAE)` | Sets solver type for mixed differential-algebraic equations  Available solvers: [`SOLVER_DAE_RK45_NEWTON`](#SOLVER_DAE_RK45_NEWTON) (default) [`SOLVER_DAE_EULER_NEWTON`](#SOLVER_DAE_EULER_NEWTON) |
| `void` | `setSolverNAE(Engine.SolverNAEType solverNAE)` | Sets solver type for algebraic equations  Available solvers: [`SOLVER_NAE_MODIFIED_NEWTON`](#SOLVER_NAE_MODIFIED_NEWTON) (default) [`SOLVER_NAE_FAST_NEWTON`](#SOLVER_NAE_FAST_NEWTON) [`SOLVER_NAE_CLASSIC_NEWTON`](#SOLVER_NAE_CLASSIC_NEWTON) |
| `void` | `setSolverODE(Engine.SolverODEType solverODE)` | Sets solver type for ordinary differential equations  Available solvers: [`SOLVER_ODE_EULER`](#SOLVER_ODE_EULER) (default) [`SOLVER_ODE_RK4`](#SOLVER_ODE_RK4) |
| `void` | `setStartDate(Date date)` | Sets the date corresponding to the start time of the simulation. |
| `void` | `setStartTime(double tstart)` | Sets the start time for the simulation - the initial value of the model clock. |
| `void` | `setStartTime(double tstart, TimeUnits units)` | Sets the start time for the simulation - the initial value of the model clock. |
| `void` | `setStopDate(Date date)` | Sets the stop time of the simulation by converting the stop date provided to the model time, subject to the start time, start date and time unit settings. |
| `void` | `setStopTime(double tstop)` | Sets the stop time for the simulation. |
| `void` | `setStopTime(double tstop, TimeUnits units)` | Sets the stop time for the simulation. |
| `void` | `setTimeUnit(TimeUnits tu)` | Sets the correspondence between the model time unit and a real time unit. |
| `void` | `setTTOL(double ttol)` | Sets the time tolerance of the numeric engine. |
| `final void` | `setVMethods(Number n)` |  |
| `boolean` | `start(Agent root)` | Engine command applicable only in IDLE state (in other states does nothing and returns `false`). |
| `boolean` | `step()` | Makes at most one discrete step of the model (can be done from the PAUSED state only). |
| `boolean` | `stop()` | Stops and destroys the model, see also [`finish()`](#finish()) method, which doesn't destroy the model.   Engine command applicable only in any non-IDLE state (in IDLE state does nothing and returns `false`). |
| `double` | `time()` | Returns the current model (logical) time. |
| `double` | `time(TimeUnits units)` | Returns the current model (logical) time. |
| `Date` | `timeToDate(double t)` | Converts the given model time to date with respect to the start date, start time and model time unit settings, null if the time is infinity. |
| `long` | `timeToDateInMillis(double time)` | Returns the model date milliseconds with respect to the start time/date and the model time unit for the given model time |
| `boolean` | `unregisterAgentWithEquations(Agent ao)` | Unregisters the agent from the engine equations solver. |
| `void` | `unregisterDelay(VariableDelay variableDelay)` | Unregisters the delay from the engine equations solver. |
