*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/omniverse_connector/CameraUsdRepresentation.html>*

---

Package [com.anylogic.engine.omniverse\_connector](package-summary.md)

# Class CameraUsdRepresentation

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.omniverse\_connector.AbstractUsdRepresentation](AbstractUsdRepresentation.md "class in com.anylogic.engine.omniverse_connector")<[Camera3D](../presentation/Camera3D.md "class in com.anylogic.engine.presentation")>

com.anylogic.engine.omniverse\_connector.CameraUsdRepresentation

All Implemented Interfaces:
:   `UsdRepresentation<Camera3D>`

---

```
public class CameraUsdRepresentation
extends AbstractUsdRepresentation<Camera3D>
```

Create USD representation for camera

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `CameraUsdRepresentation(UsdContext context, Camera3D objectToWatch, String usdPrimPath)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `addTransformator(Consumer<PositionAndScale> t)` |  |
| `void` | `fillFrame(OmniFrame frame)` |  |
