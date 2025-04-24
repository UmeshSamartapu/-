import torch

print("Number of GPU: ", torch.cuda.device_count())

if torch.cuda.is_available():
    print("GPU Name: ", torch.cuda.get_device_name())
else:
    print("No GPU available or CUDA not enabled")

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('Using device:', device)
