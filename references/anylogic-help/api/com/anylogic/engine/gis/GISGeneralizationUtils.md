*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/gis/GISGeneralizationUtils.html>*

---

Package [com.anylogic.engine.gis](package-summary.md)

# Class GISGeneralizationUtils

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.gis.GISGeneralizationUtils

---

```
@AnyLogicInternalAPI
public class GISGeneralizationUtils
extends Object
```

**This class is internal and shouldn't be called by user.**
*it may be removed/renamed in future.*

Author:
:   AnyLogic North America, LLC <https://anylogic.com>

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static double[]` | `get3PointBasedRegion(double[] doubleArray)` |  |
| `static double` | `getDisplayPPM()` | *This method is not designed to be called by user*  Returns 'screen' pixels per 'display' meter for given projection (may be `null`) |
| `static int` | `getMapScaleBasedGeneralizationPrecision(long mapScale)` | *This method is not designed to be called by user* |
| `static double[]` | `getSimplifiedPointList(double[] points, double precisionInMeters, List<Integer> oldIndexes)` | **Attention!** This method may damage contents of the given `points` array. |
