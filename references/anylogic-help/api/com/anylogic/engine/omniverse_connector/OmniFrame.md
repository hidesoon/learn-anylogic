*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/omniverse_connector/OmniFrame.html>*

---

Package [com.anylogic.engine.omniverse\_connector](package-summary.md)

# Class OmniFrame

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.omniverse\_connector.OmniFrame

---

```
@AnyLogicInternalAPI
public class OmniFrame
extends Object
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

## Nested Class Summary

| Modifier and Type | Class | Description |
| --- | --- | --- |
| `static class` | `OmniFrame.FrameInfo` |  |
| `static class` | `OmniFrame.InstancedFieldInfo` |  |
| `static class` | `OmniFrame.PopulationInfo` |  |
| `static class` | `OmniFrame.StaticFieldInfo` |  |

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final OmniFrame` | `NULL_FRAME` |  |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `OmniFrame(long id, boolean fullframe)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addPopulationInfo(OmniFrame.FrameInfo info)` |  |
| `void` | `addStaticAttributesInfo(OmniFrame.FrameInfo info)` |  |
| `void` | `addStaticVariantsInfo(OmniFrame.FrameInfo info)` |  |
| `long` | `getId()` |  |
| `Collection<OmniFrame.FrameInfo>` | `getPopulations()` |  |
| `Collection<OmniFrame.FrameInfo>` | `getStaticsAttributes()` |  |
| `Collection<OmniFrame.FrameInfo>` | `getStaticsVariants()` |  |
| `boolean` | `isFullFrame()` |  |
| `String` | `toString()` |  |
