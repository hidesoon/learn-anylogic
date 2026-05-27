*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/InternalCADFormat.html>*

---

Package [com.anylogic.engine.presentation](package-summary.md)

# Interface InternalCADFormat

---

```
@AnyLogicInternalAPI
public interface InternalCADFormat
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final String` | `ANY_LOGIC_CAD_TITLE_PREFIX` | The first data stored in the internal AnyLogic CAD file  File format:  `&ltString&gt` `ANY_LOGIC_CAD_TITLE_PREFIX + version`  `&ltint&gt` version  `&ltdouble&gt` x0 coordinate of top-left corner  `&ltdouble&gt` y0 coordinate of top-left corner  `&ltdouble&gt` width of the CAD bounds  `&ltdouble&gt` height of the CAD bounds  [a sequence of commands stored as command id - byte - followed by command-specific contents] - see `CMD_*` constants of this class  `&ltbyte&gt` command  ... |
| `static final byte` | `CMD_CLOSE` | Path command. |
| `static final byte` | `CMD_CUBICTO` | Path command. |
| `static final byte` | `CMD_END` | End of CAD file |
| `static final byte` | `CMD_LAYER` | Starts new layer.  Command contents:  `&ltString&gt` layer name  {  `&ltbyte&gt` CMD\_SET\_COLOR  `&ltColor&gt` default layer color  |  `&ltbyte&gt` CMD\_NO\_COLOR  }  `&ltint&gt` number of paths |
| `static final byte` | `CMD_LINETO` | Path command. |
| `static final byte` | `CMD_MOVETO` | Path command. |
| `static final byte` | `CMD_NO_COLOR` | Sets null color. |
| `static final byte` | `CMD_PATH_DRAW` | Starts new path which should be drawn  Command contents:  `&ltint&gt` number of commands in the path |
| `static final byte` | `CMD_PATH_FILL` | Starts new path which should be filled, the same command contents as in [`CMD_PATH_DRAW`](#CMD_PATH_DRAW) |
| `static final byte` | `CMD_QUADTO` | Path command. |
| `static final byte` | `CMD_SET_COLOR` | Sets new color.  Command contents:  `&ltint&gt` color value (see [`Color.getRGB()`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html#getRGB() "class or interface in java.awt")) |
| `static final byte` | `CMD_SET_WINDING` | Sets new winding rule.  Command contents:  `&ltint&gt` int value of [`PathIterator.getWindingRule()`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/geom/PathIterator.html#getWindingRule() "class or interface in java.awt.geom") |
| `static final int` | `CURRENT_VERSION` |  |
