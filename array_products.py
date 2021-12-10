def arrayOfProducts(array):
    # Write your code here.
    products = [1 for _ in range(len(array))]

    for i in range(len(array)):
        runningProduct = 1

        for j in range(len(array)):
            if i != j:
                runningProduct *= array[j]

        products[i] = runningProduct

    return products


def arrayOfProducts(array):
    # Write your code here.
    products = [1 for _ in range(len(array))]
    leftProducts = [1 for _ in range(len(array))]
    rightProducts = [1 for _ in range(len(array))]

    leftRunningProduct = 1
    for i in range(len(array)):
        products[i] = leftRunningProduct
        leftRunningProduct *= array[i]

    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        products[i] *= rightRunningProduct
        rightRunningProduct *= array[i]

    return products
