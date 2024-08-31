# 从 Rain_ValueSwitch.py 文件中导入 Rain_ValueSwitch 类
from .Rain_ValueSwitch import Rain_ValueSwitch

# 从 Rain_Math.py 文件中导入 Rain_Math 类
from .Rain_Math import Rain_Math

# 从 Rain_IntToFloat.py 文件中导入 Rain_IntToFloat 类
from .Rain_IntToFloat import Rain_IntToFloat

# 从 Rain_ImageSize.py 文件中导入 Rain_ImageSize 类
from .Rain_ImageSize import Rain_ImageSize

# 定义节点类的映射字典，将类名映射到实际类定义
NODE_CLASS_MAPPINGS = {
    "Rain_ValueSwitch": Rain_ValueSwitch,  # 映射 Rain_ValueSwitch 类
    "Rain_Math": Rain_Math,  # 映射 Rain_Math 类
    "Rain_IntToFloat": Rain_IntToFloat,  # 映射 Rain_IntToFloat 类
    "Rain_ImageSize": Rain_ImageSize  # 映射 Rain_ImageSize 类
}

# 定义节点显示名称的映射字典，将类名映射到界面显示的名称
NODE_DISPLAY_NAME_MAPPINGS = {
    "Rain_ValueSwitch": "🐙Rain_ValueSwitch",  # 界面显示为 "🐙Rain_ValueSwitch"
    "Rain_Math": "🐙Rain_Math",  # 界面显示为 "🐙Rain_Math"
    "Rain_IntToFloat": "🐙Rain_IntToFloat",  # 界面显示为 "🐙Rain_IntToFloat"
    "Rain_ImageSize": "🐙Rain_ImageSize"  # 界面显示为 "🐙Rain_ImageSize"
}

# 导出模块中的所有内容，以便外部引用
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']