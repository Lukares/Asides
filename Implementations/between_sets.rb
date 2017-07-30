#!/bin/ruby

def getTotalX(a, b)
    lcm_a = lcmArr(a)
    gcd_b = gcdArr(b)
    total = 0
    temp = lcm_a
    
    while temp <= gcd_b 
       total += 1 if gcd_b % temp == 0
       temp += lcm_a
    end
    total
end

def lcmArr(arr)
    result = arr[0]
    arr.each do |val|
        result = lcm result, val
    end
    result
end

def lcm(a, b)
    (a * b) / (gcd a, b )
end

def gcdArr(arr)
    result = arr[0]
    arr.each do |val|
        result = gcd result, val
    end
    result
end

def gcd(a, b)
    return a if b.zero?
    gcd b, a % b
end

n, m = gets.strip.split(' ')
n = n.to_i
m = m.to_i
a = gets.strip
a = a.split(' ').map(&:to_i)
b = gets.strip
b = b.split(' ').map(&:to_i)
total = getTotalX(a, b)
puts total;
