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
        
        # Create a DSP by type.
        var reverb = system.create_dsp_by_type(FmodDSP.DSP_TYPE_SFXREVERB)
        
        # Or create another DSP by type.
        var delay = system.create_dsp_by_type(FmodDSP.DSP_TYPE_DELAY)

添加到通道或总线
~~~~~~~~~~~~~~~~~~

.. code-block:: gdscript

    func add_effects():
        var system = FmodServer.main_system
        
        # Create a reverb DSP.
        var reverb = system.create_dsp_by_type(FmodDSP.DSP_TYPE_SFXREVERB)
        
        # Add it to the master bus.
        var master = system.get_master_channel_group()
        master.add_dsp(0, reverb)  # Index 0 is the start of the signal chain.
        
        # Or add it to a specific channel.
        var channel = play_some_sound()
        channel.add_dsp(0, reverb)

控制 DSP 参数
~~~~~~~~~~~~~

.. code-block:: gdscript

    func control_dsp(dsp: FmodDSP):
        # Enable or disable.
        dsp.set_active(true)
        
        # Bypass the effect while letting the signal pass through.
        dsp.set_bypass(false)
        
        # Set parameters. Parameter indices and values depend on the DSP type.
        dsp.set_parameter_float(0, 0.5)   # Float parameter
        dsp.set_parameter_int(1, 44100)   # Integer parameter
        dsp.set_parameter_bool(2, true)   # Boolean parameter
        
        # Get a parameter value.
        var value = dsp.get_parameter_float(0)
        
        # Get parameter metadata.
        var info = dsp.get_parameter_info(0)
        print("Parameter name: %s" % info.name)
        print("Min: %f, Max: %f" % [info.min, info.max])

从通道/总线移除 DSP
~~~~~~~~~~~~~~~~~~~~

.. code-block:: gdscript

    func remove_dsp():
        var master = FmodServer.main_system.get_master_channel_group()
        var dsp = master.get_dsp(0)  # Get the first DSP.
        
        if dsp:
            master.remove_dsp(dsp)
            dsp.release()  # Release DSP resources.

常用效果器详解
--------------

混响（Reverb）
~~~~~~~~~~~~~~

.. code-block:: gdscript

    func setup_reverb():
        var system = FmodServer.main_system
        var reverb = system.create_dsp_by_type(FmodDSP.DSP_TYPE_SFXREVERB)
        
        # Parameters:
        # 0 - Decay Time (0.0 ~ 20000.0 ms)
        # 1 - Early Delay (0.0 ~ 300.0 ms)
        # 2 - Late Delay (0.0 ~ 100.0 ms)
        # 3 - HF Decay Ratio (0.0 ~ 100.0%)
        # 4 - Diffusion (0.0 ~ 100.0%)
        # 5 - Density (0.0 ~ 100.0%)
        # 6 - Low Shelf Frequency (20.0 ~ 1000.0 Hz)
        # 7 - Low Shelf Gain (-36.0 ~ 12.0 dB)
        # 8 - High Cut (1000.0 ~ 20000.0 Hz)
        # 9 - Early Late Mix (0.0 ~ 100.0%)
        # 10 - Wet Level (-80.0 ~ 20.0 dB)
        # 11 - Dry Level (-80.0 ~ 20.0 dB)
        
        # Small room settings.
        reverb.set_parameter_float(0, 800.0)    # Short decay
        reverb.set_parameter_float(1, 7.0)      # Short early delay
        reverb.set_parameter_float(3, 50.0)     # Mid/high frequency decay
        reverb.set_parameter_float(10, -6.0)    # Moderate reverb amount
        
        var master = system.get_master_channel_group()
        master.add_dsp(0, reverb)

均衡器（EQ）
~~~~~~~~~~~~

.. code-block:: gdscript

    func setup_eq():
        var system = FmodServer.main_system
        var eq = system.create_dsp_by_type(FmodDSP.DSP_TYPE_EQ)
        
        # EQ parameters:
        # Each band has three parameters: Frequency, Gain, Q.
        # Three bands are supported by default.
        
        # Low frequency boost.
        eq.set_parameter_float(0, 100.0)   # Frequency (Hz)
        eq.set_parameter_float(1, 6.0)     # Gain (dB)
        eq.set_parameter_float(2, 1.0)     # Q value
        
        # Mid frequency cut.
        eq.set_parameter_float(3, 1000.0)  # Frequency
        eq.set_parameter_float(4, -3.0)    # Gain
        eq.set_parameter_float(5, 2.0)     # Q value
        
        # High frequency boost.
        eq.set_parameter_float(6, 8000.0)  # Frequency
        eq.set_parameter_float(7, 3.0)     # Gain
        eq.set_parameter_float(8, 1.0)     # Q value
        
        var music_bus = system.get_channel_group_by_name("Music")
        music_bus.add_dsp(0, eq)

滤波器（Filter）
~~~~~~~~~~~~~~~~

.. code-block:: gdscript

    func setup_filter():
        var system = FmodServer.main_system
        var filter = system.create_dsp_by_type(FmodDSP.DSP_TYPE_FILTER)
        
        # Parameters:
        # 0 - Type: 0=low-pass, 1=high-pass, 2=band-pass, 3=notch
        # 1 - Frequency: cutoff frequency (1.0 ~ 22000.0 Hz)
        # 2 - Q: resonance (0.0 ~ 100.0)
        
        # Low-pass filter for an underwater effect.
        filter.set_parameter_int(0, 0)        # Low-pass
        filter.set_parameter_float(1, 400.0)  # 400 Hz cutoff
        filter.set_parameter_float(2, 1.0)    # Low resonance
        
        # Or use a high-pass filter for a telephone effect.
        # filter.set_parameter_int(0, 1)        # High-pass
        # filter.set_parameter_float(1, 800.0)  # 800 Hz cutoff

延迟（Delay）
~~~~~~~~~~~~~

.. code-block:: gdscript

    func setup_delay():
        var system = FmodServer.main_system
        var delay = system.create_dsp_by_type(FmodDSP.DSP_TYPE_DELAY)
        
        # Parameters:
        # 0 - Delay: delay time (0.0 ~ 10000.0 ms)
        # 1 - Feedback: feedback amount (0.0 ~ 100.0%)
        # 2 - Mix: dry/wet mix (0.0 ~ 100.0%)
        
        # Echo effect.
        delay.set_parameter_float(0, 375.0)   # 375 ms delay
        delay.set_parameter_float(1, 40.0)    # 40% feedback
        delay.set_parameter_float(2, 50.0)    # 50% mix

失真（Distortion）
~~~~~~~~~~~~~~~~~~

.. code-block:: gdscript

    func setup_distortion():
        var system = FmodServer.main_system
        var distortion = system.create_dsp_by_type(FmodDSP.DSP_TYPE_DISTORTION)
        
        # Parameters:
        # 0 - Level: distortion amount (0.0 ~ 1.0)
        
        distortion.set_parameter_float(0, 0.3)  # Light distortion

音高变换（Pitch Shift）
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: gdscript

    func setup_pitch_shift():
        var system = FmodServer.main_system
        var pitch = system.create_dsp_by_type(FmodDSP.DSP_TYPE_PITCHSHIFT)
        
        # Parameters:
        # 0 - Pitch: 0.5=one octave down, 1.0=normal, 2.0=one octave up
        # 1 - FFT Size: 256, 512, 1024, 2048, 4096
        # 2 - Max Channels
        
        # Pitch up for a chipmunk effect.
        pitch.set_parameter_float(0, 1.5)
        
        # Pitch down.
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
        
        # Parameters:
        # 0 - Window Type: 0=rectangular, 1=triangle, 2=Hamming, 3=Hanning, 4=Blackman
        # 1 - Window Size: must be >= 64 and a power of two
        
        spectrum_dsp.set_parameter_int(0, 3)   # Hanning window
        spectrum_dsp.set_parameter_int(1, 1024) # 1024-point FFT
        
        var master = system.get_master_channel_group()
        master.add_dsp(0, spectrum_dsp)

    func _process(delta):
        # Get spectrum data.
        var data = spectrum_dsp.get_parameter_data(0)
        # data contains amplitude values for each frequency band.

效果器路由
----------

串联连接
~~~~~~~~

信号依次通过多个效果器：

.. code-block:: gdscript

    func chain_effects():
        var system = FmodServer.main_system
        var bus = system.get_master_channel_group()
        
        # Signal flow: input -> EQ -> Reverb -> output.
        var eq = system.create_dsp_by_type(FmodDSP.DSP_TYPE_EQ)
        var reverb = system.create_dsp_by_type(FmodDSP.DSP_TYPE_SFXREVERB)
        
        bus.add_dsp(0, eq)
        bus.add_dsp(1, reverb)  # After the EQ.

并联连接
~~~~~~~~

使用 DSP 连接创建并行处理：

.. code-block:: gdscript

    func parallel_effects():
        var system = FmodServer.main_system
        
        # Create a mix bus.
        var wet_bus = system.create_channel_group("Wet")
        var master = system.get_master_channel_group()
        master.add_group(wet_bus)
        
        # Dry signal goes directly to the master bus.
        # Wet signal goes through reverb before reaching the master bus.
        var reverb = system.create_dsp_by_type(FmodDSP.DSP_TYPE_SFXREVERB)
        wet_bus.add_dsp(0, reverb)
        
        # Adjust the dry/wet balance.
        wet_bus.set_volume_db(-6.0)  # Keep the wet signal slightly lower.

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
                reverb.set_active(false)  # No reverb outdoors.

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
