*来源 (Source): <https://anylogic.help/advanced/code/elements-api.html>*

---

# AnyLogic class reference

* [Palette elements](#palette-elements)

All elements of agents (except for connectors and all types of statechart states) can be accessed from code simply by their names.

Almost all AnyLogic elements are represented as instances of Java classes, having their own methods and data fields.

Here you can find references to the classes that AnyLogic generates for its elements.

To obtain information about functions of an AnyLogic element

1. In this article, expand the required palette’s description by clicking its name in the section below.
2. Find the element in the table. The name of the corresponding Java class is given in the right column. Click the link to open Javadoc help on this class. If it is said that the class is inherited from some base class or classes, all methods of that base class or classes are available to you too.

### Palette elements

Process Modeling Library
:   Refer to the [Process Modeling Library Reference Guide](https://anylogic.help/library-reference-guides/process-modeling-library/index.html) for details.

Material Handling Library
:   Refer to the [Material Handling Library Reference Guide](https://anylogic.help/library-reference-guides/material-handling-library/index.html) for details.

Pedestrian Library
:   Refer to the [Pedestrian Library Reference Guide](https://anylogic.help/library-reference-guides/pedestrian-library/index.html) for details.

Rail Library
:   Refer to the [Rail Library Reference Guide](https://anylogic.help/library-reference-guides/rail-library/index.html) for details.

Road Traffic Library
:   Refer to the [Road Traffic Library Reference Guide](https://anylogic.help/library-reference-guides/road-traffic-library/index.html) for details.

Fluid Library
:   Refer to the [Fluid Library Reference Guide](https://anylogic.help/library-reference-guides/fluid-library/index.html) for details.

System Dynamics
:   | Element | Class |
    | --- | --- |
    | **Stock** | In case the variable is not declared as an array, it is represented in AnyLogic as a primitive variable that you can only access and modify. In case it is declared as an array, it is represented as an instance of [HyperArray](https://anylogic.help/api/com/anylogic/engine/HyperArray.html) class. |
    | **Flow** |
    | **Dynamic variable** |
    | **Link** | Link is a simple graphical element that does not provide API. |
    | **Parameter** | You choose the type/class of the parameter by yourself in the **Type** property of the parameter. You can make your parameter an instance of any primitive [Java type](java-types.md) (int, double, boolean, etc.), or of any Java class you like (String, Date, Color, [HyperArray](https://anylogic.help/api/com/anylogic/engine/HyperArray.html) (the class of the parameter declared as an array) and any other). |
    | **Table Function** | [TableFunction](https://anylogic.help/api/com/anylogic/engine/TableFunction.html) |
    | **Loop** | Loop is a simple graphical element that does not provide API. |
    | **Connector** | You cannot access connectors from code. |

Agent
:   | Element | Class |
    | --- | --- |
    | **Agent** | You define agent types by yourself, so that they get the names you define for them. All agent types inherit from the base class of agents: [Agent](https://anylogic.help/api/com/anylogic/engine/Agent.html). |
    | **Parameter** | You choose the type/class of the parameter by yourself in the **Type** property of the parameter. You can make your parameter an instance of any primitive [Java type](java-types.md) (int, double, boolean, etc.), or of any Java class you like (String, Date, Color, [HyperArray](https://anylogic.help/api/com/anylogic/engine/HyperArray.html) (the class of the parameter declared as an array) and any other). |
    | **Event** | Class of the event depends on its **Trigger type**:  * Timeout: [EventTimeout](https://anylogic.help/api/com/anylogic/engine/EventTimeout.html) * Rate: [EventRate](https://anylogic.help/api/com/anylogic/engine/EventRate.html) * Condition: [EventCondition](https://anylogic.help/api/com/anylogic/engine/EventCondition.html)  All these classes are inherited from the base class [Event](https://anylogic.help/api/com/anylogic/engine/Event.html). |
    | **Dynamic Event** | AnyLogic creates Java class with the name you specify for the dynamic event. All dynamic events that will be created and scheduled during the simulation will be are instances of this class. |
    | **Variable** | You choose the type/class of the variable by yourself in the **Type** property of the variable. You can make your variable instance of any primitive [Java type](java-types.md) (int, double, boolean, etc.), or of any Java class you like. |
    | **Collection** | The type is defined by the user in the **Collection class** property of the collection. The most commonly used collection classes are [ArrayList](https://docs.oracle.com/javase/9/docs/api/java/util/ArrayList.html) and [LinkedList](https://docs.oracle.com/javase/9/docs/api/java/util/LinkedList.html). |
    | Function | You can only call the function by typing its name followed by parentheses. In the case function has some arguments, you should pass argument values separated by commas inside the parentheses. Arguments should be provided in the same order they are defined in the **Function arguments** table. |
    | **Table Function** | [TableFunction](https://anylogic.help/api/com/anylogic/engine/TableFunction.html) |
    | **Schedule** | [Schedule](https://anylogic.help/api/com/anylogic/engine/Schedule.html) |
    | **Port** | The base class for all ports in AnyLogic is [Port](https://anylogic.help/api/com/anylogic/engine/Port.html). However, you can [define your own port classes](../libraries/ports.md#custom-port) with custom functionality. In this case you should make them inherit from Port class. |
    | **Connector** | You cannot access connectors from code. |
    | **Link to agents** | Link to agent implements [LinkToAgent](https://anylogic.help/api/com/anylogic/engine/LinkToAgent.html) interface. |
    | **Statechart** | You can access statechart by the name of its statechart entry point. It is an instance of the class [Statechart](https://anylogic.help/api/com/anylogic/engine/Statechart.html). You can also access transitions programmatically. Class of the transition depends on its trigger type:  * Timeout: [TransitionTimeout](https://anylogic.help/api/com/anylogic/engine/TransitionTimeout.html) * Rate: [TransitionRate](https://anylogic.help/api/com/anylogic/engine/TransitionRate.html) * Condition: [TransitionCondition](https://anylogic.help/api/com/anylogic/engine/TransitionCondition.html) * Message, Arrival: [TransitionMessage](https://anylogic.help/api/com/anylogic/engine/TransitionMessage.html)  All these classes are inherited from the base class [Transition](https://anylogic.help/api/com/anylogic/engine/Transition.html). States, final states, branches, and history states cannot be accessed from code. |

Presentation
:   AnyLogic presentation shapes are instances of the corresponding classes listed in the table below. All these classes are inherited from the base class [Shape](https://anylogic.help/api/com/anylogic/engine/presentation/Shape.html). It contains methods allowing user to change shape's position, visibility, scale, and rotation angle.

    | Element | Class |
    | --- | --- |
    | **Line** | [ShapeLine](https://anylogic.help/api/com/anylogic/engine/presentation/ShapeLine.html) |
    | **Polyline** | [ShapePolyLine](https://anylogic.help/api/com/anylogic/engine/presentation/ShapePolyLine.html) |
    | **Curve** | [ShapeCurve](https://anylogic.help/api/com/anylogic/engine/presentation/ShapeCurve.html) |
    | **Rectangle** | [ShapeRectangle](https://anylogic.help/api/com/anylogic/engine/presentation/ShapeRectangle.html) |
    | **Rounded Rectangle** | [ShapeRoundedRectangle](https://anylogic.help/api/com/anylogic/engine/presentation/ShapeRoundedRectangle.html) |
    | **Oval** | [ShapeOval](https://anylogic.help/api/com/anylogic/engine/presentation/ShapeOval.html) |
    | **Arc** | [ShapeArc](https://anylogic.help/api/com/anylogic/engine/presentation/ShapeArc.html) |
    | **Text** | [ShapeText](https://anylogic.help/api/com/anylogic/engine/presentation/ShapeText.html) |
    | **Image** | [ShapeImage](https://anylogic.help/api/com/anylogic/engine/presentation/ShapeImage.html) |
    | **Canvas** | [ShapeCanvas](https://anylogic.help/api/com/anylogic/engine/presentation/ShapeCanvas.html) |
    | **Group** | [ShapeGroup](https://anylogic.help/api/com/anylogic/engine/presentation/ShapeGroup.html) |
    | **View Area** | [ViewArea](https://anylogic.help/api/com/anylogic/engine/presentation/ViewArea.html) |
    | **CAD Drawing** | [ShapeCAD](https://anylogic.help/api/com/anylogic/engine/presentation/ShapeCAD.html) |
    | **3D Window** | [ShapeWindow3D](https://anylogic.help/api/com/anylogic/engine/presentation/ShapeWindow3D.html) |
    | **3D Object** | [Shape3DObject](https://anylogic.help/api/com/anylogic/engine/presentation/Shape3DObject.html) |
    | **Camera** | [Camera3D](https://anylogic.help/api/com/anylogic/engine/presentation/Camera3D.html) |
    | **Light** | Class of the light depends on its **Light type**:  * Ambient: [Light3DAmbient](https://anylogic.help/api/com/anylogic/engine/presentation/Light3DAmbient.html) * Directional: [Light3DDirectional](https://anylogic.help/api/com/anylogic/engine/presentation/Light3DDirectional.html) * Point: [Light3DPoint](https://anylogic.help/api/com/anylogic/engine/presentation/Light3DPoint.html) * Spot: [Light3DSpot](https://anylogic.help/api/com/anylogic/engine/presentation/Light3DSpot.html)  All these classes are inherited from the base class [Light3D](https://anylogic.help/api/com/anylogic/engine/presentation/Light3D.html). |

Space Markup
:   | Element | Class |
    | --- | --- |
    | **Path** | [Path](https://anylogic.help/api/com/anylogic/engine/markup/Path.html) |
    | **Rectangular Node** | [RectangularNode](https://anylogic.help/api/com/anylogic/engine/markup/RectangularNode.html) |
    | **Polygonal Node** | [PolygonalNode](https://anylogic.help/api/com/anylogic/engine/markup/PolygonalNode.html) |
    | **Point Node** | [PointNode](https://anylogic.help/api/com/anylogic/engine/markup/PointNode.html) |
    | **Attractor** | [Attractor](https://anylogic.help/api/com/anylogic/engine/markup/Attractor.html) |
    | **Pallet Rack** | [PalletRack](https://anylogic.help/api/com/anylogic/engine/markup/PalletRack.html) |
    | GIS |
    | **GIS Map** | [ShapeGISMap](https://anylogic.help/api/com/anylogic/engine/presentation/ShapeGISMap.html) |
    | **GIS Point** | [GISPoint](https://anylogic.help/api/com/anylogic/engine/markup/GISPoint.html) |
    | **GIS Route** | [GISRoute](https://anylogic.help/api/com/anylogic/engine/markup/GISRoute.html) |
    | **GIS Region** | [GISRegion](https://anylogic.help/api/com/anylogic/engine/markup/GISRegion.html) |
    | **Route Provider** | Implements interface [IGISRouteProvider](https://anylogic.help/api/com/anylogic/engine/gis/IGISRouteProvider.html) |
    | Material Handling |  |
    | **Conveyor** | [ConveyorPath](https://anylogic.help/api/com/anylogic/engine/markup/ConveyorPath.html) |
    | **Conveyor spur** | [ConveyorSpur](https://anylogic.help/api/com/anylogic/engine/markup/ConveyorSpur.html) |
    | **Position on Conveyor** | [PositionOnConveyor](https://anylogic.help/api/com/anylogic/engine/markup/PositionOnConveyor.html) |
    | **Transfer Table** | [ConveyorTransferTable](https://anylogic.help/api/com/anylogic/engine/markup/ConveyorTransferTable.html) |
    | **Turntable** | [ConveyorTurntable](https://anylogic.help/api/com/anylogic/engine/markup/ConveyorTurntable.html) |
    | **Turn Station** | [ConveyorTurnStation](https://anylogic.help/api/com/anylogic/engine/markup/ConveyorTurnStation.html) |
    | **Station** | [ConveyorStation](https://anylogic.help/api/com/anylogic/engine/markup/ConveyorStation.html) |
    | **Custom Station** | [ConveyorCustomStation](https://anylogic.help/api/com/anylogic/engine/markup/ConveyorCustomStation.html) |
    | **Jib Crane** | [JibCrane](https://anylogic.help/api/com/anylogic/engine/markup/JibCrane.html) |
    | **Overhead Crane** | [OverheadCrane](https://anylogic.help/api/com/anylogic/engine/markup/OverheadCrane.html) |
    | **Storage** | [Storage](https://anylogic.help/api/com/anylogic/engine/markup/Storage.html) |
    | **Lift** | [Lift](https://anylogic.help/api/com/anylogic/engine/markup/Lift.html) |
    | **Network Port** | [NetworkPort](https://anylogic.help/api/com/anylogic/engine/markup/NetworkPort.html) |
    | **Level Gate** | [LevelGate](https://anylogic.help/api/com/anylogic/engine/markup/LevelGate.html) |
    | **Density Map** | [DensityMap](https://anylogic.help/api/com/anylogic/engine/markup/DensityMap.html) |
    | Pedestrian |
    | **Wall** | [Wall](https://anylogic.help/api/com/anylogic/engine/markup/Wall.html) |
    | **Rectangular Wall** | [RectangularWall](https://anylogic.help/api/com/anylogic/engine/markup/RectangularWall.html) |
    | **Circular Wall** | [CircularWall](https://anylogic.help/api/com/anylogic/engine/markup/CircularWall.html) |
    | **Target Line** | [TargetLine](https://anylogic.help/api/com/anylogic/engine/markup/TargetLine.html) |
    | **Service with Lines** | [ServiceWLine](https://anylogic.help/api/com/anylogic/engine/markup/ServiceWLine.html) Consists of service points ([ServicePoint](https://anylogic.help/api/com/anylogic/engine/markup/ServicePoint.html)) and queue lines ([QueuePath](https://anylogic.help/api/com/anylogic/engine/markup/QueuePath.html)) |
    | **Service with Area** | [ServiceWArea](https://anylogic.help/api/com/anylogic/engine/markup/ServiceWArea.html) Consists of service points ([ServicePoint](https://anylogic.help/api/com/anylogic/engine/markup/ServicePoint.html)) and waiting area ([QueueArea](https://anylogic.help/api/com/anylogic/engine/markup/QueueArea.html)) |
    | **Escalator Group** | [EscalatorGroup](https://anylogic.help/api/com/anylogic/engine/markup/EscalatorGroup.html) Consists of escalators ([Escalator](https://anylogic.help/api/com/anylogic/engine/markup/Escalator.html)) |
    | **Elevator** | [Elevator](https://anylogic.help/api/com/anylogic/engine/markup/Elevator.html) |
    | **Pathway** | [Pathway](https://anylogic.help/api/com/anylogic/engine/markup/Pathway.html) |
    | **Ped Flow Statistics** | [PedFlowStatistics](https://anylogic.help/api/com/anylogic/engine/markup/PedFlowStatistics.html) |
    | **Density Map** | [DensityMap](https://anylogic.help/api/com/anylogic/engine/markup/DensityMap.html) |
    | **Rail** |
    | **Railway Track** | [RailwayTrack](https://anylogic.help/api/com/anylogic/engine/markup/RailwayTrack.html) |
    | **Position on Track** | [PositionOnTrack](https://anylogic.help/api/com/anylogic/engine/markup/PositionOnTrack.html) |
    | Road |
    | **Road** | [Road](https://anylogic.help/api/com/anylogic/engine/markup/Road.html) |
    | **Intersection** | [Intersection](https://anylogic.help/api/com/anylogic/engine/markup/Intersection.html) |
    | **Stop Line** | [StopLine](https://anylogic.help/api/com/anylogic/engine/markup/StopLine.html) |
    | **Bus Stop** | [BusStop](https://anylogic.help/api/com/anylogic/engine/markup/BusStop.html) |
    | **Parking Lot** | [ParkingLot](https://anylogic.help/api/com/anylogic/engine/markup/ParkingLot.html) |
    | Fluid |
    | **Storage Tank** | [StorageTank](https://anylogic.help/api/com/anylogic/engine/markup/StorageTank.html) |
    | **Pipe** | [Pipe](https://anylogic.help/api/com/anylogic/engine/markup/Pipe.html) |
    | **Bulk Conveyor Belt** | [BulkConveyorBelt](https://anylogic.help/api/com/anylogic/engine/markup/BulkConveyorBelt.html) |

Analysis
:   | Element | Class |
    | --- | --- |
    | **Data Set** | [DataSet](https://anylogic.help/api/com/anylogic/engine/analysis/DataSet.html) |
    | **Statistics** | The class of the statistics element depends on the type of statistics:  * Discrete: [StatisticsDiscrete](https://anylogic.help/api/com/anylogic/engine/analysis/StatisticsDiscrete.html)  * Continuous: [StatisticsContinuous](https://anylogic.help/api/com/anylogic/engine/analysis/StatisticsContinuous.html) |
    | **Histogram Data** | Histogram data element is represented in AnyLogic with instance of on of the following classes:  * [HistogramSimpleData](https://anylogic.help/api/com/anylogic/engine/analysis/HistogramSimpleData.html) — Data of a histogram with a fixed minimum, maximum, and number of intervals. * [HistogramSmartData](https://anylogic.help/api/com/anylogic/engine/analysis/HistogramSmartData.html) — Data of a histogram with a fixed number of intervals but auto-adjustable data range.  Both classes are inherited from the base class [HistogramData](https://anylogic.help/api/com/anylogic/engine/analysis/HistogramData.html). |
    | **Histogram2D Data** | [Histogram2DData](https://anylogic.help/api/com/anylogic/engine/analysis/Histogram2DData.html) |
    | **Bar Chart** | [BarChart](https://anylogic.help/api/com/anylogic/engine/analysis/BarChart.html) |
    | **Stack chart** | [StackChart](https://anylogic.help/api/com/anylogic/engine/analysis/StackChart.html) |
    | **Pie Chart** | [PieChart](https://anylogic.help/api/com/anylogic/engine/analysis/PieChart.html) |
    | **Plot** | [Plot](https://anylogic.help/api/com/anylogic/engine/analysis/Plot.html) |
    | **Time Plot** | [TimePlot](https://anylogic.help/api/com/anylogic/engine/analysis/TimePlot.html) |
    | **Time Stack Chart** | [TimeStackChart](https://anylogic.help/api/com/anylogic/engine/analysis/TimeStackChart.html) |
    | **Time Color Chart** | [TimeColorChart](https://anylogic.help/api/com/anylogic/engine/analysis/TimeColorChart.html) |
    | **Histogram** | [Histogram](https://anylogic.help/api/com/anylogic/engine/analysis/Histogram.html) |
    | **Histogram 2D** | [Histogram2D](https://anylogic.help/api/com/anylogic/engine/analysis/Histogram2D.html) |

Controls
:   AnyLogic controls are instances of the corresponding classes listed in the table below. All these classes are inherited from the base class [ShapeControl](https://anylogic.help/api/com/anylogic/engine/presentation/ShapeControl.html) that in turn inherits from the class [Shape](https://anylogic.help/api/com/anylogic/engine/presentation/Shape.html). Shape contains methods allowing user to change control's position, visibility, scale, and rotation angle.

    | Element | Class |
    | --- | --- |
    | **Button** | [ShapeButton](https://anylogic.help/api/com/anylogic/engine/presentation/ShapeButton.html) |
    | **Check Box** | [ShapeCheckBox](https://anylogic.help/api/com/anylogic/engine/presentation/ShapeCheckBox.html) |
    | **Edit Box** | [ShapeTextField](https://anylogic.help/api/com/anylogic/engine/presentation/ShapeTextField.html) |
    | **Radio Buttons** | [ShapeRadioButtonGroup](https://anylogic.help/api/com/anylogic/engine/presentation/ShapeRadioButtonGroup.html) |
    | **Slider** | [ShapeSlider](https://anylogic.help/api/com/anylogic/engine/presentation/ShapeSlider.html) |
    | **Combo Box** | [ShapeComboBox](https://anylogic.help/api/com/anylogic/engine/presentation/ShapeComboBox.html) |
    | **List Box** | [ShapeListBox](https://anylogic.help/api/com/anylogic/engine/presentation/ShapeListBox.html) |
    | **File Chooser** | [ShapeFileChooser](https://anylogic.help/api/com/anylogic/engine/presentation/ShapeFileChooser.html) |
    | **Progress Bar** | [ShapeProgressBar](https://anylogic.help/api/com/anylogic/engine/presentation/ShapeProgressBar.html) |

Statechart
:   You can access statechart by the name of its statechart entry point. It is an instance of the class [Statechart](https://anylogic.help/api/com/anylogic/engine/Statechart.html). You can also access transitions programmatically. Class of the transition depends on its trigger type:

    * Timeout: [TransitionTimeout](https://anylogic.help/api/com/anylogic/engine/TransitionTimeout.html)
    * Rate: [TransitionRate](https://anylogic.help/api/com/anylogic/engine/TransitionRate.html)
    * Condition: [TransitionCondition](https://anylogic.help/api/com/anylogic/engine/TransitionCondition.html)
    * Message, Arrival: [TransitionMessage](https://anylogic.help/api/com/anylogic/engine/TransitionMessage.html)

    All these classes are inherited from the base class [Transition](https://anylogic.help/api/com/anylogic/engine/Transition.html). States, final states, branches, and history states cannot be accessed from code.

Connectivity
:   | Element | Class |
    | --- | --- |
    | **Excel File** | [ExcelFile](https://anylogic.help/api/com/anylogic/engine/connectivity/ExcelFile.html) |
    | **Text File** | [TextFile](https://anylogic.help/api/com/anylogic/engine/connectivity/TextFile.html) |
    | **Database** | [Database](https://anylogic.help/api/com/anylogic/engine/connectivity/Database.html) |

Pictures
:   All pictures are in fact groups of standard AnyLogic shapes and are instances of class [ShapeGroup](https://anylogic.help/api/com/anylogic/engine/presentation/ShapeGroup.html).

3D Objects
:   All 3D objects distributed with AnyLogic are in fact common AnyLogic 3D objects and are instances of class [Shape3DObject](https://anylogic.help/api/com/anylogic/engine/presentation/Shape3DObject.html). Fork Lift Truck and Pallet Trolley are groups (instances of class [ShapeGroup](https://anylogic.help/api/com/anylogic/engine/presentation/ShapeGroup.html)), containing a couple of 3D objects - a man and a forklift/pallet trolley correspondingly. You can ungroup them and use these 3D objects individually.

Experiments
:   Class of the experiment depends on its type:

    * **Simulation:** [ExperimentSimulation](https://anylogic.help/api/com/anylogic/engine/ExperimentSimulation.html)
    * **Optimization** and **Calibration**: [ExperimentOptimization](https://anylogic.help/api/com/anylogic/engine/ExperimentOptimization.html)
    * **Parameters variation**, **Monte Carlo**, and **Sensitivity analysis**: [ExperimentParamVariation](https://anylogic.help/api/com/anylogic/engine/ExperimentParamVariation.html)
    * **Compare runs**: [ExperimentCompareRuns](https://anylogic.help/api/com/anylogic/engine/ExperimentCompareRuns.html)
    * **Reinforcement Learning**: [ExperimentReinforcementLearning](https://anylogic.help/api/com/anylogic/engine/ExperimentReinforcementLearning.html)
    * **Custom**: [ExperimentCustom](https://anylogic.help/api/com/anylogic/engine/ExperimentCustom.html)

    All these classes are inherited from the base class [Experiment](https://anylogic.help/api/com/anylogic/engine/Experiment.html).
