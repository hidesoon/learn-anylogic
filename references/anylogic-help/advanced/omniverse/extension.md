*来源 (Source): <https://anylogic.help/advanced/omniverse/extension.html>*

---

# Omniverse integration: Extension

* [Setting up Omniverse](#setting-up-omniverse)
* [Download the connector plugin](#download)
* [Launching the model](#launching-the-model)

[Omniverse connector](https://anylogic.help/anylogic/3d/omniverse.html)[Omniverse integration - Prerequisites](prerequisites.md)[Connector API](api.md)

Starting from version 8.9.7, AnyLogic enables a direct connection to be made from Omniverse to a running model using a special extension. This article describes how to set up and configure this connection.

## Setting up Omniverse

To set up an Omniverse project

1. Download the NVIDIA Kit SDK from one of the following links:
   > **Windows**: <https://catalog.ngc.nvidia.com/orgs/nvidia/teams/omniverse/resources/kit-sdk-windows>
   > **Linux**: <https://catalog.ngc.nvidia.com/orgs/nvidia/teams/omniverse/resources/kit-sdk-linux>
2. Unzip the package to a folder on your PC.
3. In the folder, launch new-project.bat.
4. When prompted by the installation script, specify the path to your Omniverse project and press Enter:

   ![NVIDIA Kit: New project](https://anylogic.help/advanced/omniverse/images/extension-new-project.png)
5. The project will then be created. Open the command line and navigate to the project folder. Once there, execute the following command:
   > **Windows**: repo.bat template new
   > **Linux**: repo.sh template new
6. If this is the first time you are running the template new tool, you will be prompted to accept the Omniverse license terms. Navigate the controls using the arrow keys on your keyboard and confirm by pressing Enter.
   Follow the subsequent steps and specify the metadata of your project. When asked to select the desired template, select **Kit Base Editor**.
   When prompted to add application layers, decline.
7. When you are finished, run the following command to build the new application:
   > **Windows**: repo.bat build
   > **Linux**: repo.sh build

   A notification will appear informing you of the successful build.
8. To launch the project you have just built, enter the following command:
   > **Windows**: repo.bat launch
   > **Linux**: repo.sh launch

Depending on your configuration, the initial launch may take some time. Once complete, you will see the Omniverse editor application, and your instance will be ready to go.

![NVIDIA Kit: The editor window](https://anylogic.help/advanced/omniverse/images/extension-omniverse-editor.png)

## Download the connector plugin

You can download the connector plugin from the AnyLogic website.

Check the [special online page](https://anylogic.help/omniverse/plugins.html) to check compatibility between the different versions of the plugin and NVIDIA Kit.

> **Windows**:
> <https://files.anylogic.com/anylogic.connector-1.0.2%2Bwx64.r.zip>
>
> **Linux**:
> <https://files.anylogic.com/anylogic.connector-1.0.2%2Blx64.r.zip>

To configure Omniverse Kit to run AnyLogic models

1. In the main menu of the Kit editor, go to **Edit** > **Preferences**.
2. Locate and open the **Rendering** section.
3. Make sure the **Enable Fabric delegate** option is selected. This is required for integration with AnyLogic in this implementation because it uses Fabric technology to enable live streaming in Omniverse.

   More information about Fabric can be found in the [NVIDIA documentation](https://docs.omniverse.nvidia.com/kit/docs/usdrt/latest/docs/fabricsd/intro.html).
4. In the main menu of the Kit editor, go to **Developer** > **Extensions**.
5. Click **Options**.
6. Select **Import Extension** from the drop-down menu.

   ![NVIDIA Kit: Importing an extension](https://anylogic.help/advanced/omniverse/images/extension-import-extension.png)
7. In the subsequent dialog, select the extension you have downloaded from one of the [links above](#download).
8. After importing the extension, switch to the **Third Party** tab in the **Extensions** view of Omniverse Kit and enable the **AnyLogic Connector** extension.

   ![NVIDIA Kit: Enabling the extension](https://anylogic.help/advanced/omniverse/images/extension-enable-extension.png)

   You can also click the extension in the list to enable autoload for it during Kit startup, or you can check the readme file and dependencies.

Now that this has been done, you can use the extension to launch your AnyLogic model in Omniverse.

Before attempting to launch the model, make sure to prepare it in AnyLogic by [rendering it](customization.md#render) and adding the [**Omniverse connector**](https://anylogic.help/anylogic/3d/omniverse.html) element. You may also configure the properties of the 3D elements if desired.

**To enable the extension view**, select **Window** > **AnyLogic Connector** from the main menu of the NVIDIA Kit. Then, you can align the connector view inside the Kit editor as you see fit.

## Launching the model

The extension supports two ways of launching the model: connecting to a running model or importing a standalone executable.

To connect to the running model

1. Open the **AnyLogic Connector** extension.
2. Select the **Connect** tab.
3. Specify the connection parameters:
   * **Host** — The IP address or hostname of the machine where the model is running. It can be localhost.
   * **Port** — The port of the machine where the model is launched, 4566 by default.
   * **Password** — (*Optional*) The password you configured in the Omniverse connector in AnyLogic; see [Customizing the connection](customization.md#connection).
   * Click **Connect**.

That’s it. You are now connected to the running scene, and Kit is rendering the model data in real time. Use the standard AnyLogic engine controls to adjust the execution speed or interact with the built-in model controls to dynamically modify parameters such as the number of transporters or the intensity of pedestrian flow. All changes are immediately reflected in the Kit window.

![NVIDIA Kit: Connected to the running model](https://anylogic.help/advanced/omniverse/images/extension-connected.png)

Click **Disconnect** to stop the real-time rendering at any time.

Apply custom prims, scaling, and coordinate transformations in the properties of AnyLogic elements rather than in Omniverse Kit.

To import a model from a standalone executable

To use this approach, first [export the model to a standalone application](https://anylogic.help/anylogic/running/export-java-application.html). The model must contain an **Omniverse connector** element that does not require a password.

1. Open the **AnyLogic Connector** extension.
2. Select the **Run** tab.
3. Click **Browse** and locate the executable file for the standalone model. Depending on the operating system, it wil be either a BAT or an SH file.
4. Kit will then attempt to connect to the model. If successful, the scene will be displayed in the editor.

   ![NVIDIA Kit: Running a standalone model](https://anylogic.help/advanced/omniverse/images/extension-run-standalone.png)

   To launch and control the scene, use the controls available at the bottom of the extension view:
   * ![](https://anylogic.help/advanced/omniverse/images/icons/run-pause.gif) — Starts or pauses the execution.
   * ![](https://anylogic.help/advanced/omniverse/images/icons/default-speed.gif) — Sets the model execution to its default speed.
   * ![](https://anylogic.help/advanced/omniverse/images/icons/slow-down.gif) — Decreases the execution speed.
   * ![](https://anylogic.help/advanced/omniverse/images/icons/speed-up.gif) — Increases the execution speed.
5. When finished your work, click **Terminate** to disconnect the model from Omniverse and stop the rendering.
