#!/bin/ruby

def divisibleSumPairs(n, k, ar)
    if ar.length === 1 
        return 0
    end
    
    result = 0
    root = ar[0]
    temp = ar[1..n]
    temp.each do |val|
        result += 1 if (val + root) % k === 0
    end
    result + divisibleSumPairs(n, k, ar[1..n])
end

n, k = gets.strip.split(' ')
n = n.to_i
k = k.to_i
ar = gets.strip
ar = ar.split(' ').map(&:to_i)
result = divisibleSumPairs(n, k, ar)
puts result;
