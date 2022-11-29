import os
import re

from core import global_var

output_dir = global_var.output_dir


# 按照格式保存 S参数
# S 参数格式为 [(frequency, (real part, imaginary part)), ------]
# 格式上是一个列表， 每个元素是一个元组，元组内有频率，实部和虚部的信息
# 格式处理后按照 频率 实部 虚部 按行写入文件， 以 space 分割
def save(sPara_data, dir, file_name):
    save_dir = os.path.join(output_dir, dir)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    file_path = os.path.join(save_dir, file_name)
    with open(file_path, mode="a", encoding="utf-8") as f:
        for i in range(len(sPara_data)):
            line = str(sPara_data[i]).replace("(", "").replace(")", "")
            line = line + "\n"
            pattern = re.compile(r"[+-][\d.]+j")
            find_str = str(pattern.findall(line)[0])
            line = re.sub(pattern, " " + find_str, line)
            line = line.replace("j", "").replace(", ", " ")
            f.write(line)


# 保存 AT 所需要的 S参数
# 传入的 AT 的 S参数， 总共八个数据， 保存在一个字典里
# 这一个字典包含两个字典，分别是 Zmax_in 入射 和 Zmin_in 入射，每个入射四个数据，所以总共八个
# 实际上对于 AT 结构来说，一个方向的入射数据就够了，Zmin_in 的数据可以不处理
# Zmin 端口的入射数据已经被注释，不再使用
def save_AT(batch, sParam_AT_data, dir="AT", prefix="", suffix=".txt"):
    save_dir_base = os.path.join(dir, str(batch) + "_batch", "cst", "sParam")

    save_dir_Zmax_in = os.path.join(save_dir_base, "Zmax_in")
    # save_dir_Zmin_in = os.path.join(save_dir_base, "Zmin_in")

    Z = "Zmin2_Zmax1"
    save(sParam_AT_data["Zmax_in"][Z], os.path.join(save_dir_Zmax_in, Z), prefix + "_" + Z + suffix)

    Z = "Zmin1_Zmax1"
    save(sParam_AT_data["Zmax_in"][Z], os.path.join(save_dir_Zmax_in, Z), prefix + "_" + Z + suffix)

    Z = "Zmin2_Zmax2"
    save(sParam_AT_data["Zmax_in"][Z], os.path.join(save_dir_Zmax_in, Z), prefix + "_" + Z + suffix)

    Z = "Zmin1_Zmax2"
    save(sParam_AT_data["Zmax_in"][Z], os.path.join(save_dir_Zmax_in, Z), prefix + "_" + Z + suffix)

    # Z = "Zmax2_Zmin1"
    # save(sParam_AT_data["Zmin_in"][Z], os.path.join(save_dir_Zmin_in, Z), prefix + "_" + Z + suffix)
    #
    # Z = "Zmax1_Zmin1"
    # save(sParam_AT_data["Zmin_in"][Z], os.path.join(save_dir_Zmin_in, Z), prefix + "_" + Z + suffix)
    #
    # Z = "Zmax2_Zmin2"
    # save(sParam_AT_data["Zmin_in"][Z], os.path.join(save_dir_Zmin_in, Z), prefix + "_" + Z + suffix)
    #
    # Z = "Zmax1_Zmin2"
    # save(sParam_AT_data["Zmin_in"][Z], os.path.join(save_dir_Zmin_in, Z), prefix + "_" + Z + suffix)
