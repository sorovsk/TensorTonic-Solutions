#include <cuda_runtime.h>

__global__ void vector_sub(const float* A, const float* B, float* C, int N) {
    // Write code here
    // 计算当前线程的全局索引
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    // 防止超出数组边界
    if (idx < N) {
        C[idx] = A[idx] - B[idx];
    }
}

extern "C" void solve(const float* A, const float* B, float* C, int N) {
    int threads = 256;
    int blocks = (N + threads - 1) / threads;
    vector_sub<<<blocks, threads>>>(A, B, C, N);
    cudaDeviceSynchronize();
}