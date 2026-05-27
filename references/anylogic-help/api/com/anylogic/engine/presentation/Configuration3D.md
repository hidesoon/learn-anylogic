*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/Configuration3D.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class Configuration3D

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.presentation.Configuration3D

All Implemented Interfaces:
:   `Serializable`

---

```
public class Configuration3D
extends Object
implements Serializable
```

Configuration of 3D world of the associated agent
This object controls the background color and grid at the Z=0 plane.
Background and grid are only applied at the scope of the underlying
agent.

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.Configuration3D)

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `Color` | `getBackgroundColor()` | Returns the background color of 3D world of the agent |
| `Color` | `getGridColor()` | Returns grid color or `null` (if grid is invisible) |
| `SkyboxType` | `getSkybox()` |  |
| `void` | `setBackgroundColor(Color backgroundColor)` | Sets the background color of 3D world of the agent |
| `void` | `setGridColor(Color gridColor)` | Sets new grid color value or disables grid |
| `void` | `setSkybox(SkyboxType skybox)` |  |
