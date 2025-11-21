from huggingface_hub import snapshot_download
import os

# --- 参数配置 ---

# 1. 你的仓库 ID
repo_id = "sii-geai-lab/ESOT500"

# 2. 你想下载的仓库内文件夹的路径
path_in_repo = "ESOT500-L/anno_t"

# 3. 你想保存到本地的文件夹路径 (脚本会自动创建这个文件夹)
local_dir = "./ESOT500-L-test-annot"

# --- 执行下载 ---

print(f"开始从仓库 '{repo_id}' 下载文件夹 '{path_in_repo}'...")
print(f"文件将被保存到本地路径: '{os.path.abspath(local_dir)}'")

# 使用 snapshot_download 函数进行下载
# - repo_type="dataset" 必须指定，因为这个仓库是数据集类型
# - allow_patterns 允许我们使用通配符来指定下载内容
#   "ESOT500-L/anno_t/*" 的意思就是下载这个文件夹下的所有文件和子文件夹
snapshot_download(
    repo_id=repo_id,
    repo_type="dataset",
    allow_patterns=f"{path_in_repo}/*",
    local_dir=local_dir,
    local_dir_use_symlinks=False # 建议设为False，直接下载文件而不是链接
)

print("\n下载完成！")
