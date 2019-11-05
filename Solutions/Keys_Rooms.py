'''
There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room. 

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0). 

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.

Example 1:

Input: [[1],[2],[3],[]]
Output: true
Explanation:  
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.
'''

'''
Solution 1: use a stack to keep track of all the rooms we are goign to visit. We use an array of length rooms and set them all to false except for room 0. We enter room 0 and grab all the keys in it and visit all those rooms and mark them true. Put all keys in stack until its empty, in the end we check all the values in our seen array and if they are all true we gucci. 
Time: O(N + M) N being the rooms M being the keys, O(N) space for the array and stack we made
'''


def canVisitAllRooms(self, rooms):
    # initiate array of all false values of length rooms
    seen = [False] * len(rooms)
    seen[0] = True  # mark room 0 as true since we can visit that first
    stack = [0]  # put that room in the stack so we can grab all the keys

    while stack:
        node = stack.pop()
        for key in rooms[node]:  # grab all keys in room
            if not seen[key]:  # mark true if we havent visited that room already
                seen[key] = True

                # add key to stack so we can check that room as well
                stack.append(key)

    return all(seen)  # all returns true if everything in the array is true
