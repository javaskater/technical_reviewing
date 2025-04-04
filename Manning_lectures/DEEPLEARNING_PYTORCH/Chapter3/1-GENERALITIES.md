# 47
> For image recognition, early
> representations can be things such as edge detection or certain textures like fur. Deeper
> representations can capture more complex structures like ears, noses, or eyes
# 48/462
* Tensors *keep track of the graph of computations that created them*
  * so we get the CNN from the tensor 
# 49
* [Part 1 Chapter 3 Tensors](https://github.com/deep-learning-with-pytorch/dlwpt-code/blob/master/p1ch3/1_tensors.ipynb)
  * simple part for playing with Tensors
  * note the float() function, it translates from a one element tensor to a Python float
    * *ValueError: only one element tensors can be converted to Python scalars*
* in the tensor like in numpy arrays, the elements are all of the same type
  * so you don't have to have the type info for each element like in list, you have the type info one and for all for the entire tensor.
* and are placed in continuous elements in memory
* For a tensor, the attribute *shape* and the function **size()* give the same result
```python
print(f"Shape: {points.shape} Size: {points.size()}")
```
* Playing with columns
```python
points = torch.tensor([[4.0, 1.0], [5.0, 3.0], [2.0, 1.0]])
points[:, 1] # returns tensor([1., 3., 1.])
points[0] # is the same than points[0, :]
points[1:,0] # transforms the 2 column elements in a row
```
# 51
## the famous unsqueeze
```python
points.unsqueeze(0) #adds a one element dimension before the lines
points.unsqueeze(1) #adds a one element dimension for each line
points.unsqueeze(3) #adds a one element dimension for each element in its column
```
# 52
* Multiplying Tensors
```python
x = torch.tensor([[1, 2, 3]]) # one line 3 columns
x+10
y = torch.tensor([[10],[20], [30]]) # 3 lines one column
#x*y
y*x # gives the same thing as x*y
```
# 56
* The most complicated Tensor Addition
  * I tested that in Colab
```python
x = torch.tensor([[1,2,3],[4,5,6]])
print(f"{x.shape}") # torch.Size([2, 3])
y = torch.tensor([[[10,20,30]],[[40,50,60]]]) # torch.Size([2, 1, 3])
print(f"{y.shape}")
z = x+y
print(f"{z.size()}") # torch.Size([2, 2, 3])
z
```
* z result is 
```bash
tensor([[[11, 22, 33],
         [14, 25, 36]],

        [[41, 52, 63],
         [44, 55, 66]]])
```
