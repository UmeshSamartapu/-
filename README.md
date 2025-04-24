# ⚡ 𝐒𝐞𝐭𝐭𝐢𝐧𝐠 𝐔𝐩 𝐘𝐨𝐮𝐫 𝐍𝐕𝐈𝐃𝐈𝐀 𝐆𝐏𝐔 𝐟𝐨𝐫 𝐃𝐞𝐞𝐩 𝐋𝐞𝐚𝐫𝐧𝐢𝐧𝐠 – 𝐀 𝐐𝐮𝐢𝐜𝐤 𝐆𝐮𝐢𝐝𝐞

> _If you're diving into deep learning and want to leverage the power of your NVIDIA GPU, here’s a simple step-by-step setup guide to get you up and running!_

---

## 🔹 Step 1: NVIDIA GPU Driver
Install the latest driver for your NVIDIA GPU:  
🔗 [NVIDIA Driver Download](https://lnkd.in/ebzmztiU)

---

## 🔹 Step 2: Visual Studio with C++ Build Tools
Install Visual Studio (Community Edition) with C++ build tools – required for compiling CUDA code:  
🔗 [Download Visual Studio](https://lnkd.in/etiUe8ZR)

---

## 🔹 Step 3: Anaconda / Miniconda
To manage Python environments and install deep learning packages easily:  
🔗 [Download Anaconda](https://lnkd.in/e-nzTmr3)

---

## 🔹 Step 4: CUDA Toolkit
Install the version of CUDA Toolkit that’s compatible with your GPU and PyTorch:  
🔗 [CUDA Toolkit Archive](https://lnkd.in/eV9RZvzY)

---

## 🔹 Step 5: cuDNN Library
Download the cuDNN library to enable GPU acceleration:  
🔗 [cuDNN Archive](https://lnkd.in/ebb39bck)

---

## 🔹 Step 6: Install PyTorch with CUDA Support
Use the PyTorch installation helper to install the correct version for your CUDA setup:  
🔗 [Install PyTorch](https://lnkd.in/e2CbGF_X)

---

## ✅ Final Test – Verify GPU is Detected by PyTorch

### ⚡ Create Virtual Environment:
```bash
conda create -n tv10 python=3.10
conda activate tv10

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
conda install pytorch torchaudio pytorch-cuda -c pytorch -c nvidia

python Test_Torch.py
```

## ✅ Final Test – Verify GPU is Detected by Tensorflow

### ⚡ Create Virtual Environment:
```bash
conda create -n tf10 python=3.10
conda activate tf10

pip install tensorflow==2.10 numpy==1.24.4

python Test_TensorFlow.py
```

