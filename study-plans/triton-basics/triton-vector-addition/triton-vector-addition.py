import torch
import triton
import triton.language as tl


@triton.jit
def vector_add_kernel(x_ptr, y_ptr, out_ptr, n, BLOCK_SIZE: tl.constexpr):
    # Write code here
    # 获取当前程序（block）的ID
    pid = tl.program_id(axis=0)
    # 计算本block处理的起始索引
    start_idx = pid * BLOCK_SIZE
    # 计算偏移量：0,1,2,...,BLOCK_SIZE-1
    offsets = start_idx + tl.arange(0, BLOCK_SIZE)
    # 创建掩码，防止读取/写入超出数组边界
    mask = offsets < n
    # 加载数据（超出边界的元素用0填充，但掩码会阻止写入）
    x_vals = tl.load(x_ptr + offsets, mask=mask)
    y_vals = tl.load(y_ptr + offsets, mask=mask)
    # 执行加法
    out_vals = x_vals + y_vals
    # 存储结果（只存储掩码为真的位置）
    tl.store(out_ptr + offsets, out_vals, mask=mask)


def solve(x: torch.Tensor, y: torch.Tensor, out: torch.Tensor) -> None:
    """Launch vector_add_kernel on the provided tensors."""
    n = x.numel()
    BLOCK_SIZE = 1024
    grid = ((n + BLOCK_SIZE - 1) // BLOCK_SIZE,)
    vector_add_kernel[grid](x, y, out, n, BLOCK_SIZE=BLOCK_SIZE)