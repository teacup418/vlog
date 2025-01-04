import os

# project_path = input("项目路径")
project_path = "C:\\Users\\Vincent\\Desktop\\test"
dirs = []
d1 = os.path.join(project_path, "1.工程文件")
dirs.append(d1)
d2 = os.path.join(project_path, "2.素材\\origin")
dirs.append(d2)
d3 = os.path.join(project_path, "3.配套")
dirs.append(d3)
for dir in dirs:
    os.makedirs(dir, exist_ok=True)
# try:
# except FileExistsError as fee:
#     pass
