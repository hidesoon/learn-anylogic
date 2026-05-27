*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/routing/finders/AbstractNetworkPathFinder.html>*

---

Package [com.anylogic.engine.routing.finders](package-summary.md)

# Class AbstractNetworkPathFinder<N extends INode<N,P>,P extends IPath<N>>

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.anylogic.engine.routing.finders.AbstractNetworkPathFinder<N,P>

Direct Known Subclasses:
:   `ConveyorNetworkPathFinder`, `NetworkPathFinder`

---

```
public abstract class AbstractNetworkPathFinder<N extends INode<N,P>,P extends IPath<N>>
extends Object
```

## Constructor Summary

| Constructor | Description |
| --- | --- |
| `AbstractNetworkPathFinder()` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `static <T> Predicate<T>` | `contains(T... array)` |  |
| `static RouteData` | `findShortestRoute(IPathFinderProviderFactory factory, Collection<RouteData> routes, LengthUnits units)` |  |
| `static <T> Predicate<T>` | `notContains(T... array)` |  |
