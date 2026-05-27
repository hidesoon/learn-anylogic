*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/routing/finders/IPathFinderProviderFactory.html>*

---

Package [com.anylogic.engine.routing.finders](package-summary.md)

# Interface IPathFinderProviderFactory

---

```
public interface IPathFinderProviderFactory
```

## Field Summary

| Modifier and Type | Field | Description |
| --- | --- | --- |
| `static final IPathFinderProviderFactory` | `DEFAULT_CONVEYOR_NETWORK_FACTORY` |  |
| `static final IPathFinderProviderFactory` | `DEFAULT_NETWORK_FACTORY` |  |
| `static final IRouteScoreProvider` | `DEFAULT_ROUTE_SCORE_PROVIDER` |  |

## Method Summary

| Modifier and Type | Method | Description |
| --- | --- | --- |
| `IAStarProvider` | `create(Object sourceVertex, Point sourcePos, Object targetVertex, Point targetPos)` |  |
| `default IRouteScoreProvider` | `createRouteScoreProvider()` |  |
