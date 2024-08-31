class Rain_Math:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "value1": ("FLOAT", {"default": 0.0}),  # 输入的第一个浮点数
                "value2": ("FLOAT", {"default": 0.0}),  # 输入的第二个浮点数
                "operation": (["+", "-", "*", "/", "^", "%", "√", "log", "abs"], {"default": "+"}),  # 运算类型
            },
        }
 
    RETURN_TYPES = ("FLOAT",)  # 返回类型为浮点数
    RETURN_NAMES = ("result",)  # 返回值的名称为result
 
    FUNCTION = "calculate"  # 指定调用的函数为calculate
 
    CATEGORY = "🐙Rain/📟Logic"  # 类别分类
 
    def calculate(self, value1, value2, operation):
        if operation == "+":  # 加法
            result = value1 + value2
        elif operation == "-":  # 减法
            result = value1 - value2
        elif operation == "*":  # 乘法
            result = value1 * value2
        elif operation == "/":  # 除法
            if value2 != 0:
                result = value1 / value2
            else:
                result = float('inf')  # 处理除以零的情况
        elif operation == "^":  # 幂运算
            result = value1 ** value2
        elif operation == "%":  # 取模运算
            result = value1 % value2
        elif operation == "√":  # 平方根
            result = value1 ** 0.5  # 计算 value1 的平方根
        elif operation == "log":  # 对数运算
            import math
            result = math.log(value2, value1)  # 计算以 value1 为底数的 value2 的对数
        elif operation == "abs":  # 绝对值运算
            result = abs(value1)  # 计算 value1 的绝对值
        else:
            result = 0.0  # 默认值，如果操作未被识别
 
        return (result,)
 
 
NODE_CLASS_MAPPINGS = {
    "Rain_Math": Rain_Math  # 将类 Rain_Math 映射为插件中的节点
}
 
NODE_DISPLAY_NAME_MAPPINGS = {
    "Rain_Math": "🐙Rain_Math"  # 定义节点在界面上显示的名称
}