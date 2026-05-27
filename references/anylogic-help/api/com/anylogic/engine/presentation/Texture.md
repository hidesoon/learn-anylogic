*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/Texture.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Class Texture

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.presentation.Texture

All Implemented Interfaces:
:   `Paint`, `Transparency`, `Serializable`

---

```
public class Texture
extends Object
implements Paint, Serializable
```

Objects of this class may be used to define the appearance of shapes' parts.
`Texture` may be used in the shapes instead of `Color`.
Additionally to the color, this class supports textures.
Example: [`UtilitiesColor.brickRedTexture`](UtilitiesColor.md#brickRedTexture) - texture with red bricks,
may be used as a fill for a rectangle:
`rectangle.setFillColor(brickRedTexture);`

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

See Also:
:   [Serialized Form](https://anylogic.help/api/serialized-form.html#com.anylogic.engine.presentation.Texture)

## Field Summary

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `PaintContext` | `createContext(ColorModel cm, Rectangle deviceBounds, Rectangle2D userBounds, AffineTransform xform, RenderingHints hints)` | Deprecated. this method will be removed in future releases. |
| `boolean` | `equals(Object obj)` |  |
| `Color` | `getAmbientColor()` | Deprecated. this method will be removed in future releases. |
| `Color` | `getDiffuseColor()` | Deprecated. this method will be removed in future releases. |
| `String` | `getName()` | Returns internal name of the texture |
| `Paint` | `getPaint_xjal()` | Deprecated. this method will be removed in future releases. |
| `Color` | `getSpecularColor()` | Deprecated. this method will be removed in future releases. |
| `static Texture` | `getTexture(String name)` | Returns texture object for the given name |
| `int` | `getTransparency()` | Deprecated. this method will be removed in future releases. |
| `int` | `hashCode()` |  |
| `String` | `toString()` |  |
