class Rain_ValueSwitch:
    def __init__(self):
        pass  # 初始化方法，目前没有特殊初始化逻辑
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # input_value 现在是一个节点输入接口，可以链接到其他节点
                "input_value": ("NODE", {"default": None}),
                "threshold_value": ("FLOAT", {"default": 0.5, "min": 0.0, "max": 1.0, "step": 0.01}),
                "value_if_leq_threshold": ("FLOAT", {"default": 1.0}),
                "value_if_gt_threshold": ("FLOAT", {"default": 2.0}),
            },
        }
 
    # 定义返回类型和名称
    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("output_value",)
    # 指定执行的函数和分类
    FUNCTION = "switch_value"
    CATEGORY = "🐙Rain/📟Logic"
 
    def switch_value(self, input_value, threshold_value, value_if_leq_threshold, value_if_gt_threshold):
        # 获取输入节点的输出值
        input_value = input_value.evaluate()  # 假设 input_value 是节点，可以通过 evaluate() 方法获取值
        # 根据输入值与阈值的比较结果返回相应的值
        return (value_if_leq_threshold if input_value <= threshold_value else value_if_gt_threshold,)
 
# 节点类的映射字典
NODE_CLASS_MAPPINGS = {
    "Rain_ValueSwitch": Rain_ValueSwitch
}

# 节点显示名称的映射字典
NODE_DISPLAY_NAME_MAPPINGS = {
    "Rain_ValueSwitch": "🐙Rain_ValueSwitch"
}