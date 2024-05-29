import calculations as calcs
import Item

def Test_calcPrimitivities():
    Iron = Item.Item("Iron", 0, {})
    Copper = Item.Item("Copper", 0, {})
    Gear = Item.Item("Gear", 0.5, {Iron: 2})

    Turret = Item.Item("Turret", 10, {Iron: 20, Copper: 20, Gear: 20})
    
    assert calcs.calcPrimitivities(Turret) == {Iron:60, Copper:20}

def Test_calcChainComponents():
    Iron = Item.Item("Iron", 0, {})
    Copper = Item.Item("Copper", 0, {})
    Gear = Item.Item("Gear", 0.5, {Iron: 2})

    Turret = Item.Item("Turret", 10, {Iron: 20, Copper: 20, Gear: 20})
    FastTurret = Item.Item("FastItem", 25, {Turret: 3, Copper: 25}) # for tests only, it doesn't exist in game
    for item, cnt in calcs.calcChainComponents(FastTurret).items():
        print(item.name(), cnt)
    
    
    assert calcs.calcChainComponents(FastTurret) == {FastTurret: 1, Iron:180, Copper:85, Gear : 60, Turret : 3}


Test_calcPrimitivities()
Test_calcChainComponents()
print("ALL TESTS ARE GOOD!")
