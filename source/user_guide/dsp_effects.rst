DSP 效果器
==========

Godot-FmodPlayer 内置 16+ 种专业级 DSP（数字信号处理）效果器，用于实时音频处理。

DSP 类型
--------

效果器列表
~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - 效果器
     - 类型常量
     - 说明
   * - 增益
     - ``DSP_TYPE_AMPLIFY``
     - 简单的音量放大/衰减
   * - 6段均衡器
     - ``DSP_TYPE_EQ6``
     - 6段参数均衡器
   * - 10段均衡器
     - ``DSP_TYPE_EQ10``
     - 10段参数均衡器
   * - 21段均衡器
     - ``DSP_TYPE_EQ21``
     - 21段参数均衡器
   * - 滤波器
     - ``DSP_TYPE_FILTER``
     - 低通/高通/带通/陷波滤波器
   * - 混响
     - ``DSP_TYPE_SFXREVERB``
     - 房间混响效果
   * - 延迟
     - ``DSP_TYPE_DELAY``
     - 回声和延迟线
   * - 合唱
     - ``DSP_TYPE_CHORUS``
     - 立体声合唱效果
   * - 失真
     - ``DSP_TYPE_DISTORTION``
     - 过驱动和失真
   * - 移相器
     - ``DSP_TYPE_PHASER``
     - 相位偏移效果
   * - 音高变换
     - ``DSP_TYPE_PITCHSHIFT``
     - 实时音高变换
   * - 压缩器
     - ``DSP_TYPE_COMPRESSOR``
     - 动态范围压缩
   * - 限制器
     - ``DSP_TYPE_HARDLIMITER``
     - 硬限制器/峰值限制
   * - 声像器
     - ``DSP_TYPE_PANNER``
     - 立体声定位
   * - 立体声增强
     - ``DSP_TYPE_STEREOENHANCE``
     - 立体声宽度控制
   * - 频谱分析器
     - ``DSP_TYPE_SPECTRUMANALYZER``
     - 实时频率分析
   * - 录音
     - ``DSP_TYPE_RECORD``
     - 音频录制到文件

使用 DSP 效果器
---------------

创建 DSP
~~~~~~~~

.. code-block:: gdscript

    func create_dsp():
        var system = FmodServer.main_system
        
        # 通过类型创建 DSP
        var reverb = system.create_dsp_by_type(FmodDSP.DSP_TYPE_SFXREVERB)
        
        # 或通过索引创建
        var delay = system.create_dsp_by_type(FmodDSP.DSP_TYPE_DELAY)

添加到通道或总线
~~~~~~~~~~~~~~~~~~

.. code-block:: gdscript

    func add_effects():
        var system = FmodServer.main_system
        
        # 创建混响
        var reverb = system.create_dsp_by_type(FmodDSP.DSP_TYPE_SFXREVERB)
        
        # 添加到主总线
        var master = system.get_master_channel_group()
        master.add_dsp(0, reverb)  # 索引 0 表示信号链的开头
        
        # 或者添加到特定通道
        var channel = play_some_sound()
        channel.add_dsp(0, reverb)

控制 DSP 参数
~~~~~~~~~~~~~

.. code-block:: gdscript

    func control_dsp(dsp: FmodDSP):
        # 启用/禁用
        dsp.set_active(true)
        
        # 旁通（让信号通过但不处理）
        dsp.set_bypass(false)
        
        # 设置参数（参数索引和值取决于 DSP 类型）
        dsp.set_parameter_float(0, 0.5)   # 浮点参数
        dsp.set_parameter_int(1, 44100)   # 整数参数
        dsp.set_parameter_bool(2, true)   # 布尔参数
        
        # 获取参数
        var value = dsp.get_parameter_float(0)
        
        # 获取参数信息
        var info = dsp.get_parameter_info(0)
        print("Parameter name: %s" % info.name)
        print("Min: %f, Max: %f" % [info.min, info.max])

从通道/总线移除 DSP
~~~~~~~~~~~~~~~~~~

.. code-block:: gdscript

    func remove_dsp():
        var master = FmodServer.main_system.get_master_channel_group()
        var dsp = master.get_dsp(0)  # 获取第一个 DSP
        
        if dsp:
            master.remove_dsp(dsp)
            dsp.release()  # 释放 DSP 资源

常用效果器详解
--------------

混响（Reverb）
~~~~~~~~~~~~~~

.. code-block:: gdscript

    func setup_reverb():
        var system = FmodServer.main_system
        var reverb = system.create_dsp_by_type(FmodDSP.DSP_TYPE_SFXREVERB)
        
        # 参数说明：
        # 0 - Decay Time: 衰减时间（0.0 ~ 20000.0 ms）
        # 1 - Early Delay: 早期反射延迟（0.0 ~ 300.0 ms）
        # 2 - Late Delay: 后期反射延迟（0.0 ~ 100.0 ms）
        # 3 - HF Decay Ratio: 高频衰减比率（0.0 ~ 100.0%）
        # 4 - Diffusion: 扩散度（0.0 ~ 100.0%）
        # 5 - Density: 密度（0.0 ~ 100.0%）
        # 6 - Low Shelf Frequency: 低频架频（20.0 ~ 1000.0 Hz）
        # 7 - Low Shelf Gain: 低频架增益（-36.0 ~ 12.0 dB）
        # 8 - High Cut: 高频截止（1000.0 ~ 20000.0 Hz）
        # 9 - Early Late Mix: 早期/后期混合（0.0 ~ 100.0%）
        # 10 - Wet Level: 湿声电平（-80.0 ~ 20.0 dB）
        # 11 - Dry Level: 干声电平（-80.0 ~ 20.0 dB）
        
        # 小房间设置
        reverb.set_parameter_float(0, 800.0)    # 短衰减
        reverb.set_parameter_float(1, 7.0)      # 短早期延迟
        reverb.set_parameter_float(3, 50.0)     # 中高频衰减
        reverb.set_parameter_float(10, -6.0)    # 适中混响量
        
        var master = system.get_master_channel_group()
        master.add_dsp(0, reverb)

均衡器（EQ）
~~~~~~~~~~~~

.. code-block:: gdscript

    func setup_eq():
        var system = FmodServer.main_system
        var eq = system.create_dsp_by_type(FmodDSP.DSP_TYPE_EQ)
        
        # EQ 参数：
        # 每个频段有 3 个参数：Frequency, Gain, Q
        # 默认支持 3 个频段
        
        # 低频增益
        eq.set_parameter_float(0, 100.0)   # 频率 (Hz)
        eq.set_parameter_float(1, 6.0)     # 增益 (dB)
        eq.set_parameter_float(2, 1.0)     # Q 值
        
        # 中频削减
        eq.set_parameter_float(3, 1000.0)  # 频率
        eq.set_parameter_float(4, -3.0)    # 增益
        eq.set_parameter_float(5, 2.0)     # Q 值
        
        # 高频增益
        eq.set_parameter_float(6, 8000.0)  # 频率
        eq.set_parameter_float(7, 3.0)     # 增益
        eq.set_parameter_float(8, 1.0)     # Q 值
        
        var music_bus = system.get_channel_group_by_name("Music")
        music_bus.add_dsp(0, eq)

滤波器（Filter）
~~~~~~~~~~~~~~~~

.. code-block:: gdscript

    func setup_filter():
        var system = FmodServer.main_system
        var filter = system.create_dsp_by_type(FmodDSP.DSP_TYPE_FILTER)
        
        # 参数：
        # 0 - Type: 0=低通, 1=高通, 2=带通, 3=陷波
        # 1 - Frequency: 截止频率 (1.0 ~ 22000.0 Hz)
        # 2 - Q: 共振 (0.0 ~ 100.0)
        
        # 低通滤波器（水下效果）
        filter.set_parameter_int(0, 0)        # 低通
        filter.set_parameter_float(1, 400.0)  # 400Hz 截止
        filter.set_parameter_float(2, 1.0)    # 低共振
        
        # 或者高通滤波器（电话效果）
        # filter.set_parameter_int(0, 1)        # 高通
        # filter.set_parameter_float(1, 800.0)  # 800Hz 截止

延迟（Delay）
~~~~~~~~~~~~~

.. code-block:: gdscript

    func setup_delay():
        var system = FmodServer.main_system
        var delay = system.create_dsp_by_type(FmodDSP.DSP_TYPE_DELAY)
        
        # 参数：
        # 0 - Delay: 延迟时间（0.0 ~ 10000.0 ms）
        # 1 - Feedback: 反馈量（0.0 ~ 100.0%）
        # 2 - Mix: 干湿比（0.0 ~ 100.0%）
        
        # 回声效果
        delay.set_parameter_float(0, 375.0)   # 375ms 延迟
        delay.set_parameter_float(1, 40.0)    # 40% 反馈
        delay.set_parameter_float(2, 50.0)    # 50% 混音

失真（Distortion）
~~~~~~~~~~~~~~~~~~

.. code-block:: gdscript

    func setup_distortion():
        var system = FmodServer.main_system
        var distortion = system.create_dsp_by_type(FmodDSP.DSP_TYPE_DISTORTION)
        
        # 参数：
        # 0 - Level: 失真程度（0.0 ~ 1.0）
        
        distortion.set_parameter_float(0, 0.3)  # 轻度失真

音高变换（Pitch Shift）
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: gdscript

    func setup_pitch_shift():
        var system = FmodServer.main_system
        var pitch = system.create_dsp_by_type(FmodDSP.DSP_TYPE_PITCHSHIFT)
        
        # 参数：
        # 0 - Pitch: 音高（0.5 = 降八度, 1.0 = 正常, 2.0 = 升八度）
        # 1 - FFT Size: FFT 大小（256, 512, 1024, 2048, 4096）
        # 2 - Max Channels: 最大通道数
        
        # 升调（Chipmunk 效果）
        pitch.set_parameter_float(0, 1.5)
        
        # 降调
        # pitch.set_parameter_float(0, 0.75)

频谱分析器（Spectrum Analyzer）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: gdscript

    extends Node

    var spectrum_dsp: FmodDSP
    var spectrum_data: Array[float] = []

    func _ready():
        var system = FmodServer.main_system
        spectrum_dsp = system.create_dsp_by_type(FmodDSP.DSP_TYPE_SPECTRUMANALYZER)
        
        # 参数：
        # 0 - Window Type: 窗口类型（0=矩形, 1=三角, 2=汉明, 3=汉宁, 4=布莱克曼）
        # 1 - Window Size: 窗口大小（必须 >= 64 且是 2 的幂）
        
        spectrum_dsp.set_parameter_int(0, 3)   # 汉宁窗
        spectrum_dsp.set_parameter_int(1, 1024) # 1024 点 FFT
        
        var master = system.get_master_channel_group()
        master.add_dsp(0, spectrum_dsp)

    func _process(delta):
        # 获取频谱数据
        var data = spectrum_dsp.get_parameter_data(0)
        # data 包含各频段的幅度值

效果器路由
----------

串联连接
~~~~~~~~

信号依次通过多个效果器：

.. code-block:: gdscript

    func chain_effects():
        var system = FmodServer.main_system
        var bus = system.get_master_channel_group()
        
        # 信号流向：输入 -> EQ -> Reverb -> 输出
        var eq = system.create_dsp_by_type(FmodDSP.DSP_TYPE_EQ)
        var reverb = system.create_dsp_by_type(FmodDSP.DSP_TYPE_SFXREVERB)
        
        bus.add_dsp(0, eq)
        bus.add_dsp(1, reverb)  # 在 EQ 之后

并联连接
~~~~~~~~

使用 DSP 连接创建并行处理：

.. code-block:: gdscript

    func parallel_effects():
        var system = FmodServer.main_system
        
        # 创建混音总线
        var wet_bus = system.create_channel_group("Wet")
        var master = system.get_master_channel_group()
        master.add_group(wet_bus)
        
        # 干声直接到主总线
        # 湿声经过混响后到主总线
        var reverb = system.create_dsp_by_type(FmodDSP.DSP_TYPE_SFXREVERB)
        wet_bus.add_dsp(0, reverb)
        
        # 调整干湿比
        wet_bus.set_volume_db(-6.0)  # 湿声稍小

动态效果器管理
--------------

效果器预设
~~~~~~~~~~

.. code-block:: gdscript

    class_name ReverbPreset
    extends RefCounted

    const SMALL_ROOM = {
        "decay": 800.0,
        "early_delay": 7.0,
        "late_delay": 11.0,
        "hf_decay": 83.0,
        "diffusion": 100.0,
        "density": 100.0,
        "wet_level": -6.0
    }

    const LARGE_HALL = {
        "decay": 4000.0,
        "early_delay": 20.0,
        "late_delay": 30.0,
        "hf_decay": 59.0,
        "diffusion": 100.0,
        "density": 100.0,
        "wet_level": -3.0
    }

    static func apply(dsp: FmodDSP, preset: Dictionary):
        dsp.set_parameter_float(0, preset["decay"])
        dsp.set_parameter_float(1, preset["early_delay"])
        dsp.set_parameter_float(2, preset["late_delay"])
        dsp.set_parameter_float(3, preset["hf_decay"])
        dsp.set_parameter_float(4, preset["diffusion"])
        dsp.set_parameter_float(5, preset["density"])
        dsp.set_parameter_float(10, preset["wet_level"])

运行时切换效果
~~~~~~~~~~~~~~

.. code-block:: gdscript

    func switch_effect_area(area_name: String):
        var system = FmodServer.main_system
        var reverb = get_current_reverb_dsp()
        
        match area_name:
            "small_room":
                ReverbPreset.apply(reverb, ReverbPreset.SMALL_ROOM)
            "cave":
                ReverbPreset.apply(reverb, ReverbPreset.LARGE_HALL)
            "outdoor":
                reverb.set_active(false)  # 户外无混响

性能考虑
--------

#. **DSP 消耗 CPU** - 每个激活的 DSP 都会增加 CPU 负担
#. **使用旁通而非移除** - 临时禁用效果时使用 ``set_bypass(true)`` 比频繁添加/移除更高效
#. **注意 FFT 大小** - 音高变换和频谱分析器的 FFT 大小影响延迟和 CPU 使用
#. **复用 DSP** - 相同设置的效果器可以在多个通道间复用

最佳实践
--------

#. **效果顺序** - EQ -> 动态处理（压缩器）-> 空间效果（混响）
#. **总线效果** - 将混响等效果放在总线上，多个通道共享
#. **参数平滑** - 避免每帧大幅改变 DSP 参数，使用插值
#. **资源管理** - 场景切换时记得释放不再使用的 DSP
