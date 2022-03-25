# Ship-Rendezvous-Problem
**1 Introduction**
Your company has been contracted to provide a tool in Python to solve the Ship Rendezvous problem (SRP) to enable a cruise company to minimise the time it takes for the support ship to visit each of the cruise ships in the fleet.
The support ship must visit each of the n cruise ships exactly once and then return to the port (where it started). The support ship travels at a constant speed and changes direction with negligible time. Each cruise ship moves at a constant velocity (i.e. speed and direction). The objective is to minimise the total time taken to visit all the cruise ships (i.e. the time taken to reach the final ship).
This problem is considered in 2-dimensional (2D) Euclidean space. A problem instance is defined by specifying the starting (x, y) coordinates for all ships (including the support ship), the velocity of the support ship, and the velocity of the cruise ships.
Note that it is certain that the SRP has a finite solution if the support ship is faster than all other ships in the fleet. However, it is very likely (but not certain) that the SRP will not have a complete solution (one where all the cruise ships are visited) if one or more of the cruise ships are faster than the support ship.

**2 Your Python Task**
You must implement the greedy heuristic for the 2D Euclidean SRP in Python. Your program must perform the following tasks:
• Read the data from a CSV file (a sample data file is provided on Blackboard sample_srp_data.csv);
• Run the greedy heuristic against the problem instance to obtain a solution;
• Output a list of indexes of unvisited cruise ships, a list of indexes of the visited cruise ships, and the total time to visit all visitable cruise ships.

**3 Greedy Heuristic for the SRP**
A simple way of finding a solution to the SRP is to use a greedy heuristic. The greedy heuristic works as follows
1. For each unvisited cruise ship, calculate how long it would take the support ship to intercept it from the support ship’s current position.
2. Choose the cruise ship, i, which can be reached in the shortest amount of time.
3. Visit cruise ship i and update the positions of the ships in the fleet.
4. Return to 1 if there are any unvisited cruise ships that can be reached by the support ship.
In order to make the heuristic deterministic (i.e. to guarantee the same result each time it is run on the same problem instance) you must specify how ties in Step 2 are broken. If there is a tie, the algorithm should choose to visit the ship with the smallest index (for example, if ships 5 and 7 are tied, ship 5 should be chosen in preference to ship 7).

**4 Technical Appendix**
This appendix contains some technical information to help you solve the proposed problem in the assignment. Please, pay attention to these formula and specifications to ensure that your algorithm produces the correct results.

**Notation**
We denote the starting coordinates of the support ship by (X0; Y0) and its speed by S. We consider the ship i in the task force, where 1 ≤ i ≤ n. We denote its starting coordinates by (xi0; yi0). Its velocity is split into x-component and y-component, vix and viy , respectively. Therefore the
position of ship i at time t > 0 is given by
(xit; yit) = (xi0 + t*vix; yi0 + t*viy)
Note that the speed of ship i (denoted by si) can be obtained from its velocity with the following equation:
si = sqrt(vix^2 + viy^2).

**Calculating intercept times**
To calculate intercept times, it is simplest to update the position of the ships at every step, so that (X0; Y0) represents the current coordinates of the support ship and (xi0; yi0) represents the current coordinates of ship i for 1 ≤ i ≤ n. Then the time, T, taken for the support ship to move from its current position and intercept ship i is found by finding the smallest positive root of the quadratic equation:
a*T^2 + bT + c = 0
where the coefficients are obtained as follows:
a = vix^2 + viy^2 − S^2
b = 2((xi0 − X0)vix + (yi0 − Y0)viy)
c = (xi0 − X0)^2 + (yi0 − Y0)^2.

**Input Data**
The input data for each problem instance will be presented in a comma separated value (CSV) file. A correctly-formatted input file consists of N rows of data, where N ≥ 2. Row 1 corresponds to the support ship, and the remaining rows (i.e. rows 2; ...; N) correspond to the ships to be intercepted. Each row contains five pieces of information in the following order:
• Ship name/description (text).
• Start x-coordinate (decimal number).
• Start y-coordinate (decimal number).
• Velocity x-component (decimal number).
• Velocity y-component (decimal number).
