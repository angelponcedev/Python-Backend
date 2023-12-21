def add(number_1, number_2):
    result = number_1 + number_2
    # if we end the  function on this line, then the function could be considered
    # as void, it doesnt return any variable
    print(result)
    # with the keyword return now the function does return a lot of
    # the type of return of the function will be determined directly by
    # the type of the returned variable, in this case would be a number
    return (result)

myvaryable = add(10,20)