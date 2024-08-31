class Rain_Node:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input_value": ("FLOAT", {
                    "default": 0.5, 
                    "min": 0.0, 
                    "max": 1.0
                }),
                "threshold_value": ("FLOAT", {
                    "default": 0.5, 
                    "min": 0.0, 
                    "max": 1.0
                }),
                "value_if_leq_threshold": ("FLOAT", {
                    "default": 1.0, 
                }),
                "value_if_gt_threshold": ("FLOAT", {
                    "default": 2.0, 
                }),
            },
        }
 
    RETURN_TYPES = ("FLOAT",)  # 返回一个浮点数
    RETURN_NAMES = ("output_value",)
 
    FUNCTION = "test"
 
    CATEGORY = "🐙Rain/📟Logic"
 
    def test(self, input_value, threshold_value, value_if_leq_threshold, value_if_gt_threshold):
        # 判断逻辑：如果输入值 <= 阈值，输出自定义值1；否则输出自定义值2
        if input_value <= threshold_value:
            return (value_if_leq_threshold,)
        else:
            return (value_if_gt_threshold,)
 
 
# 导出节点类的映射字典
NODE_CLASS_MAPPINGS = {
    "Rain_Node": Rain_Node
}
 
# 节点的显示名称映射字典
NODE_DISPLAY_NAME_MAPPINGS = {
    "Rain_Node": "🐙Rain_ValueSwitch"
}