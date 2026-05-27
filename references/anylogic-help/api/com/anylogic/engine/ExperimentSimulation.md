*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ExperimentSimulation.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class ExperimentSimulation<ROOT extends Agent>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.Presentable](Presentable.md "class in com.anylogic.engine")

[com.anylogic.engine.Utilities](Utilities.md "class in com.anylogic.engine")

[com.anylogic.engine.Experiment](Experiment.md "class in com.anylogic.engine")<ROOT>

com.anylogic.engine.ExperimentSimulation<ROOT>

Type Parameters:
:   `ROOT` - class of top-level agent

All Implemented Interfaces:
:   `AgentConstants`, `CodeValueExecutor`, `EnvironmentConstants`, `UtilitiesMath`, `UtilitiesRandom`, `UtilitiesString`, `Serializable`

---

```
public abstract class ExperimentSimulation<ROOT extends Agent>
extends Experiment<ROOT>
```

The simplest possible experiment consisting of a single simulation
run. One should implement the createRoot() method in a subclass to set a
particular model to this experiment.
A typical usage pattern is here:

```
public class MyExperiment extends ExperimentSimulation {

    public Agent createRoot( Engine engine ) {
       MyMain root = new MyMain( engine, null, null );
       //set parameters of root if needed
       ...
       return root;
    }

    public void setup() {
       Engine eng = getEngine();
       //set engine stop time, time mode, etc.
       ...
       Presentation p = new Presentation( ex, null );
       p.start();
       //set presentation size, configure toolbar, etc.
       ...
    }

    public static void main( String[] args ) {
       MyExperiment ex = new MyExperiment();
       ex.setName( "My Experiment" );
       ex.setup( null );
    }

 }
```

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.ExperimentSimulation)

## Nested Class Summary

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ExperimentSimulation()` | Creates the experiment and a new simulation engine that will be used for all simulations. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `customRunPause_xjal(boolean requestRun, boolean atAbsoluteTime, double time)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `customRunPause_xjal(boolean absoluteTime, double t)` | Deprecated. |
| `final com.anylogic.engine.internal.ActiveView` | `ep_xjal()` | *This method shouldn't be accessed by user*  is public due to technical reasons |
| `void` | `finish()` | Sets a flag that, when tested by the engine, causes it to finish after completing the current event execution. |
| `OmniFrame` | `generateOmniFrame(boolean fullFrame)` |  |
| `Engine` | `getEngine()` | Returns the engine executing the model. |
| `OmniverseSyncParameters` | `getOmniverseSyncParams()` |  |
| `double` | `getProgress()` | Returns the progress of the experiment: in this case it is the same as the progress of the current simulation run. |
| `double` | `getRunTimeSeconds()` | Returns the real duration of the experiment in seconds, excluding pause times, in this case it is same as duration of the simulation run. |
| `Experiment.State` | `getState()` | Returns the current state of the experiment. |
| `UsdContext` | `getUsdContext()` |  |
| `boolean` | `isOmniverseAvailable()` |  |
| `boolean` | `isOmniverseEnabled()` |  |
| `void` | `onDestroy_xjal()` | *This method normally shouldn't be called by user.*  Is called when the experiment object is dynamically disposed - before closing the model window.  This method should be overridden to release resources (e.g. |
| `void` | `pause()` | Pauses the model execution. |
| `void` | `prepareForOmniverse()` |  |
| `void` | `registerExperimentHost_xjal(IExperimentHost experimentHost)` | **This method isn't designed to be called by user.**  *Public due to technical reasons*  May be removed in future releases |
| `void` | `run()` | Runs the model from the current state. |
| `void` | `runAndShowRoot_xjal()` | Deprecated. |
| `void` | `setNewEngine_xjal(Engine engine)` | **This method is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| `void` | `setupOmniverseParameters(ROOT root)` |  |
| `abstract void` | `setupRootParameters(ROOT root, boolean callOnChangeActions)` | Is called to setup parameters of top-level agent. |
| `void` | `startOmniverseConnector()` |  |
| `void` | `step()` | Performs one step of the model execution. |
| `void` | `stop()` | Terminates the model execution, destroys and forgets the model and calls garbage collector, but keeps all experiment data. |
