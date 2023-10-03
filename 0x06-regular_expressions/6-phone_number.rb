#!/usr/bin/env ruby
match = ARGV[0].scan(/^\d{10}$/)
string = match.join
puts string
