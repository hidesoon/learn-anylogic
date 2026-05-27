*来源 (Source): <https://anylogic.help/api/com/anylogic/engine/package-summary.html>*

---

# Package com.anylogic.engine

---

| Class | Description |
| --- | --- |
| [AbstractAgentPlainMovementData](AbstractAgentPlainMovementData.md "class in com.anylogic.engine") |  |
| [AbstractLinkToAgent](AbstractLinkToAgent.md "interface in com.anylogic.engine")<T extends [Agent](Agent.md "class in com.anylogic.engine"),A extends [Agent](Agent.md "class in com.anylogic.engine")> |  |
| [AbstractShapeGISMap](AbstractShapeGISMap.md "interface in com.anylogic.engine") | Deprecated. Will be removed in future releases, use [`ShapeGISMap`](presentation/ShapeGISMap.md "class in com.anylogic.engine.presentation") class instead |
| [AccelerationUnits](AccelerationUnits.md "enum class in com.anylogic.engine") | Standard AnyLogic acceleration units, should be used in specific functions and parameters which work with units. |
| [Agent](Agent.md "class in com.anylogic.engine") | This is a base class for all agent classes created by the user. |
| [AgentArrayList](AgentArrayList.md "class in com.anylogic.engine")<E extends [Agent](Agent.md "class in com.anylogic.engine")> | Agent population list based on array implementation  Supports fast element retrieval by its index (the [`AgentArrayList.get(int)`](AgentArrayList.md#get(int)) operation runs in constant time).  The add operation runs in amortized constant time, that is, adding n elements requires O(n) time. |
| [AgentConstants](AgentConstants.md "interface in com.anylogic.engine") |  |
| [AgentDestroyListener](AgentDestroyListener.md "interface in com.anylogic.engine") |  |
| [AgentExtension](AgentExtension.md "interface in com.anylogic.engine") | Base interface for extensions of [`Agent`](Agent.md "class in com.anylogic.engine")s. |
| [AgentExtensionFactory](AgentExtensionFactory.md "class in com.anylogic.engine")<T extends [AgentExtension](AgentExtension.md "interface in com.anylogic.engine")> |  |
| [AgentExtensionImpl](AgentExtensionImpl.md "class in com.anylogic.engine") | Base class for extensions of [`Agent`](Agent.md "class in com.anylogic.engine")s.  Please note that agent, during its lifetime, may change instances of some extensions (e.g. |
| [AgentLinkedHashSet](AgentLinkedHashSet.md "class in com.anylogic.engine")<E extends [Agent](Agent.md "class in com.anylogic.engine")> | Agent population collection based on [`LinkedHashSet`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedHashSet.html "class or interface in java.util") implementation  This collection offers constant time performance for the basic operations (add, remove, contains and size) and guarantees insertion-order during iteration    *Note, that due to set-based implementation, element retrieval by its index ([`AgentLinkedHashSet.get(int)`](AgentLinkedHashSet.md#get(int))) is extremely slow when rapidly invoked it with random index for large collections.* |
| [AgentList](AgentList.md "class in com.anylogic.engine")<E extends [Agent](Agent.md "class in com.anylogic.engine")> | Agent population list interface |
| [AgentOrientation](AgentOrientation.md "enum class in com.anylogic.engine") |  |
| [AgentSpacePosition](AgentSpacePosition.md "class in com.anylogic.engine") |  |
| [AmountType](AmountType.md "enum class in com.anylogic.engine") |  |
| [AmountUnits](AmountUnits.md "enum class in com.anylogic.engine") | Standard AnyLogic amount units, should be used in specific functions and parameters which work with units. |
| [AngleUnits](AngleUnits.md "enum class in com.anylogic.engine") |  |
| [AnyLogicCustomAliasProposal](AnyLogicCustomAliasProposal.md "annotation interface in com.anylogic.engine") | **This class is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| [AnyLogicCustomProposalPriority](AnyLogicCustomProposalPriority.md "annotation interface in com.anylogic.engine") | Users should ignore this annotation.  This annotation is used only inside the AnyLogic, for code completion purposes |
| [AnyLogicCustomProposalPriority.Type](AnyLogicCustomProposalPriority.Type.md "enum class in com.anylogic.engine") |  |
| [AnyLogicCustomProposalType](AnyLogicCustomProposalType.md "annotation interface in com.anylogic.engine") | **This class is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| [AnyLogicCustomProposalType.Label](AnyLogicCustomProposalType.Label.md "enum class in com.anylogic.engine") |  |
| [AnyLogicCustomSerialization](AnyLogicCustomSerialization.md "annotation interface in com.anylogic.engine") | **This class is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  Annotation for custom serialization processing during save to snapshot operations. |
| [AnyLogicCustomSerializationMode](AnyLogicCustomSerializationMode.md "enum class in com.anylogic.engine") | **This class is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*  The mode constants for [`AnyLogicCustomSerialization`](AnyLogicCustomSerialization.md "annotation interface in com.anylogic.engine") annotation< |
| [AnyLogicInternalAPI](AnyLogicInternalAPI.md "annotation interface in com.anylogic.engine") | Classes, methods and fields marked with this annotation should not be called by user  These members are invoked by engine internals and are public only due to restrictions of java language (inter-package visibility, interface members etc.)  This annotation is used only inside the Engine for development purposes    Methods and fiend annotated using this annotation may have names ending with `"_xjal"` suffix as well |
| [AnyLogicInternalCodegenAPI](AnyLogicInternalCodegenAPI.md "annotation interface in com.anylogic.engine") | Classes, methods and fields marked with this annotation should not be called by user  These members are usually invoked by automatically generated code  This annotation is used only inside the Engine for development purposes    Methods and fiend annotated using this annotation may have names ending with `"_xjal"` suffix as well |
| [AnyLogicInternalLibraryAPI](AnyLogicInternalLibraryAPI.md "annotation interface in com.anylogic.engine") | Classes, methods and fields marked with this annotation should not be called by user  These members are invoked by engine internals and are public only due to restrictions of java language (inter-package visibility, interface members etc.)  This annotation is used only inside the Engine for development purposes    Methods and fiend annotated using this annotation may have names ending with `"_xjal"` suffix as well |
| [AnyLogicLegacyAPI](AnyLogicLegacyAPI.md "annotation interface in com.anylogic.engine") | Classes, methods and fields marked with this annotation are from old versions of AnyLogic, they are supported and may be called by user. |
| [AnyLogicRuntimePreferences](AnyLogicRuntimePreferences.md "class in com.anylogic.engine") | **This class is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| [Area2D](Area2D.md "interface in com.anylogic.engine") | This interface represents some rectangular area. |
| [Area3D](Area3D.md "interface in com.anylogic.engine") | This interface represents some rectangular area. |
| [AreaUnits](AreaUnits.md "enum class in com.anylogic.engine") | Standard AnyLogic area units, should be used in specific functions and parameters which work with units. |
| [ArrivalCallback](ArrivalCallback.md "interface in com.anylogic.engine") |  |
| [AutotestExperimentHost](AutotestExperimentHost.md "class in com.anylogic.engine") |  |
| [CellDirection](CellDirection.md "enum class in com.anylogic.engine") | Constants for directions in discrete space |
| [CellPosition](CellPosition.md "class in com.anylogic.engine") | A simple pair of integers: `r` (row) and `c` (column) |
| [CustomDistributionAbstract](CustomDistributionAbstract.md "class in com.anylogic.engine")<E> | This abstract class is used to generate random numbers from a probability density function (PDF) that is defined by the user. |
| [CustomDistributionContinuous](CustomDistributionContinuous.md "class in com.anylogic.engine") | This class is used to generate random numbers from a probability density function (PDF) defined as: - piecewise linear function. |
| [CustomDistributionDiscrete](CustomDistributionDiscrete.md "class in com.anylogic.engine") | This class is used to generate random numbers from a probability density function (PDF) defined as a set of values of any type with corresponding rates. |
| [CustomDistributionOptions](CustomDistributionOptions.md "class in com.anylogic.engine")<E extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<?>> | This class is used to generate random enum values from a probability density function (PDF) defined as a set of values of any type with corresponding rates. |
| [Dimension](Dimension.md "class in com.anylogic.engine") | A dimension of a HyperArray - a set of non-negative integers (or identifiers mapped to non-negative integers) that are used as indexes in hyper arrays. |
| [DynamicEvent](DynamicEvent.md "class in com.anylogic.engine") | This class is a base class for dynamic events created by the user. |
| [Engine](Engine.md "class in com.anylogic.engine") | The simulation engine that drives the model execution. |
| [Engine.EventSelectionMode](Engine.EventSelectionMode.md "enum class in com.anylogic.engine") | Simultaneous event selection mode constants |
| [Engine.ModelType](Engine.ModelType.md "enum class in com.anylogic.engine") | The type of the model, returned by Engine. |
| [Engine.SolverDAEType](Engine.SolverDAEType.md "enum class in com.anylogic.engine") | The solver type for mixed differential-algebraic equations |
| [Engine.SolverNAEType](Engine.SolverNAEType.md "enum class in com.anylogic.engine") | The solver type for algebraic equations |
| [Engine.SolverODEType](Engine.SolverODEType.md "enum class in com.anylogic.engine") | The solver type for ordinary differential equations |
| [Engine.State](Engine.State.md "enum class in com.anylogic.engine") | The state of the Engine |
| [Environment](Environment.md "class in com.anylogic.engine") | Deprecated. this class only stores constants, for compatibility and may be removed in future |
| [EnvironmentConstants](EnvironmentConstants.md "interface in com.anylogic.engine") |  |
| [Event](Event.md "class in com.anylogic.engine") | Base class for all kinds of (static) events: EventTimeout, EventRate and EventCondition.  **Memory**: sizeof(EventOriginator) = 22 bytes |
| [EventCondition](EventCondition.md "class in com.anylogic.engine") | Event with trigger of type condition. |
| [EventOriginator](EventOriginator.md "class in com.anylogic.engine") | Base class for all constructs in AnyLogic modeling language that are able to schedule discrete events, like Event, DynamicEvent and Transition.  **Memory**: sizeof(Object) + 8 bytes = 22 bytes |
| [EventProfiler](EventProfiler.md "class in com.anylogic.engine") |  |
| [EventProfiler.EventType](EventProfiler.EventType.md "enum class in com.anylogic.engine") |  |
| [EventRate](EventRate.md "class in com.anylogic.engine") | Event with trigger of type rate. |
| [EventTimeout](EventTimeout.md "class in com.anylogic.engine") | Event with trigger of type timeout. |
| [EventTimeout.Mode](EventTimeout.Mode.md "enum class in com.anylogic.engine") |  |
| [Experiment](Experiment.md "class in com.anylogic.engine")<ROOT extends [Agent](Agent.md "class in com.anylogic.engine")> | A base class for all AnyLogic experiments. |
| [Experiment.Command](Experiment.Command.md "enum class in com.anylogic.engine") |  |
| [Experiment.State](Experiment.State.md "enum class in com.anylogic.engine") | The state of the Engine |
| [ExperimentCompareRuns](ExperimentCompareRuns.md "class in com.anylogic.engine")<ROOT extends [Agent](Agent.md "class in com.anylogic.engine")> | Experiment used to run simulation several times with different parameter values set by user before each run.  To use this experiment you need to subclass from it and override method [`Experiment.onEngineFinished()`](Experiment.md#onEngineFinished()). |
| [ExperimentCustom](ExperimentCustom.md "class in com.anylogic.engine") | Base class for all custom experiments  The experiment scenario should be defined in the overridden [`ExperimentCustom.run()`](ExperimentCustom.md#run()) method    Custom experiment may be executed from another experiment - in this case the latter should be passed as an argument to the constructor of the custom experiment. |
| [ExperimentExecutionListener](ExperimentExecutionListener.md "interface in com.anylogic.engine") | **This class is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| [ExperimentMultipleRuns](ExperimentMultipleRuns.md "class in com.anylogic.engine")<ROOT extends [Agent](Agent.md "class in com.anylogic.engine")> | Base class for all experiments that support multiple simulation runs (e.g. |
| [ExperimentMultipleRuns.ConfidenceLevel](ExperimentMultipleRuns.ConfidenceLevel.md "enum class in com.anylogic.engine") | Confidence level constants |
| [ExperimentOptimization](ExperimentOptimization.md "class in com.anylogic.engine")<ROOT extends [Agent](Agent.md "class in com.anylogic.engine")> | Experiment used to search for optimal solutions. |
| [ExperimentParamVariation](ExperimentParamVariation.md "class in com.anylogic.engine")<ROOT extends [Agent](Agent.md "class in com.anylogic.engine")> | Experiment used to run simulation several times with different parameter values. |
| [ExperimentReinforcementLearning](ExperimentReinforcementLearning.md "class in com.anylogic.engine")<ROOT extends [Agent](Agent.md "class in com.anylogic.engine"),O,A,C> | Base class for Reinforcement Learning experiments.    This class serves as an interface between the model and the platform (Learning Platform) using Reinforcement Learning to train some Learning Agent which is based on that platform (e.g. |
| [ExperimentRunFast](ExperimentRunFast.md "class in com.anylogic.engine")<ROOT extends [Agent](Agent.md "class in com.anylogic.engine")> | Base class for all experiments that support fast simulation run (e.g. |
| [ExperimentSimulation](ExperimentSimulation.md "class in com.anylogic.engine")<ROOT extends [Agent](Agent.md "class in com.anylogic.engine")> | The simplest possible experiment consisting of a single simulation run. |
| [ExperimentTest](ExperimentTest.md "class in com.anylogic.engine")<ROOT extends [Agent](Agent.md "class in com.anylogic.engine")> | **This class is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| [ExtAgentContinuous](ExtAgentContinuous.md "interface in com.anylogic.engine") | An extension of agent designed to support agent based modeling in continuous (3D) space, in particular:  - time (continuous or discrete)  - 3D continuous space  - connections between agents, networks (e.g. |
| [ExtAgentContinuousDelegate](ExtAgentContinuousDelegate.md "class in com.anylogic.engine")<E extends [ExtAgentContinuous](ExtAgentContinuous.md "interface in com.anylogic.engine")> | Deprecated. |
| [ExtAgentDiscrete](ExtAgentDiscrete.md "interface in com.anylogic.engine") | An extension of [`Agent`](Agent.md "class in com.anylogic.engine") designed to support agent based modeling in discrete 2D space, in particular:  - time (continuous or discrete)  - 2D discrete space  - connections between agents, networks (e.g. |
| [ExtAgentGIS](ExtAgentGIS.md "interface in com.anylogic.engine") | An extension of Agent designed to support agent based modeling in continuous GIS space, in particular:  - time (continuous or discrete)  - continuous 2D space based on GIS map  - connections between agents, networks (e.g. |
| [ExtAgentInteractive](ExtAgentInteractive.md "interface in com.anylogic.engine") | An extension of [`Agent`](Agent.md "class in com.anylogic.engine") designed to support agent communication, in particular:  - time (continuous or discrete)  - connections between agents, networks (e.g. |
| [ExtAgentWithSpatialMetrics](ExtAgentWithSpatialMetrics.md "interface in com.anylogic.engine") |  |
| [ExtAgentWithSpatialMetricsDelegate](ExtAgentWithSpatialMetricsDelegate.md "class in com.anylogic.engine")<E extends [ExtAgentWithSpatialMetrics](ExtAgentWithSpatialMetrics.md "interface in com.anylogic.engine")> | Base class for extensions delegating their 'Continuous / GIS space agent' activity to an existing extension of agent |
| [ExtAnimationParams](ExtAnimationParams.md "interface in com.anylogic.engine") |  |
| [ExtDefaultAnimationProvider](ExtDefaultAnimationProvider.md "interface in com.anylogic.engine") |  |
| [ExtEntity](ExtEntity.md "interface in com.anylogic.engine") |  |
| [ExtEntityContinuousDelegate](ExtEntityContinuousDelegate.md "class in com.anylogic.engine")<E extends [ExtEntity](ExtEntity.md "interface in com.anylogic.engine")> | Deprecated. |
| [ExtEntityDelegate](ExtEntityDelegate.md "class in com.anylogic.engine")<E extends [ExtEntity](ExtEntity.md "interface in com.anylogic.engine")> | Base class for extensions delegating their 'Entity' activity to an existing extension of agent |
| [ExtEnvironmentContinuous](ExtEnvironmentContinuous.md "interface in com.anylogic.engine") | Agent environment extension for continuous (3D) space |
| [ExtEnvironmentDiscrete](ExtEnvironmentDiscrete.md "interface in com.anylogic.engine") | Agent environment extension for discrete 2D space |
| [ExtEnvironmentGIS](ExtEnvironmentGIS.md "interface in com.anylogic.engine") | Agent space extension for continuous 2D space based on GIS map |
| [ExtEnvironmentInteractive](ExtEnvironmentInteractive.md "interface in com.anylogic.engine") | Extension interface for agent space with communication enabled. |
| [ExtEnvironmentWithLayout](ExtEnvironmentWithLayout.md "interface in com.anylogic.engine") |  |
| [ExtEnvironmentWithMetrics](ExtEnvironmentWithMetrics.md "interface in com.anylogic.engine") |  |
| [ExtRootModelAgent](ExtRootModelAgent.md "interface in com.anylogic.engine") | This extension may be defined only in the top-level agent of the model. |
| [ExtSpace](ExtSpace.md "interface in com.anylogic.engine") | This extension: Tracks moving agents (either straight movement or through network or on the GIS map) Owns animator for agents created dynamically in flowcharts and for agents which jumped from their original space (implemented using replicated embedded object presentation shape) |
| [ExtSpace.SpaceAgentIterable](ExtSpace.SpaceAgentIterable.md "interface in com.anylogic.engine") |  |
| [ExtWithSpaceType](ExtWithSpaceType.md "interface in com.anylogic.engine") | **This interface is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| [FakeExperimentHost](FakeExperimentHost.md "class in com.anylogic.engine") |  |
| [FlowchartActivityType](FlowchartActivityType.md "enum class in com.anylogic.engine") | Type of state the agent may be in when inside some flowchart block. |
| [FlowchartBlock](FlowchartBlock.md "class in com.anylogic.engine") | Base class for all process flowchart blocks in new libraries since AnyLogic 7.  Provides standard functions like [`FlowchartBlock.remove(Agent)`](FlowchartBlock.md#remove(com.anylogic.engine.Agent)). |
| [FlowchartMappedPort](FlowchartMappedPort.md "class in com.anylogic.engine")<InMessageType,OutMessageType> | An implementation of [`FlowchartPort`](FlowchartPort.md "class in com.anylogic.engine") which delegates its [`FlowchartMappedPort.count()`](FlowchartMappedPort.md#count()) and [`FlowchartMappedPort.isError()`](FlowchartMappedPort.md#isError()) methods to another port, this one is mapped with.  Usage: create a custom port of this type and add connector from this port to the port of embedded object (or call [`FlowchartMappedPort.map(Port)`](FlowchartMappedPort.md#map(com.anylogic.engine.Port)) on this port).  There should be one and only one mapped port, otherwise an error will be thrown. |
| [FlowchartPort](FlowchartPort.md "class in com.anylogic.engine")<InMessageType,OutMessageType> | Special Port class for flowchart blocks. |
| [FlowRateUnits](FlowRateUnits.md "enum class in com.anylogic.engine") | Standard AnyLogic flow rate units, should be used in specific functions and parameters which work with units. |
| [HyperArray](HyperArray.md "class in com.anylogic.engine") | A storage for multi-dimensional data used primarily in system dynamics models. |
| [IMaintenanceable](IMaintenanceable.md "interface in com.anylogic.engine") | General parent interface that is implemented by {@link Agent)} AND (transitively) by all markups that offer Downtime functionality. |
| [InspectionWindowColorTheme](InspectionWindowColorTheme.md "enum class in com.anylogic.engine") |  |
| [IPathData](IPathData.md "interface in com.anylogic.engine") |  |
| [IRouteProvider](IRouteProvider.md "interface in com.anylogic.engine")<T extends [IPathData](IPathData.md "interface in com.anylogic.engine")> | This is a base interface to create a route for an agent. |
| [IRunConfiguration](IRunConfiguration.md "interface in com.anylogic.engine")<T extends [Agent](Agent.md "class in com.anylogic.engine")> |  |
| [IRunConfigurationProvider](IRunConfigurationProvider.md "interface in com.anylogic.engine") | **This class is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| [IRunOutputsConsumer](IRunOutputsConsumer.md "interface in com.anylogic.engine") |  |
| [IRunValueAccessor](IRunValueAccessor.md "interface in com.anylogic.engine") |  |
| [IRunValueDescriptor](IRunValueDescriptor.md "interface in com.anylogic.engine")<T> |  |
| [IRunValueDescriptorImpl](IRunValueDescriptorImpl.md "class in com.anylogic.engine")<T> |  |
| [IStatechartState](IStatechartState.md "interface in com.anylogic.engine")<A extends [Agent](Agent.md "class in com.anylogic.engine"),T extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<T> & [IStatechartState](IStatechartState.md "interface in com.anylogic.engine")<A,T>> | Base interface for all statechart state enumerations |
| [IterableWithSize](IterableWithSize.md "interface in com.anylogic.engine")<T> | **This interface is internal and shouldn't be called by user.**  *it may be removed/renamed in future.*   Declares a collection with known size and ability to get element by index. |
| [IUnits](IUnits.md "interface in com.anylogic.engine")<T extends [IUnits](IUnits.md "interface in com.anylogic.engine")<T>> | Base interface for all units enumerations |
| [LayoutType](LayoutType.md "enum class in com.anylogic.engine") | Layout type constants for agent spaces supporting layout |
| [LearningAgentInterface](LearningAgentInterface.md "interface in com.anylogic.engine")<O,A,C> | Data communication interface designed for use with [`ExperimentReinforcementLearning`](ExperimentReinforcementLearning.md "class in com.anylogic.engine"): describes the interaction between the model and Learning Platform / pre-trained Learning Agent |
| [LearningAgentModelInterface](LearningAgentModelInterface.md "interface in com.anylogic.engine")<ROOT extends [Agent](Agent.md "class in com.anylogic.engine")> | Internal interface designed for different usage patterns with Reinforcement Learning |
| [LengthUnits](LengthUnits.md "enum class in com.anylogic.engine") | Standard AnyLogic length units, should be used in specific functions and parameters which work with units. |
| [LibraryEventHandler](LibraryEventHandler.md "class in com.anylogic.engine") | **This class is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| [LibraryEventHandler.Event](LibraryEventHandler.Event.md "class in com.anylogic.engine") |  |
| [LinkToAgent](LinkToAgent.md "interface in com.anylogic.engine")<T extends [Agent](Agent.md "class in com.anylogic.engine"),A extends [Agent](Agent.md "class in com.anylogic.engine")> |  |
| [LinkToAgentAnimationSettings](LinkToAgentAnimationSettings.md "interface in com.anylogic.engine") |  |
| [LinkToAgentAnimationSettingsImpl](LinkToAgentAnimationSettingsImpl.md "class in com.anylogic.engine") |  |
| [LinkToAgentCollection](LinkToAgentCollection.md "interface in com.anylogic.engine")<T extends [Agent](Agent.md "class in com.anylogic.engine"),A extends [Agent](Agent.md "class in com.anylogic.engine")> |  |
| [LinkToAgentCollectionImpl](LinkToAgentCollectionImpl.md "class in com.anylogic.engine")<T extends [Agent](Agent.md "class in com.anylogic.engine"),A extends [Agent](Agent.md "class in com.anylogic.engine")> |  |
| [LinkToAgentImpl](LinkToAgentImpl.md "class in com.anylogic.engine")<T extends [Agent](Agent.md "class in com.anylogic.engine"),A extends [Agent](Agent.md "class in com.anylogic.engine")> |  |
| [LinkToAgentStandardImpl](LinkToAgentStandardImpl.md "class in com.anylogic.engine")<T extends [Agent](Agent.md "class in com.anylogic.engine"),A extends [Agent](Agent.md "class in com.anylogic.engine")> |  |
| [Locatable2D](Locatable2D.md "interface in com.anylogic.engine") | This interface represents some point location. |
| [Locatable3D](Locatable3D.md "interface in com.anylogic.engine") | This interface represents some location. |
| [LRUCache](LRUCache.md "class in com.anylogic.engine")<K,V> |  |
| [MessageDeliveryType](MessageDeliveryType.md "enum class in com.anylogic.engine") | Message destination types for inter-agent communication |
| [MetalOptimization](MetalOptimization.md "class in com.anylogic.engine") |  |
| [ModelException](ModelException.md "class in com.anylogic.engine") |  |
| [ModelProperties](ModelProperties.md "class in com.anylogic.engine") | **This class is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| [ModelPropertyName](ModelPropertyName.md "enum class in com.anylogic.engine") | **This class is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| [NeighborhoodType](NeighborhoodType.md "enum class in com.anylogic.engine") | Types of neighborhood for discrete space |
| [NetworkType](NetworkType.md "enum class in com.anylogic.engine") | Agent network type constants |
| [OptimizationCallback](OptimizationCallback.md "class in com.anylogic.engine") | This class is designed for usage in optimizations performed within custom experiments, see [`ExperimentOptimization.createOptimization(Engine, OptimizationCallback)`](ExperimentOptimization.md#createOptimization(com.anylogic.engine.Engine,com.anylogic.engine.OptimizationCallback)).    **Usage example** (the code of custom experiment, requires `import com.opttek.optquest.*;`): |
| [OptimizationEngine](OptimizationEngine.md "enum class in com.anylogic.engine") |  |
| [OptQuestOptimization](OptQuestOptimization.md "class in com.anylogic.engine") | A wrapper class for COptQuestOptimization. |
| [Pair](Pair.md "class in com.anylogic.engine")<FIRST,SECOND> | A pair of two (possibly `null`) elements, may be used as key in maps.  Overrides [`Pair.equals(Object)`](Pair.md#equals(java.lang.Object)) and [`Pair.hashCode()`](Pair.md#hashCode()).  Objects of this class are immutable: they have no setter methods. |
| [Path2D](Path2D.md "interface in com.anylogic.engine") | This interface represents a sequence of `(x, y)` points  Coordinates of all the points `(Path2D.getPointDx(int), Path2D.getPointDy(int))` are relative to the base coordinates `(Path2D.getX(), Path2D.getY())` |
| [Path3D](Path3D.md "interface in com.anylogic.engine") | This interface represents a sequence of `(x, y, z)` points  Coordinates of all the points `(Path2D.getPointDx(int), Path2D.getPointDy(int), Path3D.getPointDz(int))` are relative to the base coordinates `(Path2D.getX(), Path2D.getY(), Path3D.getZ())` |
| [Point](Point.md "class in com.anylogic.engine") | Class representing Point structure: three coordinates (x, y, z). |
| [Port](Port.md "class in com.anylogic.engine")<InMessageType,OutMessageType> | Port is a universal interface of an agent via which it can send and receive messages - arbitrary objects. |
| [Position](Position.md "class in com.anylogic.engine") | Class representing Point structure three coordinates (x, y, z) with two angles for orientation. |
| [PositionAndScale](PositionAndScale.md "class in com.anylogic.engine") |  |
| [Presentable](Presentable.md "class in com.anylogic.engine") | A base for any object that can be displayed by presentation panel. |
| [ProbabilityDistributionIllegalArgumentException](ProbabilityDistributionIllegalArgumentException.md "class in com.anylogic.engine") |  |
| [ProbabilityDistributionInfiniteLoopException](ProbabilityDistributionInfiniteLoopException.md "class in com.anylogic.engine") |  |
| [RateUnits](RateUnits.md "enum class in com.anylogic.engine") | Standard AnyLogic rate units, should be used in specific functions and parameters which work with units. |
| [ReinforcementLearningDataAccessor](ReinforcementLearningDataAccessor.md "interface in com.anylogic.engine")<ROOT extends [Agent](Agent.md "class in com.anylogic.engine"),O,A,C> |  |
| [ReinforcementLearningModel](ReinforcementLearningModel.md "interface in com.anylogic.engine")<ROOT extends [Agent](Agent.md "class in com.anylogic.engine"),O,A,C> |  |
| [ReinforcementLearningPlatform](ReinforcementLearningPlatform.md "interface in com.anylogic.engine")<ROOT extends [Agent](Agent.md "class in com.anylogic.engine"),O,A,C> |  |
| [RotationSpeedUnits](RotationSpeedUnits.md "enum class in com.anylogic.engine") |  |
| [Scale](Scale.md "class in com.anylogic.engine") |  |
| [Schedule](Schedule.md "class in com.anylogic.engine")<V extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html "class or interface in java.io")> | Schedule class. |
| [ScheduleWithUnits](ScheduleWithUnits.md "class in com.anylogic.engine")<U extends [IUnits](IUnits.md "interface in com.anylogic.engine")<U>> | Schedule with units (Time, Rate etc.). |
| [SDIntegrationManager](SDIntegrationManager.md "class in com.anylogic.engine") | This class solves a system of algebraic differential equations. |
| [SDUtilities](SDUtilities.md "class in com.anylogic.engine") | This class contains functions commonly used in System Dynamic modeling. |
| [Segment2D](Segment2D.md "interface in com.anylogic.engine") | This interface represents a segment: `(x, y) - (x+dx, y+dy)` |
| [Segment3D](Segment3D.md "interface in com.anylogic.engine") | This interface represents a segment: `(x, y, z) - (x+dx, y+dy, z+dz)` |
| [SharedEditorAPI](SharedEditorAPI.md "class in com.anylogic.engine") | **This class is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| [SpaceType](SpaceType.md "enum class in com.anylogic.engine") |  |
| [SpeedUnits](SpeedUnits.md "enum class in com.anylogic.engine") | Standard AnyLogic speed units, should be used in specific functions and parameters which work with units. |
| [Statechart](Statechart.md "class in com.anylogic.engine")<T extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<T> & [IStatechartState](IStatechartState.md "interface in com.anylogic.engine")<?,T>> | Statechart - the most advanced construct to describe event- and time-driven behavior. |
| [TableFunction](TableFunction.md "class in com.anylogic.engine") | Table function enables the user to define functions by giving a number of (argument, value) pairs, i.e. |
| [TableFunction.InterpolationType](TableFunction.InterpolationType.md "enum class in com.anylogic.engine") |  |
| [TableFunction.OutOfRangeAction](TableFunction.OutOfRangeAction.md "enum class in com.anylogic.engine") |  |
| [TableTransferable](TableTransferable.md "class in com.anylogic.engine") | **This class is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* |
| [TaskPreemptionPolicy](TaskPreemptionPolicy.md "enum class in com.anylogic.engine") | TaskPreemptionPolicy |
| [TimeUnits](TimeUnits.md "enum class in com.anylogic.engine") | Standard AnyLogic time units, should be used in specific functions and parameters which work with units. |
| [Transition](Transition.md "class in com.anylogic.engine") | Base class for all kinds of statechart transitions: TransitionTimeout, TransitionRate, TransitionCondition and TransitionMessage  **Memory**: sizeof(EventOriginator) = 22 bytes |
| [TransitionCondition](TransitionCondition.md "class in com.anylogic.engine") | Statechart transition with trigger of type condition. |
| [TransitionMessage](TransitionMessage.md "class in com.anylogic.engine") | Statechart transition with trigger of type message. |
| [TransitionRate](TransitionRate.md "class in com.anylogic.engine") | Statechart transition with trigger of type rate. |
| [TransitionTimeout](TransitionTimeout.md "class in com.anylogic.engine") | Statechart transition with trigger of type timeout. |
| [Utilities](Utilities.md "class in com.anylogic.engine") | This class provides a lot of commonly used functions and constants, including the probability distributions and mathematical functions. |
| [UtilitiesArray](UtilitiesArray.md "class in com.anylogic.engine") | This class provides a lot of commonly used functions for operations with arrays |
| [UtilitiesCollection](UtilitiesCollection.md "class in com.anylogic.engine") | This class provides a lot of commonly used functions for operations with collections / agent populations |
| [UtilitiesCommon](UtilitiesCommon.md "interface in com.anylogic.engine") | Various utilities, e.g. |
| [UtilitiesError](UtilitiesError.md "class in com.anylogic.engine") |  |
| [UtilitiesMath](UtilitiesMath.md "interface in com.anylogic.engine") | Various math utilities |
| [UtilitiesRandom](UtilitiesRandom.md "interface in com.anylogic.engine") | Random number generation utilities for various probability distributions |
| [UtilitiesStream](UtilitiesStream.md "class in com.anylogic.engine") | **This class is internal and shouldn't be called by user.**  *it may be removed/renamed in future.* Please use `UtilitiesCollection` class instead |
| [UtilitiesString](UtilitiesString.md "interface in com.anylogic.engine") | Various string utilities, e.g. |
| [VariableDelay](VariableDelay.md "class in com.anylogic.engine") | *This class is designed for internal use inside AnyLogic code generation, it shouldn't be explicitly accessed by users.*  VariableDelay object accumulates a history of an expression (of type double or HyperArray and generates delayed values of the expression using the accumulated information. |
| [VariableDelay.Type](VariableDelay.Type.md "enum class in com.anylogic.engine") | Type of delay object, see description on items |
