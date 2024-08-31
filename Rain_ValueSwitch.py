# 定义一个类 Rain_ValueSwitch，这个类代表了一个逻辑节点，用于根据输入值和阈值来选择输出不同的值。
class Rain_ValueSwitch:
    def __init__(self):
        pass  # 初始化方法，当前未做任何操作，可以根据需要添加属性或初始化逻辑
    
    # 定义输入类型和范围，返回一个字典，用于指定节点的输入配置
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                # 输入值，类型为浮点数，默认值为 0.5，范围从 0.0 到 1.0
                "input_value": ("FLOAT", {
                    "default": 0.5, 
                    "min": 0.0, 
                    "max": 1.0
                }),
                # 阈值，类型为浮点数，默认值为 0.5，范围从 0.0 到 1.0
                "threshold_value": ("FLOAT", {
                    "default": 0.5, 
                    "min": 0.0, 
                    "max": 1.0
                }),
                # 如果输入值小于等于阈值，输出此自定义值，默认值为 1.0
                "value_if_leq_threshold": ("FLOAT", {
                    "default": 1.0, 
                }),
                # 如果输入值大于阈值，输出此自定义值，默认值为 2.0
                "value_if_gt_threshold": ("FLOAT", {
                    "default": 2.0, 
                }),
            },
        }
 
    # 定义返回类型，这里是一个浮点数
    RETURN_TYPES = ("FLOAT",)
    # 定义返回值的名称，在调用时可以更方便识别输出
    RETURN_NAMES = ("output_value",)
    # 指定要调用的函数名称，在此类中定义的函数，用于实现具体逻辑
    FUNCTION = "switch_value"
    # 指定插件在 UI 中的分类路径，方便查找
    CATEGORY = "🐙Rain/📟Logic"
 
    # 实现具体的逻辑：判断输入值是否小于等于阈值，并根据结果返回相应的自定义值
    def switch_value(self, input_value, threshold_value, value_if_leq_threshold, value_if_gt_threshold):
        if input_value <= threshold_value:
            # 如果输入值 <= 阈值，返回 value_if_leq_threshold
            return (value_if_leq_threshold,)
        else:
            # 如果输入值 > 阈值，返回 value_if_gt_threshold
            return (value_if_gt_threshold,)
 
 
# 导出节点类的映射字典，将节点类名映射到类定义，供外部调用
NODE_CLASS_MAPPINGS = {
    "Rain_ValueSwitch": Rain_ValueSwitch
}
 
# 节点的显示名称映射字典，将内部类名映射到 UI 上显示的名称
NODE_DISPLAY_NAME_MAPPINGS = {
    "Rain_ValueSwitch": "🐙Rain_ValueSwitch"
}