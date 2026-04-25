术语表
======

  本章节内容参考 FMOD 官方术语表：
  `FMOD Glossary <https://www.fmod.com/docs/2.02/api/glossary.html>`_

  原文档版权归 FMOD 及其相关权利方所有。本文在理解原始术语含义的基础上，结合 Godot 引擎与 Godot-FmodPlayer 的使用场景进行了整理、补充与示例调整

.. _Glossary-2dvs3d:

2D 与 3D
~~~~~~~~

三维 **声源** 是指在空间中具有位置和速度的 :ref:`FmodChannel<FmodChannel>`。当三维 :ref:`FmodChannel<FmodChannel>` 播放时，其音量、扬声器位置和音高会根据与 **听众** 的关系自动调整

**监听器** 通常是玩家或游戏摄像机的位置。他有像 **声源** 一样的位置和速度，但也有方向

3D声音行为：

- **音量** 受 **听者** 与 **声源** 之间的相对距离影响
- **音高** 受 **听者** 与 **声源** 源的相对速度影响（这就产生了多普勒效应）
- **声像** 受 **听者** 与 **声源** 位置相对方向的影响

二维声音行为：

- 三维 **听者** 和 **声源** 的位置、力度和方向被忽略，没有任何影响
- 二维专用功能如 :ref:`FmodChannelControl.set_mix_levels_input()<FmodChannelControl-set_mix_levels_input>`、ChannelControl：：setMixMatrix和ChannelControl：：setPan，将允许手动声像

.. note:: 你可以设置 :ref:`FmodChannelControl<FmodChannelControl>` 中的 ``3d_level`` 在3D混音和2D混音之间进行混合