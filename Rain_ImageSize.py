class Rain_ImageSize:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s) -> dict:
        return {
            "required": {
                "image": ("IMAGE",),  # 接收来自 Load Image 节点的图像
            },
        }
 
    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
 
    FUNCTION = "get_image_dimensions"
 
    CATEGORY = "🐙Rain/🗺️Image"
 
    def get_image_dimensions(self, image) -> tuple:
        if not hasattr(image, 'shape'):
            raise ValueError("图像对象不包含 shape 属性")
        
        shape = image.shape
        
        if len(shape) == 4:  # 处理 (batch_size, height, width, channels)
            height, width = shape[1], shape[2]
        else:
            raise ValueError(f"图像的 shape 属性格式不正确，shape: {shape}")
        
        # 打印结果到控制台
        print(f"Image Dimensions - Width: {width}, Height: {height}")
        
        return width, height

# 注册节点
NODE_CLASS_MAPPINGS = {
    "Rain_ImageSize": Rain_ImageSize
}
 
# 设置节点的友好名称
NODE_DISPLAY_NAME_MAPPINGS = {
    "Rain_ImageSize": "🐙Rain_ImageSize"
}