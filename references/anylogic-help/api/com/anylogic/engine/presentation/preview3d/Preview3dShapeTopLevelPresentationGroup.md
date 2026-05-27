*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/preview3d/Preview3dShapeTopLevelPresentationGroup.html>*

---

Package [com.anylogic.engine.presentation.preview3d](package-summary.md)

# Class Preview3dShapeTopLevelPresentationGroup

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.anylogic.engine.presentation.Shape](../Shape.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.Shape3D](../Shape3D.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeGroup](../ShapeGroup.md "class in com.anylogic.engine.presentation")

[com.anylogic.engine.presentation.ShapeTopLevelPresentationGroup](../ShapeTopLevelPresentationGroup.md "class in com.anylogic.engine.presentation")

com.anylogic.engine.presentation.preview3d.Preview3dShapeTopLevelPresentationGroup

All Implemented Interfaces:
:   `com.anylogic.engine.internal.Child`, `Locatable2D`, `Locatable3D`, `AggregatableAnimationElement`, `HasLevel`, `LevelElement`, `SVGElement`, `UsdElement`, `Serializable`, `Cloneable`

---

```
@AnyLogicInternalAPI
public class Preview3dShapeTopLevelPresentationGroup
extends ShapeTopLevelPresentationGroup
```

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.preview3d.Preview3dShapeTopLevelPresentationGroup)

## Field Summary

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `Preview3dShapeTopLevelPresentationGroup(Presentable presentable, AtomicBoolean sendCameras, Map<Long,Camera3D> cameras)` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `void` | `resetSVGState(SVGElement elementBeingDeleted, boolean delete, Consumer<SVGCommand> commandOutput)` | Reset SVG state goes through the entire shape hierarchy and delete (generate "D" command) child shapes if needed (for example we need to delete Shape3DObjects for instanced objects explicitly in case of deletion group or other hierarchy parent) resetSVGState for children must be called before parent (to generate delete "D" command for children first) |
