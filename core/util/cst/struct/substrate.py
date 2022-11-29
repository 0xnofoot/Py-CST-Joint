from core.util.cst import modeler


# 创建一个矩形块基板, 该基板以（0,0）坐标为中心
# l: 基板的长度（y方向）
# w: 基板的宽度（x方向）
# t: 基板的厚度（z方向）
# 由于画图时最好与矩阵对应，所以 l和 w 的尺寸最好是偶数
# step: 每一个单位尺寸的步长，用来计算长度，t不参与计算
# 返回：该基板的器件和名字
def brick_sub(mws, material, l, w, th, step, name="brick_sub", component="Substrate"):
    x1 = int(-(w / 2)) * step
    x2 = int(w / 2) * step
    y1 = int(-(l / 2)) * step
    y2 = int(l / 2) * step
    modeler.shape.create_brick(mws, name, material, x1, x2, y1, y2, 0, th, component)

    return component, name
