*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gui/IExperimentHost.html>*

---

Package [com.anylogic.engine.gui](package-summary.md)

# Interface IExperimentHost

All Known Implementing Classes:
:   `AutotestExperimentHost`, `ExperimentHost`, `FakeExperimentHost`

---

```
public interface IExperimentHost
```

Object of this interface is responsible for various actions regarding AnyLogic Model
animation and graphical user interface.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Nested Class Summary

| Modifier and Type | Interface | Description |
| --- | --- | --- |
| `static interface` | `IExperimentHost.IValue` | Used for converting String/JSON input data to arbitrary java classes requested by Engine. |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addInspect(double x, double y, Presentable p, String name)` | Creates an inspect window at a particular location for an element of a Presentable object. |
| `Object` | `callFunction(String pathtofunction, IExperimentHost.IValue... args)` |  |
| `void` | `close()` | This method returns immediately and performs the following actions in a separate thread: stops experiment if it is not stopped, destroys the model and closes experiment window (only if model is started in the application mode) |
| `void` | `copyToClipboard(String text)` | Copies the given text to the system clipboard  Due to the security policy of the browser, the actual copying may be preceded by a prompt. |
| `void` | `executeCommand(String cmd, String parameters)` |  |
| `void` | `executeUserAction(long id, String value)` |  |
| `LaunchConfiguration` | `getConfiguration()` |  |
| `INavigationPoint` | `getCurrentNavigationPoint()` |  |
| `Map<String,String>` | `getDependencyModelFolders()` |  |
| `Experiment<?>` | `getExperiment()` | Returns the experiment associated with this host. |
| `Experiment.State` | `getExperimentState()` |  |
| `com.anylogic.engine.internal.presentation.FrameFlag` | `getFrameFlag()` |  |
| `SVGFrameProducer` | `getFrameProducer()` |  |
| `long` | `getNextFrameNumber()` |  |
| `Presentable` | `getPresentable()` | Returns the current top-level object (Agent or Experiment), whose presentation is displayed. |
| `double` | `getProgress()` |  |
| `AnimationPacket` | `getUpdate(boolean fullFrame)` |  |
| `Object` | `getValue(String pathtofield)` |  |
| `double` | `getZoom()` |  |
| `boolean` | `has3D()` |  |
| `void` | `hideAllInspectionWindows()` | Hide all currently visible inspection windows and prevent new inspection windows to be displayed |
| `boolean` | `isOmniverseAnimtaion()` |  |
| `boolean` | `isRunControlEnabled()` | Tests if Run, Pause, and Stop buttons on the model toolbar are enabled. |
| `boolean` | `isSpeedControlEnabled()` | Tests if the model execution speed control buttons on the model toolbar are enabled. |
| `boolean` | `isZoomAndPanningEnabled()` | Tests if zoom & panning from the GUI is enabled. |
| `default void` | `launch()` |  |
| `void` | `launch(boolean startServer, boolean startExperiment)` | Creates and optionally runs experiment, starts frame collection |
| `default void` | `loadSnapshot(String fileName)` | Stops experiment and loads snapshot (in its 'not running' state), doesn't resume simulation of loaded snapshot.  On any error throws nothing, silently rollbacks to the current experiment and resumes it if it was running. |
| `void` | `loadSnapshot(String fileName, Runnable successfulCallback, Consumer<Throwable> errorCallback)` | Stops experiment and loads snapshot (in its 'not running' state), doesn't resume simulation of loaded snapshot.  On any error throws nothing, silently rollbacks to the current experiment and resumes it if it was running.    *When snapshot is loaded, presentation forgets everything about the model which was running before (including the engine, experiment and agents), therefore, it is recommended not to keep references to model objects after this method call*  Usage example: |
| `void` | `navigateHome()` | Navigates presentation home, i.e. |
| `void` | `navigateTo(ViewArea viewArea)` | Shows the given view area in the model animation panel |
| `void` | `onAgentDestroyed_xjal(Agent ao)` | A callback called by the engine when an agent is being destroyed. |
| `void` | `openWebSite(String url)` | Opens web page with the given URL in the browser |
| `void` | `postExperimentSettings()` |  |
| `void` | `removeInspect(Presentable p, String name)` | Removes the inspect window for the given element |
| `default void` | `saveSnapshot(String fileName)` | Pauses experiment if it is currently running, saves snapshot and then resumes experiment if it was running  On any error throws nothing. |
| `void` | `saveSnapshot(String fileName, Runnable successfulCallback, Consumer<Throwable> errorCallback)` | Pauses experiment if it is currently running, saves snapshot and then resumes experiment if it was running  On any error throws nothing.  Usage example: |
| `void` | `setCenter(double x, double y)` | Centers the animation view to the given x and y (in the model coordinates) |
| `void` | `setDeveloperPanelEnabled(boolean developerPanelEnabled)` | Enables or disables the developer panel. |
| `void` | `setDeveloperPanelVisibleOnStart(boolean developerPanelVisibleOnStart)` | Shows (if [enabled](#setDeveloperPanelEnabled(boolean))) the developer panel when the model window is shown. |
| `void` | `setFrameFlag(com.anylogic.engine.internal.presentation.FrameFlag frameFlag)` |  |
| `void` | `setMaxFPS(double maxFPS)` |  |
| `void` | `setPresentable(Presentable presentable)` | Sets a new top-level object (Agent or Experiment) to be displayed and navigates to its home point. |
| `void` | `setRunControlEnabled(boolean runControlEnabled)` | Enables or disables Run, Pause, and Stop buttons on the model toolbar (but not in the developer panel), and sets the corresponding tooltips. |
| `void` | `setSendConsoleItems(boolean yes)` |  |
| `void` | `setSpeed(double speed)` |  |
| `void` | `setSpeedControlEnabled(boolean speedControlEnabled)` | Enables or disables the model execution speed control buttons on the model toolbar (but not in the developer panel), and sets the corresponding tooltips. |
| `void` | `setValue(String pathtofield, IExperimentHost.IValue value)` |  |
| `void` | `setZoom(double zoom)` | Sets the zoom level to the specified value, regardless of the previous one. |
| `void` | `setZoomAndPanningEnabled(boolean zoomAndPanningEnabled)` | Enables or disables zoom & panning initiated from the GUI (button. |
| `void` | `showAllInspectionWindows()` | Allow inspection windows to be displayed and display all visible inspection windows if they were hidden by call of [hideAllInspectionWindows()](#hideAllInspectionWindows()) |
| `void` | `showErrorDialog(String text, String title)` | Shows a standard error dialog box with the given text. |
| `void` | `showErrorInModelDialog(String text, String title)` | Shows a standard 'error in model logic' dialog box with the given text. |
| `void` | `showMessageDialog(String text)` | Shows a standard message dialog box with the given text. |
| `void` | `zoomIn(double coefficient)` | Zooms in the animation view by the given amount |
| `void` | `zoomOut(double coefficient)` | Zooms out the animation view by the given amount |
