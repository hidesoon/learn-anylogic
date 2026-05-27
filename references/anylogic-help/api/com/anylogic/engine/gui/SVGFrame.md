*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gui/SVGFrame.html>*

---

Package [com.anylogic.engine.gui](package-summary.md)

# Class SVGFrame

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.gui.SVGFrame

---

```
@AnyLogicInternalAPI
public class SVGFrame
extends Object
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `SVGFrame()` |  |
| `SVGFrame(double time, SVGCommand[] commands, boolean fullFrame, Experiment.State state, long step, double timeScale, double progress, int[] multiRunProgress, long realTime, long freeMemory, int numConnections)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `SVGCommand[]` | `getCommands()` |  |
| `ConsoleItem[]` | `getConsoleUpdate()` |  |
| `EventInfo` | `getEventInfo()` |  |
| `long` | `getFreeMemory()` |  |
| `int[]` | `getMultiRunProgress()` |  |
| `long` | `getNumber()` |  |
| `int` | `getNumConnections()` |  |
| `double` | `getProgress()` |  |
| `long` | `getRealTime()` |  |
| `Experiment.State` | `getState()` |  |
| `long` | `getStep()` |  |
| `double` | `getTime()` |  |
| `double` | `getTimeScale()` |  |
| `boolean` | `isFullFrame()` |  |
| `void` | `setConsoleUpdate(ConsoleItem[] consoleUpdate)` |  |
| `void` | `setEventInfo(EventInfo eventInfo)` |  |
| `void` | `setFullFrame(boolean fullFrame)` |  |
| `void` | `setNumber(long number)` |  |
| `String` | `toLog()` |  |
| `String` | `toString()` |  |
