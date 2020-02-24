import argparse

import torch
import torch.distributed as dist

print(torch.__version__)
print('Support distribute module:', dist.is_available())
