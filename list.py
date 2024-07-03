Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nums = [25, 12, 36, 95, 14]
>>> nums
[25, 12, 36, 95, 14]
>>> nums[0]
25
>>> nums[4]
14
>>> nums[2: ]
[36, 95, 14]
>>> nums[-1]
14
>>> nums[-5]
25
>>> names = ['navin', 'kiran', 'john']
>>> names
['navin', 'kiran', 'john']
>>> values = [9.5, 'Navin', 25]
>>> mil = [nums, names]
>>> mil
[[25, 12, 36, 95, 14], ['navin', 'kiran', 'john']]
>>> nums.append(45)
>>> nums
[25, 12, 36, 95, 14, 45]
>>> nums.insert(2,77)
>>> nums
[25, 12, 77, 36, 95, 14, 45]
>>> nums.pop(1)
12
>>> nums
[25, 77, 36, 95, 14, 45]
>>> nums.pop()
45
>>> nums
[25, 77, 36, 95, 14]
>>> del nums[2:]
>>> nums
[25, 77]
