import Item
from utils import Pair

def calcPrimitivities(item: Item.BaseItem) -> dict[Item.BaseItem, int]:
    """Return Dict<Item, int> of primitive components"""
    if(item.components() == {}):
        return {item : 1} 
    result = {} 
    for comp, cnt in item.components().items():
        innerComponents = calcPrimitivities(comp)

        for innerComp, innerCnt in innerComponents.items():
            if(innerComp in result):
                result[innerComp] += cnt * innerCnt
            else:
                result[innerComp] = cnt * innerCnt                

    return result

def calcChainComponents(item: Item.BaseItem) -> dict[Item.BaseItem, int]:
    """Return Dict<Item, int> of each item in production chain"""
    result = {item : 1} 
    for comp, cnt in item.components().items():
        innerComponents = calcChainComponents(comp)

        for innerComp, innerCnt in innerComponents.items():
            if(innerComp in result): result[innerComp] += cnt * innerCnt
            else: result[innerComp] = cnt * innerCnt                


    return result
