class Rain_IntToFloat:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input_int": ("INT",),  # 定义接收 INT 类型的输入接口
            },
        }
 
    RETURN_TYPES = ("FLOAT",)  # 输出类型定义为 FLOAT
    RETURN_NAMES = ("output_float",)  # 输出接口名称
    FUNCTION = "convert"
    CATEGORY = "🐙Rain/📟Logic"
 
    def convert(self, input_int):
        return (float(input_int),)  # 将输入的 int 值转换为 float 并返回
 
# 导出节点
NODE_CLASS_MAPPINGS = {
    "Rain_IntToFloat": Rain_IntToFloat
}
 
# 定义节点的显示名称
NODE_DISPLAY_NAME_MAPPINGS = {
    "Rain_IntToFloat": "🐙Rain_IntToFloat"
}