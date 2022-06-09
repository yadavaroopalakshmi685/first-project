str1=input("Enter the first string: ")
str2=input("Enter the second string: ")
list1=list(str1.lower())
list2=list(str2.lower())
list1.sort()
list2.sort()
if list1==list2:
	print("Both the words are anagrams to each other")
else:
	print("Not a anagram")

