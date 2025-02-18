# GPU适配的学习方向

## **🟢 1. GPU 硬件架构基础**

> 了解 GPU **如何处理并行计算**，以及与 CPU 的区别。

**学习内容：**

- GPU 和 CPU 的区别
- NVIDIA GPU 架构（SM、CUDA Core、Tensor Core）
- GPU 显存（HBM, GDDR）
- **PCIe 带宽** 与 NVLink

**推荐学习资源：**

- 📚 《GPU Gems》系列
- 📚 **NVIDIA 官网** (https://developer.nvidia.com/gpu-architecture)
- 📺 **YouTube 视频** 搜索 "NVIDIA GPU architecture"

------



## **🟡 2. CUDA 基础**

> **CUDA 是 NVIDIA GPU 的编程模型**，用于加速计算。

**学习内容：**

- CUDA 线程模型（Grid、Block、Thread）
- **显存管理**（Global、Shared、Constant Memory）
- **CUDA 核函数**（Kernel）编写
- CUDA 计算优化

**推荐学习资源：**

- 📚 《CUDA Programming: A Developer’s Guide》
- 📚 **NVIDIA CUDA 教程** (https://developer.nvidia.com/cuda-zone)
- 📺 **CUDA 公开课** (https://courses.nvidia.com/)

**实践：**

- **安装 CUDA** 并运行 `deviceQuery` 测试 GPU
- 编写 CUDA 代码加速矩阵计算 (`cudaMalloc`, `cudaMemcpy`)

------



## **🟠 3. GPU 驱动与容器化**

> **驱动决定 GPU 是否能正常运行**，在 Docker 或 K8S 中，需要正确适配驱动。

**学习内容：**

- NVIDIA **驱动安装** (`nvidia-smi` 版本检查)
- **NVIDIA Container Toolkit** (Docker 运行 GPU 容器)
- **NVIDIA MIG (Multi-Instance GPU)** —— 多任务共享 GPU

**推荐学习资源：**

- 📚 **NVIDIA 官方文档** (https://docs.nvidia.com/datacenter/)
- 📺 **Docker & GPU 加速** (https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/)

**实践：**

- 安装驱动 (`sudo apt install nvidia-driver-525`)
- `nvidia-smi` 检查 GPU 运行状态
- 运行 `docker run --gpus all nvidia/cuda:12.2-base nvidia-smi`

------



## **🔵 4. 深度学习框架的 GPU 加速**

> **理解 PyTorch、TensorFlow 如何调用 GPU，优化 AI 训练速度**

**学习内容：**

- **GPU 加速的 Tensor 运算** (`torch.cuda()`, `tf.device()`)
- **Mixed Precision 训练**（`torch.cuda.amp` / TensorRT）
- **多 GPU 训练（DDP）**
- **优化显存管理 (`torch.backends.cudnn.benchmark`)**

**推荐学习资源：**

- 📚 **PyTorch CUDA 官方文档** (https://pytorch.org/docs/stable/notes/cuda.html)
- 📚 **TensorFlow GPU 指南** (https://www.tensorflow.org/guide/gpu)
- 📺 **FastAI 公开课**

**实践：**

- 运行 `torch.cuda.is_available()`
- 训练 MNIST CNN 用 `torch.cuda.amp` 加速
- 配置 **NVIDIA Apex** 进行混合精度训练

------



## **🟣 5. GPU 适配 Kubernetes（K8S）**

> **在 K8S 上管理 GPU 资源，实现 AI 任务调度**

**学习内容：**

- **NVIDIA K8S GPU Operator**（自动管理 GPU 资源）
- **K8S 多租户 GPU 共享**（MIG）
- **GPU 监控 (`nvidia-dcgm-exporter`)**

**推荐学习资源：**

- 📚 **K8S GPU Operator 文档** (https://github.com/NVIDIA/gpu-operator)
- 📚 **K8S 计算资源管理** (https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/)

**实践：**

- 在 K8S 部署 `NVIDIA GPU Operator`
- 运行 `kubectl get pods -o wide` 查看 GPU 资源使用

------



## **🚀 总结：如何系统学习？**

1. **硬件基础** —— 理解 **NVIDIA GPU 架构**
2. **CUDA 编程** —— 学习 **线程、显存、核函数**
3. **驱动与 Docker** —— 适配 **NVIDIA Container Toolkit**
4. **深度学习优化** —— 研究 **AMP / TensorRT**
5. **K8S GPU 管理** —— 在 **Kubernetes 上运行 AI**

------

### **🔹 推荐实践**

| 任务                  | 学习内容          | 关键命令                             |
| --------------------- | ----------------- | ------------------------------------ |
| **检查 GPU 运行状态** | `nvidia-smi`      | `nvidia-smi`                         |
| **CUDA 开发**         | 编写 Kernel       | `nvcc -o kernel kernel.cu`           |
| **PyTorch 训练**      | Tensor 运算       | `torch.cuda.is_available()`          |
| **K8S 适配 GPU**      | 运行 GPU Operator | `kubectl apply -f gpu-operator.yaml` |

------

如果你的目标是 **适配 AI 训练任务**，建议从 **CUDA + TensorRT** 开始；如果是 **K8S GPU 资源管理**，可以深入 **NVIDIA GPU Operator** 🚀。