*来源 (Source): <https://anylogic.help/advanced/omniverse/prerequisites.html>*

---

# Omniverse integration: Prerequisites

* [Requirements](#requirements)
* [Connection options](#connection-options)
* [Examples](#examples)
* [Glossary](#glossary)

[Omniverse connector](https://anylogic.help/anylogic/3d/omniverse.html)[Rendering and customization](customization.md)[Connector API](api.md)

NVIDIA Omniverse is a platform that provides integrated, high-quality 3D rendering technologies that can be used to enhance the animation of AnyLogic models. This is achieved by an AnyLogic model connecting to the Omniverse session in real time using a so-called Live workflow.

|  |  |
| --- | --- |
| AnyLogic animation engine | Omniverse |

During runtime, the model sends data using a utility called the AnyLogic Omniverse Connector to modify the state of the scene according to the state changes of objects that have a graphical representation: agents, geometric shapes, and markups.

AnyLogic does not provide ready-made 3D scenes or animations for Omniverse visualization.

To use NVIDIA Kit SDK, it is recommended that you sign up for an Omniverse developer account on the [official website](https://developer.nvidia.com/omniverse#section-getting-started). Alternatively, you can use the registration-free feature branch build [available on GitHub](https://github.com/NVIDIA-Omniverse/kit-app-template). However, note that this is a frequently updated build designed for testing and prototyping only. If you are looking to develop stable solutions, it is advisable to sign up for a developer account anyway.

## Requirements

To run Omniverse, your platform should meet the following requirements:

* At minimum, an **RTX-enabled GPU with 10GB of memory**.
* NVIDIA driver version **537.58** (GameReady, Studio), **537.70** (RTX/Quadro, Grid/vGPU), **576.80** (GameReady, Studio), **573.42** (RTX/Quadro), **576.57** (Grid/vGPU).
  The latest driver version may also work but might not be tested.

Rendering from AnyLogic can be done on any machine that meets the requirements for running AnyLogic animation.

On macOS, support for Omniverse integration is limited. See [Special use cases](customization.md#macos) for more information.

The full technical specifications for running Omniverse can be found on the [official website](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/common/technical-requirements.html).

## Connection options

There are two ways to integrate AnyLogic and Omniverse:

* [**Live session**](live-session.md) — Requires Omniverse launcher (currently deprecated by NVIDIA) or a developer’s account.
* [**Extension**](extension.md) — Uses NVIDIA Kit SDK and a native extension for the platform.

## Examples

To view models that demonstrate various cases of integration between AnyLogic and Omniverse, go to the **Example models** section of the [welcome page](https://anylogic.help/anylogic/ui/welcome-page.html) by selecting **Help** > ![](https://anylogic.help/anylogic/ui/images/toolbars/Open_co.gif) **Example Models** from AnyLogic main menu.
The Omniverse-ready models can be found in the **NVIDIA Omniverse integration** folder, accessible from the left sidebar of the page.
After opening the model, you must follow a few simple steps to connect the model to your Omniverse server. Instructions on how to properly connect the example to Omniverse can be found on the model’s start page.

## Glossary

The following terms are used throughout this documentation:

* **Connector** — The connector is a utility tool used to communicate AnyLogic data to the Omniverse platform.
* **Composer** (also **Create**) — An Omniverse application which is used to assemble, light, simulate, and render 3D scenes in Omniverse.
* **Live session** — An Omniverse term that refers to the active session in which the geometry of the 3D representation is modified in real time.
* **Nucleus** — A collection of Omniverse services used to share and modify the state of the 3D representation.
* **Prim** — Short for “primitive”, the prim is the basic unit of Omniverse. Everything that is imported or created into a USD scene is a prim. This includes, cameras, sounds, lights, meshes, and so on. Technically, a primitive is a container of metadata and properties that can also contain other prims.
* **USD** — Universal Scene Description (USD) is the basic representation for assets in Omniverse.
* **Extension** — The native extension for NVIDIA Kit SDK that facilitates integration between AnyLogic and Omniverse.
