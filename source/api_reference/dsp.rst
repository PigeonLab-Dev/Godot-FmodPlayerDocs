DSP 效果器 API
==============

FmodDSP
-------

继承自：RefCounted

FMOD::DSP 的包装类，代表数字信号处理器。

方法
~~~~

生命周期
^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``setup(dsp)``
     - void
     - 设置内部 FMOD DSP
   * - ``release()``
     - void
     - 释放 DSP 资源
   * - ``set_active(active)``
     - void
     - 设置激活状态
   * - ``get_active()``
     - bool
     - 获取激活状态
   * - ``set_bypass(bypass)``
     - void
     - 设置旁通状态
   * - ``get_bypass()``
     - bool
     - 获取旁通状态

参数控制
^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``set_parameter_float(index, value)``
     - void
     - 设置浮点参数
   * - ``get_parameter_float(index)``
     - float
     - 获取浮点参数
   * - ``set_parameter_int(index, value)``
     - void
     - 设置整数参数
   * - ``get_parameter_int(index)``
     - int
     - 获取整数参数
   * - ``set_parameter_bool(index, value)``
     - void
     - 设置布尔参数
   * - ``get_parameter_bool(index)``
     - bool
     - 获取布尔参数
   * - ``set_parameter_data(index, data)``
     - void
     - 设置数据参数
   * - ``get_parameter_data(index)``
     - Dictionary
     - 获取数据参数
   * - ``get_num_parameters()``
     - int
     - 获取参数数量
   * - ``get_parameter_info(index)``
     - Dictionary
     - 获取参数信息

信息查询
^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``get_type()``
     - int
     - 获取 DSP 类型
   * - ``get_id()``
     - int
     - 获取 DSP ID
   * - ``get_name()``
     - String
     - 获取 DSP 名称

连接路由
^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``add_input(target_dsp)``
     - FmodDSPConnection
     - 添加输入连接
   * - ``disconnect_from(target_dsp)``
     - void
     - 断开连接
   * - ``disconnect_all()```
     - void
     - 断开所有连接
   * - "get_num_inputs()``
     - int
     - 获取输入数量
   * - "get_num_outputs()``
     - int
     - 获取输出数量

常量
~~~~

DSP 类型
^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 常量
     - 值
     - 说明
   * - ``DSP_TYPE_AMPLIFY``
     - 0
     - 增益
   * - ``DSP_TYPE_EQ6``
     - 1
     - 6段均衡器
   * - ``DSP_TYPE_EQ10``
     - 2
     - 10段均衡器
   * - ``DSP_TYPE_EQ21``
     - 3
     - 21段均衡器
   * - ``DSP_TYPE_FILTER``
     - 4
     - 滤波器
   * - ``DSP_TYPE_SFXREVERB``
     - 5
     - 混响
   * - ``DSP_TYPE_DELAY``
     - 6
     - 延迟
   * - ``DSP_TYPE_CHORUS``
     - 7
     - 合唱
   * - ``DSP_TYPE_DISTORTION``
     - 8
     - 失真
   * - ``DSP_TYPE_PHASER``
     - 9
     - 移相器
   * - ``DSP_TYPE_PITCHSHIFT``
     - 10
     - 音高变换
   * - ``DSP_TYPE_COMPRESSOR``
     - 11
     - 压缩器
   * - ``DSP_TYPE_HARDLIMITER``
     - 12
     - 硬限制器
   * - ``DSP_TYPE_PANNER``
     - 13
     - 声像器
   * - ``DSP_TYPE_STEREOENHANCE``
     - 14
     - 立体声增强
   * - ``DSP_TYPE_SPECTRUMANALYZER``
     - 15
     - 频谱分析器
   * - ``DSP_TYPE_RECORD``
     - 16
     - 录音
   * - ``DSP_TYPE_CAPTURE``
     - 17
     - 捕获

FmodDSPConnection
-----------------

继承自：RefCounted

DSP 之间的连接，用于信号路由。

方法
~~~~

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``set_mix(mix)``
     - void
     - 设置混合比例（0.0-1.0）
   * - ``get_mix()``
     - float
     - 获取混合比例
   * - ``set_mix_matrix(matrix)``
     - void
     - 设置混合矩阵
   * - ``get_mix_matrix()``
     - Array
     - 获取混合矩阵

FmodAudioEffect
---------------

继承自：Resource

自定义音频效果的抽象基类。

属性
~~~~

.. list-table::
   :header-rows: 1

   * - 属性
     - 类型
     - 说明
   * - ``bus``
     - FmodChannelGroup
     - 目标总线

方法
~~~~

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``apply_to(bus)``
     - void
     - 应用到总线
   * - ``remove_from_bus()``
     - void
     - 从总线移除
   * - ``create_custom_dsp(system)``
     - FmodDSP
     - 创建自定义 DSP

DSP 回调
^^^^^^^^

FmodDSP 支持通过 Callable 设置各种回调函数，实现自定义 DSP 行为。

**生命周期回调：**

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``set_create_callback(callback)`` / ``get_create_callback()``
     - void / Callable
     - DSP 创建回调
   * - ``set_release_callback(callback)`` / ``get_release_callback()``
     - void / Callable
     - DSP 释放回调
   * - ``set_reset_callback(callback)`` / ``get_reset_callback()``
     - void / Callable
     - DSP 重置回调

**处理回调：**

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``set_read_callback(callback)`` / ``get_read_callback()``
     - void / Callable
     - DSP 读取回调（逐采样处理）
   * - ``set_process_callback(callback)`` / ``get_process_callback()``
     - void / Callable
     - DSP 处理回调（块处理）
   * - ``set_shouldiprocess_callback(callback)`` / ``get_shouldiprocess_callback()``
     - void / Callable
     - 是否需要处理回调
   * - ``set_setposition_callback(callback)`` / ``get_setposition_callback()``
     - void / Callable
     - 设置位置回调

**参数回调：**

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``set_setparam_float_callback(callback)`` / ``get_setparam_float_callback()``
     - void / Callable
     - 设置浮点参数回调
   * - ``set_setparam_int_callback(callback)`` / ``get_setparam_int_callback()``
     - void / Callable
     - 设置整数参数回调
   * - ``set_setparam_bool_callback(callback)`` / ``get_setparam_bool_callback()``
     - void / Callable
     - 设置布尔参数回调
   * - ``set_setparam_data_callback(callback)`` / ``get_setparam_data_callback()``
     - void / Callable
     - 设置数据参数回调
   * - ``set_getparam_float_callback(callback)`` / ``get_getparam_float_callback()``
     - void / Callable
     - 获取浮点参数回调
   * - ``set_getparam_int_callback(callback)`` / ``get_getparam_int_callback()``
     - void / Callable
     - 获取整数参数回调
   * - ``set_getparam_bool_callback(callback)`` / ``get_getparam_bool_callback()``
     - void / Callable
     - 获取布尔参数回调
   * - ``set_getparam_data_callback(callback)`` / ``get_getparam_data_callback()``
     - void / Callable
     - 获取数据参数回调

回调函数签名
^^^^^^^^^^^^

**创建回调：**

.. code-block:: gdscript

    func create_callback() -> int:
        # 返回 FMOD_RESULT 枚举值 (FMOD_OK = 0)
        return 0

**处理回调：**

.. code-block:: gdscript

    func process_callback(length: int, in_buffers: Dictionary, inputs_idle: bool, op: int) -> Dictionary:
        # length: 采样数
        # in_buffers: 输入缓冲区字典 {索引: PackedFloat32Array}
        # inputs_idle: 输入是否空闲
        # op: 处理操作类型 (0=查询, 1=执行)
        
        # 返回字典:
        return {
            "outbuffers": {0: output_array},  # 输出缓冲区
            "outchannels": [channel_count],   # 输出通道数
            "result": 0  # FMOD_RESULT
        }

**读取回调：**

.. code-block:: gdscript

    func read_callback(in_array: PackedFloat32Array, length: int, in_channels: int) -> Dictionary:
        # in_array: 输入音频数据
        # length: 采样数
        # in_channels: 输入通道数
        
        # 处理音频...
        var out_array = PackedFloat32Array()
        out_array.resize(length * in_channels)
        
        for i in range(length * in_channels):
            out_array[i] = in_array[i] * 0.5  # 衰减
        
        return {
            "output": out_array,
            "outchannels": in_channels,
            "result": 0  # FMOD_RESULT
        }

**参数设置回调：**

.. code-block:: gdscript

    func set_param_float_callback(index: int, value: float) -> int:
        # index: 参数索引
        # value: 参数值
        print("设置参数 ", index, " = ", value)
        return 0  # FMOD_OK

**参数获取回调：**

.. code-block:: gdscript

    func get_param_float_callback(index: int) -> Dictionary:
        # index: 参数索引
        return {
            "value": 1.0,       # 参数值
            "valuestr": "1.0",  # 值的字符串表示
            "result": 0         # FMOD_RESULT
        }

示例
~~~~

创建自定义效果（旧方式）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: gdscript

    class_name MyCustomEffect
    extends FmodAudioEffect

    func _on_dsp_create(dsp_state) -> bool:
        # 初始化自定义数据
        return true

    func _on_dsp_process(dsp_state, length, inbuffer, outbuffer, op) -> bool:
        # 处理音频数据
        # inbuffer: 输入音频数据
        # outbuffer: 输出音频数据
        # length: 采样数
        
        for i in range(length):
            outbuffer[i] = inbuffer[i] * 0.5  # 简单衰减
        
        return true

    func _on_dsp_release(dsp_state) -> bool:
        # 清理资源
        return true

    # 使用
    func apply_effect():
        var effect = MyCustomEffect.new()
        var system = FmodServer.main_system
        var master = system.get_master_channel_group()
        effect.apply_to(master)

使用回调创建自定义 DSP（新方式）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: gdscript

    func create_custom_dsp():
        var system = FmodServer.main_system
        
        # 创建自定义 DSP
        var dsp = system.create_dsp("MyCustomDSP")
        
        # 设置创建回调
        dsp.set_create_callback(func() -> int:
            print("DSP 已创建")
            return 0  # FMOD_OK
        )
        
        # 设置处理回调
        dsp.set_process_callback(func(length: int, in_buffers: Dictionary, inputs_idle: bool, op: int) -> Dictionary:
            if op == 0:  # FMOD_DSP_PROCESS_QUERY
                # 返回支持的输出格式
                return {
                    "outchannels": [2],  # 立体声输出
                    "result": 0
                }
            
            # op == 1: FMOD_DSP_PROCESS_PERFORM
            var out_buffers = {}
            
            for i in in_buffers.keys():
                var in_data: PackedFloat32Array = in_buffers[i]
                var out_data = PackedFloat32Array()
                out_data.resize(in_data.size())
                
                # 简单的增益处理
                for j in range(in_data.size()):
                    out_data[j] = in_data[j] * 0.7  # 降低音量
                
                out_buffers[i] = out_data
            
            return {
                "outbuffers": out_buffers,
                "outchannels": [2],
                "result": 0  # FMOD_OK
            }
        )
        
        # 设置释放回调
        dsp.set_release_callback(func() -> int:
            print("DSP 已释放")
            return 0
        )
        
        # 添加到主总线
        var master = system.get_master_channel_group()
        master.add_dsp(0, dsp)

使用读取回调的简单效果器
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: gdscript

    func create_simple_gain_dsp():
        var system = FmodServer.main_system
        var dsp = system.create_dsp("GainDSP")
        
        var gain = 0.5
        
        # 设置读取回调（逐采样处理）
        dsp.set_read_callback(func(in_array: PackedFloat32Array, length: int, in_channels: int) -> Dictionary:
            var out_array = PackedFloat32Array()
            out_array.resize(length * in_channels)
            
            for i in range(length * in_channels):
                out_array[i] = in_array[i] * gain
            
            return {
                "output": out_array,
                "outchannels": in_channels,
                "result": 0
            }
        )
        
        # 设置参数回调以动态调整增益
        dsp.set_setparam_float_callback(func(index: int, value: float) -> int:
            if index == 0:
                gain = value
            return 0
        )
        
        dsp.set_getparam_float_callback(func(index: int) -> Dictionary:
            if index == 0:
                return {"value": gain, "valuestr": str(gain), "result": 0}
            return {"value": 0.0, "valuestr": "0", "result": 0}
        )
        
        return dsp

DSP 参数信息
------------

``get_parameter_info()`` 返回的字典包含：

.. list-table::
   :header-rows: 1

   * - 键
     - 类型
     - 说明
   * - ``name``
     - String
     - 参数名称
   * - "label"
     - String
     - 参数标签
   * - "description"
     - String
     - 参数描述
   * - "type``
     - int
     - 参数类型（0=float, 1=int, 2=bool, 3=data）
   * - "min``
     - float
     - 最小值
   * - "max``
     - float
     - 最大值
   * - "default``
     - float
     - 默认值
