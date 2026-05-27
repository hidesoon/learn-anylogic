*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/Experiment.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class Experiment<ROOT extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.Presentable](Presentable.md "class in com.anylogic.engine")

[com.anylogic.engine.Utilities](Utilities.md "class in com.anylogic.engine")

com.anylogic.engine.Experiment<ROOT>

Type Parameters:
:   `ROOT` - class of top-level agent

All Implemented Interfaces:
:   `AgentConstants`, `CodeValueExecutor`, `EnvironmentConstants`, `UtilitiesMath`, `UtilitiesRandom`, `UtilitiesString`, `Serializable`

Direct Known Subclasses:
:   `ExperimentRunFast`, `ExperimentSimulation`

---

```
public abstract class Experiment<ROOT extends Agent>
extends Utilities
```

A base class for all AnyLogic experiments. Experiment describes how would
one like to run the model (just perform a single simulation run, do Monte Carlo
simulation, vary parameters, optimize, etc.), and what outputs of the model you
are interested in (this may be a simple chart of how a certain value was changing over
time during a run, or how an observable depends on a parameter in case of
multiple runs, or a histogram in case of risk analysis, etc.). The experiment is
also capable of storing the outputs producted by the model so that they are
available after the simulation and independently of it. Experiment can display
itself in a presentation window and be controlled by the presentation GUI. For
that purpose it supports a set of commands that can be assigned to the presentation
window toolbar buttons and menu items.

AnyLogic models with GUI can run as Java applications.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.Experiment)

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static enum` | `Experiment.Command` |  |
| `static enum` | `Experiment.State` | The state of the Engine |

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final Experiment.State` | `ERROR` |  |
| `static final Experiment.State` | `FINISHED` |  |
| `static final Experiment.State` | `IDLE` |  |
| `com.anylogic.engine.internal.ActionQueue` | `modelExecutionCommandQueue` | *This field shouldn't be accessed by user*  is public due to technical reasons |
| `com.anylogic.engine.internal.ActionQueue` | `mutexModelActionQueue` | *This field shouldn't be accessed by user*  is public due to technical reasons |
| `static final Experiment.Command` | `OPEN_RESULTS` |  |
| `static final Experiment.Command` | `OPEN_SNAPSHOT` |  |
| `static final Experiment.Command` | `PAUSE` |  |
| `static final Experiment.State` | `PAUSED` |  |
| `static final Experiment.State` | `PLEASE_WAIT` |  |
| `static final Experiment.Command` | `RUN` |  |
| `static final Experiment.State` | `RUNNING` |  |
| `static final Experiment.Command` | `SAVE_RESULTS` |  |
| `static final Experiment.Command` | `SAVE_SNAPSHOT` |  |
| `static final Experiment.Command` | `STEP` |  |
| `static final Experiment.Command` | `STOP` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `final void` | `addExecutionListener(ExperimentExecutionListener listener)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `close()` | This method returns immediately and performs the following actions in a separate thread: stops experiment if it is not stopped, destroys the model and closes experiment window (only if model is started in the application mode) |
| `abstract ROOT` | `createRoot(Engine engine)` | Is called to obtain a new top-level agent. |
| `final void` | `destroy_xjal()` | *This method normally shouldn't be called by user.*  Is called when the experiment object is dynamically disposed - before closing the model window. |
| `RuntimeException` | `error(Throwable cause, String errorText)` | Signals an error during the model run by throwing a RuntimeException with errorText preceded by the agent full name. |
| `RuntimeException` | `errorInModel(Throwable cause, String errorText)` | Signals an model logic error during the model run by throwing a ModelException with errorText preceded by the agent full name.  This method differs from `error()` in the way of displaying error message: model logic errors are 'softer' than other errors, they use to happen in the models and signal the modeler that model might need some parameters adjustments. |
| `final String[]` | `getCommandLineArguments()` | Returns an array of Command-line Arguments passed to this experiment on model start (empty array in case of no arguments)  Never returns `null` |
| `IExperimentHost` | `getExperimentHost()` | Returns the experiment host object of the model, or some dummy object with no functionality if there is none. |
| `Object` | `getMutexRead_xjal()` | *This field shouldn't be called by user*  is public due to technical reasons |
| `Object` | `getMutexWrite_xjal()` | *This field shouldn't be called by user*  is public due to technical reasons |
| `String` | `getName()` | Returns the name (window title) of the experiment. |
| `abstract double` | `getProgress()` | Returns the progress of the experiment: a number between 0 and 1 depending on what part of experiment is completed, or `-1` if not known. |
| `int` | `getRunCount()` | Returns the number of the current simulation run, more precisely the number of times the model was destroyed. |
| `abstract double` | `getRunTimeSeconds()` | Returns the real duration of the experiment in seconds, excluding pause times. |
| `final String` | `getSnapshotFileName()` | Returns the name of snapshot file this experiment is configured to start simulation from |
| `abstract Experiment.State` | `getState()` | Returns the current state of the experiment: IDLE, PAUSED, RUNNING, FINISHED, ERROR, or PLEASE\_WAIT |
| `long` | `getStep()` | Returns the number of events executed by the engine. |
| `int` | `getWindowHeight()` | Returns the initial height of the experiment window, 600 by default. |
| `int` | `getWindowWidth()` | Returns the initial width of the experiment window, 800 by default. |
| `void` | `initDefaultRandomNumberGenerator(Engine engine)` | This method should be overridden to initialize random number generator of the given engine  Default implementation set new random generation with random seed - for unique experiments |
| `void` | `internalFillConfig(LaunchConfiguration config)` | **This class is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `boolean` | `isCommandEnabled(Experiment.Command cmd)` | Checks if a command can be executed. |
| `final boolean` | `isLoadRootFromSnapshot()` | Returns `true` if this experiment is configured to start simulation from state loaded from snapshot file |
| `static boolean` | `isTestExperiment(Class<?> experimentClass)` |  |
| `void` | `onBeforeSimulationRun(ROOT root)` | Deprecated. this method will be removed in future, please use [`addExecutionListener(ExperimentExecutionListener)`](#addExecutionListener(com.anylogic.engine.ExperimentExecutionListener)) instead of overriding this method |
| `void` | `onDestroy()` | User extension point which is called when the experiment object is dynamically disposed - before closing the model window.  This method may be overridden to perform custom actions.  Default implementation does nothing. |
| `void` | `onDestroy_xjal()` | *This method normally shouldn't be called by user.*  Is called when the experiment object is dynamically disposed - before closing the model window.  This method should be overridden to release resources (e.g. |
| `void` | `onEngineFinished()` | Deprecated. this method will be removed in future, please use [`addExecutionListener(ExperimentExecutionListener)`](#addExecutionListener(com.anylogic.engine.ExperimentExecutionListener)) instead of overriding this method |
| `void` | `onError(Throwable error)` | This method may be overridden to perform custom processing on errors in the model execution (i.e. |
| `void` | `onError(Throwable error, Agent root)` | This method may be overridden to perform custom processing on errors in the model execution (i.e. |
| `abstract void` | `pause()` | Pauses the experiment execution. |
| `void` | `registerExperimentHost_xjal(IExperimentHost experimentHost)` | **This method isn't designed to be called by user.**  *Public due to technical reasons*  May be removed in future releases |
| `final void` | `removeExecutionListener(ExperimentExecutionListener listener)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `reset()` | Is called each time before a new model is created and is intended to reset all data associated with the experiment. |
| `abstract void` | `run()` | Starts the experiment execution from the current state. |
| `void` | `setCommandLineArguments_xjal(String[] commandLineArguments)` | *This method should not be called by user* |
| `final void` | `setLoadRootFromSnapshot(String snapshotFileName)` | Tells this experiment to load the top-level agent from AnyLogic snapshot file    *This method is only available in the AnyLogic Professional* |
| `void` | `setName(String name)` | Sets the name (window title) of the experiment. |
| `void` | `setup(IExperimentHost experimentHost)` | Is called in static main() method of applications, after the experiment is constructed. |
| `void` | `setupEngine(Engine engine)` | Is called for the simulation engine when it is created |
| `abstract void` | `step()` | Performs one step of experiment execution. |
| `abstract void` | `stop()` | Terminates the experiment execution. |
| `void` | `warning(String warningText)` | Signals a warning during the model run with warningText preceded by the agent full name.  Warnings may be turned off in the AnyLogic preferences (runtime section) or by API: [`AnyLogicRuntimePreferences.setEnableWarnings(Boolean)`](AnyLogicRuntimePreferences.md#setEnableWarnings(java.lang.Boolean)).  This method checks against numerous warnings output: In case of multiple warnings having equal `warningText`, only the first 10 of them are displayed. |
| `void` | `warning(String warningTextFormat, Object... args)` | Signals a warning during the model run with warningText preceded by the agent full name. |
