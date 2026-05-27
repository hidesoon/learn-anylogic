*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/SVGUtils.SVGCadDescriptor.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class SVGUtils.SVGCadDescriptor

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.presentation.SVGUtils.SVGCadDescriptor

Enclosing class:
:   [SVGUtils](SVGUtils.md "class in com.anylogic.engine.presentation")

---

```
public static class SVGUtils.SVGCadDescriptor
extends Object
```

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `final double` | `cadHeight` |  |
| `final double` | `cadWidth` |  |
| `final Map<String,SVGUtils.SVGCadLayerDescriptor>` | `layers` |  |

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `SVGCadDescriptor(double width, double height)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static SVGUtils.SVGCadDescriptor` | `deserialize(InputStream stream)` |  |
| `void` | `serialize(File file)` |  |
