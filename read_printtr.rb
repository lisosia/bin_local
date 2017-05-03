#!/usr/bin/env ruby

require "pry"

file = "./test.printtr0"
if ARGV.size > 0
  file = ARGV[0]
end

samples = File.open(file, "r").read.split("-----------------------------------------------")
samples.map! do |str|
  ls = str.split("\n").reject{|l| l == ""}
  raise unless /monte carlo index =\s+[0-9]+/ =~ ls[0]
  seed = ls[0].split()[4].to_i
  raise if seed == 0
  head = ls[1].split
  data = ls[2 .. -1].map!{|l| l.split}
  # STDERR.puts seed, head.join(" ")
  {seed: seed,  head: head, data: data}
end

count = 0
for s in samples
  p s[:head].size
  p s[:seed]
  vout1 = s[:data].last[4].to_f
  vout2 = s[:data].last[5].to_f
  STDERR.puts s[:head][4] , s[:head][5]
  STDERR.puts vout1 ,vout2
  raise if vout1 == 0 or vout2 == 0 # to_i failed
  if vout1 > vout2
    count += 1
  end
end

puts "vout1>vount2(at_last_time): #{count} / #{samples.size}"
# binding.pry
