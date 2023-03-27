def dice_coefficient(pred, mask):
    smooth = 1e-5 
    pred = pred.view(-1)
    mask = mask.view(-1)
    intersection = (pred * mask).sum()
    union = pred.sum() + mask.sum() + smooth
    accuracy = (2 * intersection + smooth) / union
    print("Intersection:", intersection)
    print("Union:", union)
    print("Dice coefficient:", accuracy)
    return accuracy


import torch
pred = torch.Tensor([0, 1, 1, 0, 1])
print(pred.shape)
mask = torch.Tensor([1, 1, 0, 1, 0])
print(mask.shape)
dice_coefficient(pred, mask)
