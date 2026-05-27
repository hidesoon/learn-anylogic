*来源 (Source): <https://anylogic.help/advanced/omniverse/api.html>*

---

# Omniverse: Connector API

* [Calling Omniverse functions](#calling-omniverse-functions)
  + [Obtaining the representation](#obtaining-the-representation)
  + [Customizing the connection](#customizing-the-connection)
* [The UsdRepresentation object](#the-usdrepresentation-object)

[Omniverse connector](https://anylogic.help/anylogic/3d/omniverse.html)[Rendering and customization](customization.md)[Prerequisites](prerequisites.md)

In addition to setting up the association between a model element and a
primShort for “primitive”, the prim is the basic unit of Omniverse. Everything that is imported or created into a USD scene is a prim. This includes cameras, sounds, lights, meshes, and so on. Technically, a primitive is a container of metadata and properties that can also contain other prims.
through the GUI, you can also take advantage of the API to set and fine-tune such a connection.

## Calling Omniverse functions

The UsdContext object is the main interface for interacting with and managing
USDUniversal Scene Description (USD) is the basic representation for assets in Omniverse.
data within your code, providing integration between various elements of your scene and their corresponding USD representations. Through the UsdContext object, you can link scene elements to USD prims (primitive elements), manipulate USD structures, and configure the connection and synchronization between the application and the USD stage. The UsdContext includes essential connection information such as parameters, the scene path, and other configuration details; it also manages the mapping of individual elements — such as 3D shapes — to their USD prims.

For example, to connect a 3D shape representing a specific person to a prim, you can use:

> getUsdContext().addUsdRepresentation(new UsdRepresentation(specialPerson, "/World/someSpecialPerson"));

In this example, getUsdContext() retrieves the UsdContext object, and addUsdRepresentation() is called to set up an updater that ensures the specified shape (specialPerson) is properly linked and updated within the USD scene.

In addition, some of the functions (like setGlobalCoordinateTransform()) accept functions to be passed as parameters. Consider the following example:

```
Consumer<PositionAndScale> transformation = (PositionAndScale position) -> {
    position.x += 10;
    position.y += 5;
    position.z += 3;
};

// Set the global coordinate transform for the context
transformedUsdContext = getUsdContext().setGlobalCoordinateTransform(transformation);
```

Here, we apply the transformation function to all USD context, so that the Consumer elements within the scene will all be moved according to the rule specified in the function.

### Obtaining the representation

The following UsdContext functions are designed to retrieve the UsdRepresentation object which is used to represent the connection between individual objects and their prims.

| Function | Description |
| --- | --- |
| UsdRepresentation createUsdRepresentation(E element, String primPath) | Create a connection between a model element and a USD prim.   E — An element of the model (an agent, a shape, and so on).  primPath — A path to the prim within the USD scene. |
| void addUsdRepresentation(UsdRepresentation<?> usdRepresentation) | Adds a manually created UsdRepresentation object to use during the model run.   usdRepresentation — A manually created UsdRepresentation object. |
| UsdRepresentation getUsdRepresentation(Object obj) | Gets a UsdRepresentation object associated with the model element. Returns an UsdRepresentation object or null if it was not configured yet.   obj — The model element. |

### Customizing the connection

Other functions exposed by the object are used to configure the connection:

| Function | Description |
| --- | --- |
| UsdContext setGlobalCoordinateTransform(Position transformation) | Sets the default position transformation function that will be applied to the positions of the model elements before applying to the connected USD prims.  Returns the reconfigured UsdContext object.   transformation — The transformation function. |
| UsdContext fixBasisMirroring() | Applies Y-axis mirroring to the USD scene.  Returns the reconfigured UsdContext object. |
| UsdContext setConnectionParameters(String scenePath, String password, UsdRepresentation<?>... usdRepresentations) | Configures the parameters used to connect to the Omniverse scene.  Returns the reconfigured UsdContext object.    scenePath — The path to the USD scene on the Omniverse Nucleus server.  password — The password to use to connect to the server in case Omniverse is hosted on a different computer.  usdRepresentations — The collection of representations (UsdRepresentation objects) that connect the model elements to USD prims. |
| UsdContext setConnectionParameters(String scenePath, String password, boolean startLocalConnector, boolean openScene, UsdRepresentation<?>... usdRepresentations) | Configures the parameters used to connect to the Omniverse scene.  Returns the reconfigured UsdContext object.    scenePath — The path to the USD scene on the Omniverse Nucleus server.  password — The password to use to connect to the server in case Omniverse is hosted on a different computer.  startLocalConnector — Run AnyLogic Omniverse Connector at model startup (in case you need to run it separately or on a different computer).  openScene — The Boolean value that defines whether AnyLogic should attempt launching the scene in Nucleus upon model startup. For this to work, Composer should be installed locally on the current computer.  usdRepresentations — The collection of representations (UsdRepresentation objects) that connect the model elements to USD prims. |

## The UsdRepresentation object

This object represents the connection between the AnyLogic element and its USD
primShort for “primitive”, the prim is the basic unit of Omniverse. Everything that is imported or created into a USD scene is a prim. This includes cameras, sounds, lights, meshes, and so on. Technically, a primitive is a container of metadata and properties that can also contain other prims.
.

The UsdRepresentation is a parent object which is extended by multiple inheritors for different types of model elements:

* ShapeUsdRepresentation — Associates a single shape element with a prim.
* AgentUsdRepresentation — Associates a single agent with a prim.
* JibCraneUsdRepresentation — Associates a [jib crane](https://anylogic.help/markup/crane.html) with a prim.
* OverheadCraneUsdRepresentation — Associates an [overhead crane](https://anylogic.help/markup/crane-overhead.html) with a prim.
* ElevatorUsdRepresentation — Associates a [pedestrian elevator](https://anylogic.help/markup/elevator.html) with a prim.
* LiftUsdRepresentation — Associates a [lift](https://anylogic.help/markup/lift.html) (vertical conveyor) with a prim prims.
* PopulationUsdRepresentation — Associates an agent population with USD prims.

Each of these updaters has a set of functions to modify the connections between AnyLogic elements and prims. The valueProvider argument should be passed as a function.

| Function | Description |
| --- | --- |
| void addAttrUpdater(String attrName, Function<A, object> valueProvider) | Adds an attribute updater for a prim depending on the element state.   attrName — The name of the attribute of the USD object that needs to be changed.  valueProvider — The function that generates an object representation of an attribute value being updated. |
| void addAttrUpdater(String pathInsidePrim, String attrName, Function<A, Object> valueProvider) | Adds an attribute updater for an embedded prim depending on the element state.   pathInsidePrim — A relative part to an embedded prim that needs to be changed.  attrName — The name of the attribute of the USD object that needs to be changed.  valueProvider — The function that generates an object representation of an attribute value being updated. |
| void addVariantUpdater(String varsetName, Function<A, Object> variantProvider) | Adds a variant updater (a set of alternative configurations) for a prim. See more in the [official documentation](https://docs.omniverse.nvidia.com/usd/latest/learn-openusd/terms/variant-set.html).   varsetName — The name of the variant set.  variantProvider — The function that generates the name of the USD prim variant depending on the state of the element. |
| void addVariantUpdater(String pathInsidePrim, String varsetName, Function<A, Object> variantProvider) | Adds a variant updater (a set of alternative configurations) for an embedded prim. See more in the [official documentation](https://docs.omniverse.nvidia.com/usd/latest/learn-openusd/terms/variant-set.html).   pathInsidePrim — A relative part to an embedded prim that needs to be changed.  varsetName — The name of the variant set.  variantProvider — The function that generates the name of the USD prim variant depending on the state of the element. |
