#!/bin/ruby

def solve(year)
    if year == 1918
        "26.09.#{year}"
    elsif year < 1918
        if year % 4 == 0
            "12.09.#{year}" 
        else
            "13.09.#{year}"
        end
    else
        if (year % 4) == 0 && (year % 100) != 0 || (year % 400) == 0
            "12.09.#{year}"
        else
            "13.09.#{year}"
        end
    end
end

year = gets.strip.to_i
result = solve(year)
puts result;
