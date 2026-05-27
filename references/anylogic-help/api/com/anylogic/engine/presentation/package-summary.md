*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/presentation/package-summary.html>*

---

# Package com.anylogic.engine.presentation

---

| Class | Description |
| --- | --- |
| [AgentAnimationSettings](AgentAnimationSettings.md "class in com.anylogic.engine.presentation") |  |
| [Camera3D](Camera3D.md "class in com.anylogic.engine.presentation") | 3D camera object. |
| [ColorConstants](ColorConstants.md "interface in com.anylogic.engine.presentation") |  |
| [Configuration3D](Configuration3D.md "class in com.anylogic.engine.presentation") | Configuration of 3D world of the associated agent  This object controls the background color and grid at the Z=0 plane.  Background and grid are only applied at the scope of the underlying agent. |
| [DatabaseConstants](DatabaseConstants.md "interface in com.anylogic.engine.presentation") |  |
| [FileResourceUtils](FileResourceUtils.md "class in com.anylogic.engine.presentation") | *This class is not designed to be accessed by user*  Utilities for presentation purposes shared with AL IDE |
| [ImageChangedListener](ImageChangedListener.md "interface in com.anylogic.engine.presentation") | Deprecated. |
| [INavigationPoint](INavigationPoint.md "interface in com.anylogic.engine.presentation") |  |
| [InternalCADFormat](InternalCADFormat.md "interface in com.anylogic.engine.presentation") | **This class is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| [LaunchConfiguration](LaunchConfiguration.md "class in com.anylogic.engine.presentation") | **This class is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| [LegacyShapeGISMapProjection](LegacyShapeGISMapProjection.md "class in com.anylogic.engine.presentation") | Deprecated. |
| [LegacyShapeGISMapStuff](LegacyShapeGISMapStuff.md "class in com.anylogic.engine.presentation") | Deprecated. |
| [LegacyShapeGISMapStuff.ALListenerList](LegacyShapeGISMapStuff.ALListenerList.md "class in com.anylogic.engine.presentation")<T> | Deprecated. |
| [Light3D](Light3D.md "class in com.anylogic.engine.presentation") | Base class for all 3D lights, may be added to 3D groups for scene lighting    The light consists of a number of different components: Ambient, Diffuse and Specular. *Ambient light* is a light that had scattered for many times, so that it does not have any certain direction. |
| [Light3D.CarHeadlight](Light3D.CarHeadlight.md "class in com.anylogic.engine.presentation") |  |
| [Light3D.Daylight](Light3D.Daylight.md "class in com.anylogic.engine.presentation") |  |
| [Light3D.Moonlight](Light3D.Moonlight.md "class in com.anylogic.engine.presentation") |  |
| [Light3D.StreetLight](Light3D.StreetLight.md "class in com.anylogic.engine.presentation") |  |
| [Light3DAmbient](Light3DAmbient.md "class in com.anylogic.engine.presentation") | 3D ambient light, may be added to 3D groups for scene lighting  Ambient light is a light that had scattered for many times, so that it does not have any certain direction. |
| [Light3DDirectional](Light3DDirectional.md "class in com.anylogic.engine.presentation") | 3D directional light, may be added to 3D groups for scene lighting  Directional source of light is located in some infinitely distant point. |
| [Light3DPoint](Light3DPoint.md "class in com.anylogic.engine.presentation") | 3D point light, may be added to 3D groups for scene lighting  Point source of light is located in one particular [`point`](Light3DPoint.md#setPos(double,double,double)) of space. |
| [Light3DSpot](Light3DSpot.md "class in com.anylogic.engine.presentation") | 3D spot light, may be added to 3D groups for scene lighting  Spot source of light is a particular case of a [`point light`](Light3DPoint.md "class in com.anylogic.engine.presentation"). |
| [LineArrowStyle](LineArrowStyle.md "enum class in com.anylogic.engine.presentation") |  |
| [LineStyle](LineStyle.md "enum class in com.anylogic.engine.presentation") | Line style constants |
| [LinkToAgentAnimator](LinkToAgentAnimator.md "interface in com.anylogic.engine.presentation") |  |
| [ModelElementDescriptor](ModelElementDescriptor.md "class in com.anylogic.engine.presentation") | As long as at runtime the information about the model elements such as position of their icons, visibility of labels, and sometimes even type is lost, this class should contain all info needed for displaying the element and its info at runtime, including the reference to the element itself. |
| [ModelElementDescriptorUtils](ModelElementDescriptorUtils.md "class in com.anylogic.engine.presentation") | As long as at runtime the information about the model elements such as position of their icons, visibility of labels, and sometimes even type is lost, this class should contain all info needed for displaying the element and its info at runtime, including the reference to the element itself. |
| [ModelElementType](ModelElementType.md "enum class in com.anylogic.engine.presentation") |  |
| [ModelElementTypeUtils](ModelElementTypeUtils.md "enum class in com.anylogic.engine.presentation") |  |
| [Navigation3DType](Navigation3DType.md "enum class in com.anylogic.engine.presentation") | 3D Window navigation mode constants |
| [NetworkActivityMonitorImpl](NetworkActivityMonitorImpl.md "class in com.anylogic.engine.presentation") | **This class is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| [Object3DAxisOrder](Object3DAxisOrder.md "enum class in com.anylogic.engine.presentation") |  |
| [Object3DInternalLighting](Object3DInternalLighting.md "enum class in com.anylogic.engine.presentation") | This enum defines how the internal lights located inside [`Shape3DObject`](Shape3DObject.md "class in com.anylogic.engine.presentation") will operate on the scene: [turned off](Object3DInternalLighting.md#OBJECT_3D_INTERNAL_LIGHTING_OFF), [lighting this 3D object only](Object3DInternalLighting.md#OBJECT_3D_INTERNAL_LIGHTING_INSIDE) (self lighting), or [lighting on the global level](Object3DInternalLighting.md#OBJECT_3D_INTERNAL_LIGHTING_GLOBAL) (like headlamp of the car). |
| [PresentationUpdater](PresentationUpdater.md "class in com.anylogic.engine.presentation") |  |
| [ProgressConsumer](ProgressConsumer.md "interface in com.anylogic.engine.presentation") | Interface for object which can be notified with the progress information |
| [ReplicatedShape](ReplicatedShape.md "class in com.anylogic.engine.presentation")<T extends [Shape](Shape.md "class in com.anylogic.engine.presentation")> | Persistent replicated shape - a container for a number of shapes of the same type but possibly different properties. |
| [ResourceFileLocation](ResourceFileLocation.md "enum class in com.anylogic.engine.presentation") | *This class is not designed to be accessed by user* |
| [Shape](Shape.md "class in com.anylogic.engine.presentation") | The base class for all graphical shapes and also for all controls.  Shapes allow direct programmatic control, i.e. |
| [Shape3D](Shape3D.md "class in com.anylogic.engine.presentation") |  |
| [Shape3DGroup](Shape3DGroup.md "class in com.anylogic.engine.presentation") | Deprecated. this class is deprecated and will be removed in future. |
| [Shape3DObject](Shape3DObject.md "class in com.anylogic.engine.presentation") | 3D object shape loaded from COLLADA (.dae) file. |
| [ShapeAgentGroup\_xjal](ShapeAgentGroup_xjal.md "class in com.anylogic.engine.presentation") | Persistent group of agents shape. |
| [ShapeAgentPopulationGroup](ShapeAgentPopulationGroup.md "class in com.anylogic.engine.presentation") |  |
| [ShapeArc](ShapeArc.md "class in com.anylogic.engine.presentation") | Arc shape. |
| [ShapeArrowLine](ShapeArrowLine.md "class in com.anylogic.engine.presentation") | A line shape with optional arrows. |
| [ShapeButton](ShapeButton.md "class in com.anylogic.engine.presentation") | Button control. |
| [ShapeCAD](ShapeCAD.md "class in com.anylogic.engine.presentation") | Persistent CAD drawing shape. |
| [ShapeCanvas](ShapeCanvas.md "class in com.anylogic.engine.presentation") | A raster image whose pixels can be modified dynamically at runtime. |
| [ShapeCheckBox](ShapeCheckBox.md "class in com.anylogic.engine.presentation") | Checkbox control. |
| [ShapeComboBox](ShapeComboBox.md "class in com.anylogic.engine.presentation") | Combo box control. |
| [ShapeControl](ShapeControl.md "class in com.anylogic.engine.presentation") | The base class for all controls (like buttons, sliders, text fields, and also charts). |
| [ShapeControl.ValueType](ShapeControl.ValueType.md "enum class in com.anylogic.engine.presentation") |  |
| [ShapeCurve](ShapeCurve.md "class in com.anylogic.engine.presentation") | Persistent curve shape. |
| [ShapeDrawMode](ShapeDrawMode.md "enum class in com.anylogic.engine.presentation") |  |
| [ShapeEmbeddedObjectIcon](ShapeEmbeddedObjectIcon.md "class in com.anylogic.engine.presentation") | Persistent presentation of Embedded Object icon shape plus some info. |
| [ShapeEmbeddedObjectPresentation](ShapeEmbeddedObjectPresentation.md "class in com.anylogic.engine.presentation") | Persistent presentation of Embedded Object shape. |
| [ShapeFileChooser](ShapeFileChooser.md "class in com.anylogic.engine.presentation") | File chooser control. |
| [ShapeFileChooser.Type](ShapeFileChooser.Type.md "enum class in com.anylogic.engine.presentation") | File chooser type constants |
| [ShapeGISMap](ShapeGISMap.md "class in com.anylogic.engine.presentation") | GIS map projection manager and map renderer (persistent GIS Map shape which displays and map projection)  GIS map is a [`Shape`](Shape.md "class in com.anylogic.engine.presentation") and it can be placed on the model animation: it renders the associated map projection on the screen  This class provides several projection methods |
| [ShapeGISMap.Layer](ShapeGISMap.Layer.md "class in com.anylogic.engine.presentation") | Class which stores GIS map layer information |
| [ShapeGroup](ShapeGroup.md "class in com.anylogic.engine.presentation") | Group shape. |
| [ShapeImage](ShapeImage.md "class in com.anylogic.engine.presentation") | Persistent image shape. |
| [ShapeInputControl](ShapeInputControl.md "class in com.anylogic.engine.presentation") |  |
| [ShapeInspect](ShapeInspect.md "class in com.anylogic.engine.presentation") |  |
| [ShapeInspect.FakeInspectedShape](ShapeInspect.FakeInspectedShape.md "class in com.anylogic.engine.presentation") |  |
| [ShapeLine](ShapeLine.md "class in com.anylogic.engine.presentation") | A basic line. |
| [ShapeLineFill](ShapeLineFill.md "class in com.anylogic.engine.presentation") | An intermediate base class - for all shapes that have line and fill. |
| [ShapeListBox](ShapeListBox.md "class in com.anylogic.engine.presentation") | List box control. |
| [ShapeModelElementsGroup](ShapeModelElementsGroup.md "class in com.anylogic.engine.presentation") | Shape containing/drawing model elements of agent / simulation (variables, events, flowchart blocks etc.) |
| [ShapeModelPrimitives](ShapeModelPrimitives.md "class in com.anylogic.engine.presentation") |  |
| [ShapeMultiplePoints](ShapeMultiplePoints.md "class in com.anylogic.engine.presentation") | A base class for shapes having multiple points, such as polyline or curve. |
| [ShapeOval](ShapeOval.md "class in com.anylogic.engine.presentation") | Persistent oval shape. |
| [ShapePolyLine](ShapePolyLine.md "class in com.anylogic.engine.presentation") | Persistent polyline shape. |
| [ShapeProgressBar](ShapeProgressBar.md "class in com.anylogic.engine.presentation") | Progress bar control. |
| [ShapeRadioButtonGroup](ShapeRadioButtonGroup.md "class in com.anylogic.engine.presentation") | A group of radio buttons.  User's radio button group. |
| [ShapeRectangle](ShapeRectangle.md "class in com.anylogic.engine.presentation") | Persistent rectangle shape. |
| [ShapeRoundedRectangle](ShapeRoundedRectangle.md "class in com.anylogic.engine.presentation") | Persistent rounded rectangle shape. |
| [ShapeScale](ShapeScale.md "class in com.anylogic.engine.presentation") | This shape draws [`Scale`](../Scale.md "class in com.anylogic.engine") of the agent on its animation |
| [ShapeSlider](ShapeSlider.md "class in com.anylogic.engine.presentation") | Slider control. |
| [ShapeSVG](ShapeSVG.md "class in com.anylogic.engine.presentation") | A custom SVG image rendered from the SVG XML provided by the user as a String object. |
| [ShapeText](ShapeText.md "class in com.anylogic.engine.presentation") | Persistent text shape. |
| [ShapeTextField](ShapeTextField.md "class in com.anylogic.engine.presentation") | TextField control.  User's text field. |
| [ShapeTopLevelPresentationGroup](ShapeTopLevelPresentationGroup.md "class in com.anylogic.engine.presentation") | Top-level group of agent or experiment presentation |
| [ShapeWindow3D](ShapeWindow3D.md "class in com.anylogic.engine.presentation") | The window showing 3D world on the model animation.  This is a shape like any control which is located on the model animation canvas. |
| [SharedConstants](SharedConstants.md "interface in com.anylogic.engine.presentation") |  |
| [SkyboxType](SkyboxType.md "enum class in com.anylogic.engine.presentation") |  |
| [SVGElement](SVGElement.md "interface in com.anylogic.engine.presentation") | **This class is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| [SVGUtils](SVGUtils.md "class in com.anylogic.engine.presentation") | **This class is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| [SVGUtils.SVGCadDescriptor](SVGUtils.SVGCadDescriptor.md "class in com.anylogic.engine.presentation") |  |
| [SVGUtils.SVGCadLayerDescriptor](SVGUtils.SVGCadLayerDescriptor.md "class in com.anylogic.engine.presentation") |  |
| [TextAlignment](TextAlignment.md "enum class in com.anylogic.engine.presentation") | Text alignment type constants |
| [Texture](Texture.md "class in com.anylogic.engine.presentation") | Objects of this class may be used to define the appearance of shapes' parts. |
| [UsdElement](UsdElement.md "interface in com.anylogic.engine.presentation") |  |
| [UtilitiesColor](UtilitiesColor.md "class in com.anylogic.engine.presentation") |  |
| [ViewArea](ViewArea.md "class in com.anylogic.engine.presentation") | View area class.  This element references to a particular model animation coordinates of agent/experiment.  Provides ability of fast and convenient animation positioning in the model animation panel (using controls on toolbar or API, see: [`ViewArea.navigateTo()`](ViewArea.md#navigateTo()), `Panel#navigateTo(ViewArea)`). |
