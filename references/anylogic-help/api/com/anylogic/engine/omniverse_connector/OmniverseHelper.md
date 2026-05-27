*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/omniverse_connector/OmniverseHelper.html>*

---

Package [com.anylogic.engine.omniverse\_connector](package-summary.md)

# Class OmniverseHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.omniverse\_connector.OmniverseHelper

---

```
@AnyLogicInternalAPI
public class OmniverseHelper
extends Object
```

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final int` | `OMNIVERSE_CONNECTOR_DEFAULT_PORT` |  |
| `static final String` | `OMNIVERSE_PROTOCOL` |  |
| `static final String` | `RELATIVE_SCENE_PREFIX` |  |
| `static final String` | `ROOT_PRIM_NAME` |  |
| `static final String` | `USD_CONTEXT_COLLECTION_KEY` |  |
| `static final String` | `USD_EXTENSION` |  |
| `static final String` | `USDA_EXTENSION` |  |
| `static final String` | `USDC_EXTENSION` |  |
| `static final String` | `USDZ_EXTENSION` |  |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `OmniverseHelper()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static String` | `combineUsdPaths(String parent, String child)` |  |
| `static void` | `exportStage(String stagePath, String exportPath, boolean flatten)` |  |
| `static List<String>` | `formatAssetPath(String modelUsdPath, String scenePath)` |  |
| `static String` | `formatPrimName(String objectName, String parent)` |  |
| `static String` | `getConnectorPath()` |  |
| `static String` | `getResourceUsdPath(String scenePath, String objectFilePath, boolean isLocalRender)` |  |
| `static boolean` | `isOmniverseConnectorInstalled()` |  |
| `static boolean` | `isOpenStageSupported()` |  |
| `static boolean` | `isRenderModelRun()` |  |
| `static boolean` | `isValidOmniversePath(String path)` |  |
| `static boolean` | `isValidPath(String path, boolean isOmniversePath)` |  |
| `static boolean` | `isValidUsdPath(String path)` |  |
| `static boolean` | `openScene(String path)` |  |
| `static void` | `openSceneIfNeeded(OmniverseSyncParameters omniverseSyncParameters)` |  |
| `static void` | `openSceneIfNeeded(String scenePath, boolean openSceneConfigured)` |  |
| `static void` | `startLocalConnectorIfNeeded(OmniverseSyncParameters omniverseSyncParameters)` |  |
| `static void` | `startLocalConnectorIfNeeded(String password, boolean startConnectorConfigured)` |  |
