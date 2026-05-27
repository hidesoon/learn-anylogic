*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/AnyLogicRuntimePreferences.html>*

---

Package [com.anylogic.engine](package-summary.md)

# Class AnyLogicRuntimePreferences

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.AnyLogicRuntimePreferences

---

```
@AnyLogicInternalAPI
public class AnyLogicRuntimePreferences
extends Object
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Since:
:   7.1

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final String` | `ANYLOGIC_ENGINE_RUNS_IN_APP` | AnyLogic engine runs in application (3D Preview) |
| `static final String` | `ANYLOGIC_INCOMING_PORT` | AnyLogic application port for receiving data from running model |
| `static final String` | `BROWSER_USER_DATA_PATH` | Chromium argument: custom user data dir |
| `static final String` | `BUILT_IN_TILE_CACHE_PATH` |  |
| `static final String` | `ENABLE_2D_VISIBILITY_CHECK` | Try to exclude invisible 2D shapes from animation.  Possible values: true, false |
| `static final String` | `ENABLE_OBJECT3D_LOD` | Simplify distant 3D objects (Level of detail).  Possible values: true, false |
| `static final String` | `ENABLE_WARNINGS` | Check and report warnings during model simulation.  Possible values: true, false |
| `static final String` | `FLOWCHART_COUNTERS_VISIBLE` | Process flowcharts: display or hide number of agents passed through ports, contained inside flowchart blocks etc.  Possible values: true, false |
| `static final String` | `FLOWCHART_PORT_STATE_ANIMATED` | Process flowcharts: show or hide block busy / agent available indicators near ports of flowchart blocks.  Possible values: true, false |
| `static final String` | `GIS_CACHE_SIZE_LIMIT_MB` | AnyLogic application port for receiving data from running model |
| `static final String` | `LANGUAGE_ID` | Localization language code. |
| `static final String` | `OMNIVERSE_EDITOR_PID` |  |
| `static final String` | `PAUSE_EXPERIMENT_AT_START` |  |
| `static final String` | `PERFORMANCE_PARALLEL_WORKERS_COUNT` | Number of parallel processors (cores) to be used by multiple-run experiments (e.g. |
| `static final String` | `PROXY_BYPASS_ADDRESSES` | Proxy settings...  The hosts that should be accessed without the proxy. |
| `static final String` | `PROXY_ENABLED` | Proxy settings...  Possible values: true, false |
| `static final String` | `PROXY_HOST` | Proxy settings...  Possible values: url of the proxy host |
| `static final String` | `PROXY_LOGIN` | Proxy settings... |
| `static final String` | `PROXY_PASSWORD` | Proxy settings... |
| `static final String` | `PROXY_PORT` | Proxy settings...  Possible values: integer number |
| `static final String` | `PROXY_SKIP_BASIC_AUTH` | Proxy settings...  Possible values: true, false |
| `static final String` | `STANDALONE_BROWSER_COMMAND_ARGUMENTS` | Standalone application mode: command arguments for custom browser. |
| `static final String` | `STANDALONE_BROWSER_PATH` | Standalone application mode: path to the browser executable. |
| `static final String` | `STANDALONE_EXPERIMENT` | Experiment class name to be started |
| `static final String` | `STANDALONE_OMNI_CONNECTOR_PORT` |  |
| `static final String` | `STANDALONE_SERVER_PORT` | Standalone application mode: port where the server with the running model will start on. |
| `static final String` | `START_BROWSER` |  |
| `static final String` | `SYSTEM_PROP_SUFFIX_XJAL` |  |
| `static final String` | `USE_OMNIVERSE_PRESENTATION` |  |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AnyLogicRuntimePreferences()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static String` | `getBuiltInTileCachePath()` |  |
| `static boolean` | `isAnyLogicEngineRunsInApp()` |  |
| `static boolean` | `isEnable2DVisibilityCheck()` |  |
| `static boolean` | `isEnableObject3dLod()` |  |
| `static boolean` | `isEnableWarnings()` |  |
| `static boolean` | `isFlowchartCountersVisible()` |  |
| `static boolean` | `isFlowchartPortStateAnimated()` |  |
| `static void` | `setAnyLogicEngineRunsInApp(boolean runsInApp)` |  |
| `static void` | `setBuiltInTileCachePath(String path)` |  |
| `static void` | `setEnable2DVisibilityCheck(Boolean enable)` |  |
| `static void` | `setEnableObject3dLod(Boolean yes)` |  |
| `static void` | `setEnableWarnings(Boolean yes)` |  |
| `static void` | `setFlowchartCountersVisible(Boolean yes)` |  |
| `static void` | `setFlowchartPortStateAnimated(Boolean yes)` |  |
