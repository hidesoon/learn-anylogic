*来源 (Source): <https://anylogic.help/advanced/omniverse/live-session.html>*

---

# Omniverse integration: Live session

* [Viewing a scene in a Composer session](#viewing-a-scene-in-a-composer-session)

[Omniverse connector](https://anylogic.help/anylogic/3d/omniverse.html)[Connector API](api.md)[Prerequisites](prerequisites.md)

To run models in the live session mode, you need the Omniverse [USD Composer](https://docs.omniverse.nvidia.com/composer/latest/overview_external.html) application installed through the Omniverse Launcher. Note that the Omniverse Launcher is currently deprecated and may be available in legacy builds for users who have previously configured the Omniverse integration.

To use the integration, it is recommended that you sign up for an Omniverse developer account on the [official website](https://developer.nvidia.com/omniverse#section-getting-started). Alternatively, you can use the registration-free feature branch build [available on GitHub](https://github.com/NVIDIA-Omniverse/kit-app-template). However, note that this is a frequently updated build designed for testing and prototyping only. If you are looking to develop stable solutions, it is advisable to sign up for a developer account anyway.

Before attempting to launch the model, make sure to prepare it in AnyLogic by [rendering it](customization.md#render) and adding the [**Omniverse connector**](https://anylogic.help/anylogic/3d/omniverse.html) element. You may also configure the properties of the 3D elements if desired.
Apply custom prims, scaling, and coordinate transformations in the properties of AnyLogic elements rather than in Omniverse.

## Viewing a scene in a Composer session

To manually join the live session to view the running model in Composer:

1. Make sure that the model with the connector is open and launched in AnyLogic, even if the model is paused or stopped.
2. Once the model is running, open the scene in Composer. This is not necessary if the automatic startup of Composer has been enabled.
3. In the Omniverse Composer window, expand the **Live** drop-down list and select **Join session**.

   ![](https://anylogic.help/advanced/omniverse/images/live-session-join.png)
4. In the dialog that appears, select the session identified as **AnyLogicLiveSession**. The full name of the session, including the timestamp, is shown in the console view of a running AnyLogic model.
5. Click **Join**.

   ![](https://anylogic.help/advanced/omniverse/images/live-session-join-dialog.png)

Once the USD scene is connected to the model, you will see the live session in the **Layers** tab, and the session participants in the upper right corner.

To end the session, expand the **Live** drop-down list and click **Leave session**.
