*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/omniverse_connector/JibCraneUsdRepresentation.html>*

---

Package [com.anylogic.engine.omniverse\_connector](package-summary.md)

# Class JibCraneUsdRepresentation

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.omniverse\_connector.AbstractUsdRepresentation](AbstractUsdRepresentation.md "class in com.anylogic.engine.omniverse_connector")<[JibCrane](../markup/JibCrane.md "class in com.anylogic.engine.markup")<?>>

com.anylogic.engine.omniverse\_connector.JibCraneUsdRepresentation

All Implemented Interfaces:
:   `UsdRepresentation<JibCrane<?>>`

---

```
public class JibCraneUsdRepresentation
extends AbstractUsdRepresentation<JibCrane<?>>
```

Associates a jib crane with a prim.

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `JibCraneUsdRepresentation(UsdContext context, JibCrane<?> crane, String cranePrimPath)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `fillFrame(OmniFrame frame)` |  |
| `JibCraneUsdRepresentation` | `setCraneVariantUpdater(String varsetName, Function<JibCrane<?>,String> provider)` | Sets a variant updater (a set of alternative configurations) for a crane prim |
| `void` | `setHookPath(String hookPath)` | Set path to the prim that will be used for the crane’s hook |
| `JibCraneUsdRepresentation` | `setHookVariantUpdater(String varsetName, Function<JibCrane<?>,String> provider)` | Sets a variant updater (a set of alternative configurations) for a crane hook prim |
| `void` | `setJibPath(String jibPath)` | Set path to the prim that will be used for the crane’s jib. |
| `JibCraneUsdRepresentation` | `setJibVariantUpdater(String varsetName, Function<JibCrane<?>,String> provider)` | Sets a variant updater (a set of alternative configurations) for a crane jib prim |
| `void` | `setTrolleyPath(String trolleyPath)` | Set path to the prim that will be used for the crane’s trolley |
| `JibCraneUsdRepresentation` | `setTrolleyVariantUpdater(String varsetName, Function<JibCrane<?>,String> provider)` | Sets a variant updater (a set of alternative configurations) for a crane trolley prim |
