class Rain_ValueSwitch:
    def __init__(self):
        pass  # 初始化方法，目前没有特殊初始化逻辑
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_value": ("FLOAT", {"default": 0.5}),
                "threshold_value": ("FLOAT", {"default": 0.5, "min": 0.0, "max": 1.0, "step": 0.01}),
                "value_if_leq_threshold": ("FLOAT", {"default": 1.0}),
                "value_if_gt_threshold": ("FLOAT", {"default": 2.0}),
            },
        }
 
    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("output_value",)
    FUNCTION = "switch_value"
    CATEGORY = "🐙Rain/📟Logic"
 
    def switch_value(self, input_value, threshold_value, value_if_leq_threshold, value_if_gt_threshold):
        # 如果 input_value 是对象并且有 evaluate 方法，则调用 evaluate 获取值
        if hasattr(input_value, 'evaluate') and callable(input_value.evaluate):
            input_value = input_value.evaluate()
        
        # 根据输入值与阈值的比较结果返回相应的值
        return (value_if_leq_threshold if input_value <= threshold_value else value_if_gt_threshold,)
 
NODE_CLASS_MAPPINGS = {
    "Rain_ValueSwitch": Rain_ValueSwitch
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Rain_ValueSwitch": "🐙Rain_ValueSwitch"
}