# Optimal Ignition Point for Minimum Burn Time in a Connected Figure of Matches

## Problem description
Given a set of matches arranged on a grid, where each match connects two points, we need to find the optimal point of ignition to ensure the entire connected structure burns in the shortest possible time. Matches can burn from either end, and fire spreads at a constant rate along each matchstick. Each match has a specified burn time when ignited from one end.
The input is provided in a text file with the following format:
- The first line contains an integer n, the number of matches.
- Each subsequent line describes a match with five integers: x1, y1, x2, y2, t, where:
  - (x1, y1) and (x2, y2) are the coordinates of the match's endpoints.
  - t is the time taken for the match to burn completely when ignited from one end.
 The objective is to find the ignition point that results in the shortest burn time for the entire structure.
