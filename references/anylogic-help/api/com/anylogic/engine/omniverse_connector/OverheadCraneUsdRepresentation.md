*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/omniverse_connector/OverheadCraneUsdRepresentation.html>*

---

Package [com.anylogic.engine.omniverse\_connector](package-summary.md)

# Class OverheadCraneUsdRepresentation

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.omniverse\_connector.AbstractUsdRepresentation](AbstractUsdRepresentation.md "class in com.anylogic.engine.omniverse_connector")<[OverheadCrane](../markup/OverheadCrane.md "class in com.anylogic.engine.markup")<?>>

com.anylogic.engine.omniverse\_connector.OverheadCraneUsdRepresentation

All Implemented Interfaces:
:   `UsdRepresentation<OverheadCrane<?>>`

---

```
public class OverheadCraneUsdRepresentation
extends AbstractUsdRepresentation<OverheadCrane<?>>
```

Associates an overhead crane with a prim.

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `OverheadCraneUsdRepresentation(UsdContext context, OverheadCrane<?> crane, String cranePrimPath)` | Default crane hierarchy should be as follows |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `OverheadCraneUsdRepresentation` | `enableBridgeVariant()` | Adds a variant updater (a set of alternative configurations) to bridge prim. |
| `OverheadCraneUsdRepresentation` | `enableCraneVariant(String varsetName, Function<OverheadCrane<?>,String> provider)` | Sets a variant updater (a set of alternative configurations) for a crane trolley prim |
| `OverheadCraneUsdRepresentation` | `enableHookVariant()` | The method adds VariantUpdater to hook prim. |
| `OverheadCraneUsdRepresentation` | `enableTrolleyVariant()` | Adds a variant updater (a set of alternative configurations) to trolley prim. |
| `void` | `fillFrame(OmniFrame frame)` |  |
| `OverheadCraneUsdRepresentation` | `setBridgePathProvider(Function<Integer,String> bridgePathProvider)` | Sets function to provide path to crane bridge USD primitive |
| `OverheadCraneUsdRepresentation` | `setBrigdeVariantUpdater(String varsetName, Function<Integer,String> provider)` | Sets a variant updater (a set of alternative configurations) for a crane trolley prim |
| `OverheadCraneUsdRepresentation` | `setHookPathProvider(Function<Integer,String> hookPathProvider)` | Sets function to provide path for crane hook USD primitive |
| `OverheadCraneUsdRepresentation` | `setHookVariantUpdater(String varsetName, Function<Integer,String> provider)` | Sets a variant updater (a set of alternative configurations) for a crane hook prim |
| `OverheadCraneUsdRepresentation` | `setTrolleyPathProvider(Function<Integer,String> trolleyPathProvider)` | Sets function to provide path to crane trolley USD primitive |
| `OverheadCraneUsdRepresentation` | `setTrolleyVariantUpdater(String varsetName, Function<Integer,String> provider)` | Sets a variant updater (a set of alternative configurations) for a crane trolley prim |
| `OverheadCraneUsdRepresentation` | `syncCraneRootPosition()` |  |
