#!/usr/bin/env ruby
match = ARGV[0].scan(/hbt{2,5}n/)
string = match.join
puts string
