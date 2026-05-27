*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/ExperimentCustom.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class ExperimentCustom

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.ExperimentCustom

All Implemented Interfaces:
:   `Serializable`

Direct Known Subclasses:
:   `ExperimentReinforcementLearning`, `ExperimentTest`

---

```
public abstract class ExperimentCustom
extends Object
implements Serializable
```

Base class for all custom experiments
The experiment scenario should be defined in the overridden [`run()`](#run()) method

Custom experiment may be executed from another experiment - in this case the latter
should be passed as an argument to the constructor of the custom experiment. Experiment
is executed by calling [`run()`](#run()) method.
A sample action code of some Main agent which runs custom experiment:

```
 // Create custom experiment, pass currently running experiment
 // as an argument to the constructor:
 MyCustomExperiment e = new MyCustomExperiment(getExperiment());
 // setup some custom fields defined in the
 // additional class code of MyCustomExperiment:
 e.day = getDayOfWeek();
 // run experiment
 e.run();
 // collect results from custom fields defined in the
 // additional class code of MyCustomExperiment:
 traceln( "result: " + e.myResult );
```

*(In the example above, custom experiment has Code (which is actually inside
`run()` method) which gets field `day` (defined in the additional
class code), uses it in the experiment and then sets some result value to
the field `myResult`)*

Usage notes
**Use [`createEngine()`](#createEngine()) to create new Engine instance**
Use [`Engine.runFast()`](Engine.md#runFast()) method to run experiment in the fastest possible
mode
Don't forget to setup stop time or stop date to the engine before
**Use [`ExperimentOptimization.createOptimization(Engine)`](ExperimentOptimization.md#createOptimization(com.anylogic.engine.Engine)) to
create new OptQuest Optimization instance**

The simplest example of [`run()`](#run()) code:

```
 // Create Engine, initialize random number generator:
 Engine engine = createEngine();
 // Set stop time
 engine.setStopTime( 100 );
 // Create new top-level agent:
 Main root = new Main(engine, null, null);
 // Setup parameters of top-level agent here
 root.myParameter = 10;
 // Prepare Engine for simulation:
 engine.start( root );
 // Start simulation in fast mode:
 engine.runFast();
 // Obtain results of simulation here
 traceln( root.myResult );
 // Destroy the model:
 engine.stop();
```

*This object is only available in the AnyLogic Professional*

See also an [example of optimization performed within custom experiment](OptimizationCallback.md "class in com.anylogic.engine").

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [`run()`](#run())[Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.ExperimentCustom)

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `ExperimentCustom(Object parentExperiment)` | Creates new custom experiment which may be executed from another experiment - in this case the latter should be passed as an argument to the constructor of the custom experiment |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `final Engine` | `createEngine()` | Creates Engine |
| `final String[]` | `getCommandLineArguments()` | Returns an array of Command-line Arguments passed to this experiment on model start (empty array in case of no arguments)  Never returns `null`  *This method is designed for usage inside the [`run()`](#run()) method* |
| `void` | `onError(Throwable error)` | This method may be overridden to perform custom processing on errors in the model execution (i.e. |
| `void` | `onError(Throwable error, Agent root)` | This method may be overridden to perform custom processing on errors in the model execution (i.e. |
| `abstract void` | `run()` | Use [`createEngine()`](#createEngine()) |
| `void` | `setCommandLineArguments_xjal(String[] commandLineArguments)` | *This method should not be called by user* |
| `void` | `setupEngine_xjal(Engine engine)` | *This method should not be called by user* |
