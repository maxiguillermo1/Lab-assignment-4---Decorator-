import asyncio

# define asynchronous function factorial
async def factorial(name, number):

    # initialize the factorial answer to 1 
    ans = 1
    
    # loop from 1 to number + 1 sice python's for loop excludes the last number
    for i in range(1, number + 1):
        # display taks name, currently factorial value
        # current loop variable
        
        print(f"Task {name}: Computer factorial({number}), currently i = {i}...")
        
        
        ans *= i
        
        # delay 1 second, this delay will allow other concurrent tasks to run while we are sleeping
        await asyncio.sleep(1)
    
    # display the task name and the final factorial value
    print(f"Task {name}: factorial({number}) = {ans}")
    # return the final factorial value
    return ans

async def main():
    # scheduel tbree calls "factoral" concurrently 
    # using asyncio.gather will initialize all takss that will return an object for each task made (task A, Task B, Task C)
    batch = asyncio.gather(
        factorial("A", 3),
        factorial("B",4), 
        factorial("C",5)
                          ) 
    
    
    funcA,funcB,funcC = await batch
    
    print([funcA,funcB,funcC])




if __name__ == "__main__":
    
    # use asyncio to run the main function 
    asyncio.run(main())
