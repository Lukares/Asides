#!/bin/ruby

def getRecord(s)
    max = min = s[0]
    maxCount = minCount = 0
    s.each do |val| 
        if val > max
            max = val 
            maxCount += 1
        elsif val < min
            min = val
            minCount += 1
        end
    end
    [maxCount, minCount]
end

n = gets.strip.to_i
s = gets.strip
s = s.split(' ').map(&:to_i)
result = getRecord(s)
print result.join(" ")
