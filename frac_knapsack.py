def fractionalknapsack(self, W,Items,n):
        # code here
        res = 0.0
        Items.sort(key=lambda x: -x.value/x.weight)
        for item in Items:
            if W >= item.weight:
                W -= item.weight
                res += item.value
            elif W > 0 and W<item.weight:
                res += item.value * W/item.weight
                W = 0
            if W == 0:
                break
        return res
