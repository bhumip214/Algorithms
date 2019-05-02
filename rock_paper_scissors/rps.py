#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  plays = ['rock', 'paper', 'scissors']
  outcomes = []
  def possible_plays(n, result):
    if n == 0:
      return outcomes.append(result)
    else: 
      for i in plays:
        possible_plays(n - 1, result + [i])
  possible_plays(n, [])
  return outcomes


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')