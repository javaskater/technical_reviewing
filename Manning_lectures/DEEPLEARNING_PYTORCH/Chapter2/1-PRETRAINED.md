# 25
* both definitions produce the same output
```python
#resnet = models.resnet101(pretrained=True)
resnet = models.resnet101(weights=models.ResNet101_Weights.DEFAULT)
```
* It is downloading a model (that is the weights)
```bash
Downloading: "https://download.pytorch.org/models/resnet101-cd907fc2.pth" to /root/.cache/torch/hub/checkpoints/resnet101-cd907fc2.pth
100%|██████████| 171M/171M [00:02<00:00, 76.4MB/s]
```
# 28
* What does unsqueeze
```python
>>> import torch
>>> a = [[[1,1], [2,2]], [[3,3], [4,4]]]
>>> b = torch.tensor(a)
>>> b
tensor([[[1, 1],
         [2, 2]],

        [[3, 3],
         [4, 4]]])
>>> c = torch.unsqueeze(b,0)
>>> c
tensor([[[[1, 1],
          [2, 2]],

         [[3, 3],
          [4, 4]]]])
```
* Cela a rajouté une dimension devant les 2 lignes avec un seul élément
* This added dimension is th on element batch !!!
# 29
* Result of the pretrained network
```python
out = resnet(batch_t)
out
print(f"shape of a tensor {out.shape}")
```
* says 1 line (batch-size) of 1000 elements (the 1000 possible labels)
* the calculation in Colab took very little time
# 30
```python
_, index = torch.max(out, 1) #index is a tensor with only one element so we can call its item() function
print(f"found index {index.item()}")
```
* prints 207
* the [link](https://pytorch.org/docs/stable/generated/torch.nn.Softmax.html#torch.nn.Softmax) gives the Softmax definition
  * index[0] is the same thing as index.item() as there is only one element
#  