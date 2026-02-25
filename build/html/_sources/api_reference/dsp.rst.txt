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

回调方法（子类实现）
^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - 方法
     - 返回值
     - 说明
   * - ``_on_dsp_create(dsp_state)``
     - bool
     - DSP 创建回调
   * - "_on_dsp_process(dsp_state, length, inbuffer, outbuffer, op)"
     - bool
     - DSP 处理回调
   * - "_on_dsp_release(dsp_state)"
     - bool
     - DSP 释放回调

示例
~~~~

创建自定义效果
^^^^^^^^^^^^^^

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
