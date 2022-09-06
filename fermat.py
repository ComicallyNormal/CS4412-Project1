import random
import math

def prime_test(N, k):
	# This is main function, that is connected to the Test button. You don't need to touch it.
	return fermat(N,k), miller_rabin(N,k)


#This function implements modular exponentiation in an iterative form.
def mod_exp(base:int, pow:int, modNum:int)->list:
    bEncodeList = list()
    calcStore = [1] #starts list with 1 at position 0, simulates recursive way of doing things.
    finalCalc:int = 0
    if(pow!=0):
        iteratingNum:int = pow
        #instead of bubbling down we are going to generate an array of ones and zeros that we can mapp to our original list.
        while(iteratingNum!=0):
            bEncodeList.append(iteratingNum%2) #encode whether num is even or odd into parallel list.
            iteratingNum = math.floor(iteratingNum/2)
        bEncodeList.append(0) #deals with base case.
        bEncodeList.reverse() #reversing list simulates bubbling up stack

        #for every value in the encoded list we will perform and store modulus operations based on if it is even or odd
        for x in bEncodeList:
            prevCalc:int = calcStore[len(calcStore)-1] #There is no real reason to store intermediary steps but we are doing it anyway rather than popping.
            if(x == 0):
                modCalculation:int = (prevCalc**2) % modNum
                calcStore.append(modCalculation)
            elif(x == 1):
                modCalculation:int = ((prevCalc**2) * base) % modNum
                calcStore.append(modCalculation)
        finalCalc = calcStore[len(calcStore)-1] #final calculation should be the last bubble up value.
    else:
        finalCalc =1 #if passed in pow is 0

    return finalCalc

#basic probability is (1/2^k)
def fprobability(k):
    probabilityUtil:float = 1/(2**k)
    realProb:float = 1 - probabilityUtil
    return realProb

#probability is 4 times better since it catches 3/4 of the possible bad values, ie risk is 25% of what it was.
def mprobability(k):
    # You will need to implement this function and change the return value.
    origProb:int = fprobability(k)
    difference:float = 1-origProb
    newProb:float = difference * .25 #gets 3/4 of solutions that orig doesn't. error is 25% of what it was.
    realProb:float = 1-newProb

    return realProb


def fermat(primeInput:int,trialLength:int):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
	#
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.
    result:str = 'prime'
    arr:list = list()
    for x in range(trialLength):
        arr.append(random.randint(1,primeInput-1)) #We are pre generating our random numbers
    for randomNum in arr:
       # print(randomNum)
        # fermatNum:int = ((randomNum)**(primeInput-1)) % (primeInput)
        fermatNumWithMod = mod_exp(randomNum,(primeInput-1),primeInput)
        if(fermatNumWithMod != 1):
            result = 'composite'
            return result

    return result

#Miller rabin checks certain composites that are considered prime and catches them.
def miller_rabin(primeInput,trialLength):
    result:str = 'prime'
    arr:list = list()
    for x in range(trialLength):
        arr.append(random.randint(1,primeInput-1)) #We are pre generating our random numbers

    #Copying chunk from fermat as check one.
    for randomNum in arr:
        fermatNumWithMod = mod_exp(randomNum,(primeInput-1),primeInput)
        if(fermatNumWithMod != 1):
            result = 'composite'
            return result


        exponentRunner = primeInput-1
        #checks square root of exponent repeatedly until hitting base case,
        if(exponentRunner%2 ==1):
            if(mod_exp(randomNum,exponentRunner,primeInput)==1):
                result = 'prime'
                return result

        while((exponentRunner)%2==0):
            # print(randomNum,exponentRunner,primeInput)
            numWithMod = mod_exp(randomNum,(exponentRunner),primeInput)
            print(randomNum,exponentRunner,primeInput)
            print(numWithMod)
            if(numWithMod!=1): #if the first non 1 number it hits is not N-1, is composite, otherwise is prime.
                if(numWithMod!=primeInput-1):
                    result = 'composite'
                    return result
                else:
                    result = 'prime'
                    return result
            exponentRunner= math.floor(exponentRunner/2)

    return result
