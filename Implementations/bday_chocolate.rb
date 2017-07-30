#!/bin/ruby

def solve(n, s, d, m)
    fits = (n - m ) / m
    extra = n % m
    sets = 1 + (fits * m) + extra
    min = 0
    max = m
    counter = 0
    
    sets.times do
        temp = 0
        s[min...max].each do |val|
            temp += val
        end
        counter += 1 if temp == d
        min += 1
        max += 1
    end
    counter
end

n = gets.strip.to_i
s = gets.strip
s = s.split(' ').map(&:to_i)
d, m = gets.strip.split(' ')
d = d.to_i
m = m.to_i
result = solve(n, s, d, m)
puts result;
