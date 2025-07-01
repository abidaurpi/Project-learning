# # name = "Abhishek hossain"

# # for i in name:
# #     print(i, end="")  # print without newline
  
# x="dsdj fflkj"
# # reverse=x[ : : -1]
# # print(reverse)
# reverse=""
# for char in x:
#     reverse= char+ reverse
# print(reverse)
# i= len(x)-1
# reverse=""
# while i>=0:
#     reverse= reverse + x[i]
#     i-=1
# print(reverse)
# a=input("Enter your paragraph:")
# print(a)
# reverse=""
# for i in a:
#     reverse=i+ reverse
# print(reverse)


# a=input("Enter your paragraph:")
# b=a.rsplit()
# l="mew"
# k="sfd"
# print(type(b))
# for i in b:
#     m=i[1: ]
#     print(l+m+i[0]+k,end=" ")

# print("\n")
# x11="is nuefefdf fdgfdgm"
# x12=x11.split()
# print(len(x12))

# while True:
#     a = input("""Do you want to Code or Decode? 
# Write "code" if you want to code.
# Write "decode" if you want to decode: """)

#     if a != "code" and a != "decode":
#         print("Invalid text. Please write it again.")
#     else:
#         if a == "code":
#             m = input("Enter your message: ")
#             print(f"Total words in your message: {len(m.split())}")
#             x = m.split()
#             message = ""

#             for word in x:
#                 if len(word) <= 2:
#                     shortword = word[::-1]
#                     message += shortword + " "
#                 else:
#                     p = "Halum"
#                     q = "mew"
#                     slice1 = word[1:]
#                     coded = p + slice1 + word[0] + q
#                     message += coded + " "
            
#             print("Your coded message:")
#             print(message.strip())

# while True:
#     a = input("""Do you want to Code or Decode? 
# Write "code" if you want to code.
# Write "decode" if you want to decode: """)

#     if a != "code" and a != "decode":
#         print("Invalid text. Please write it again.")
#     else:
#         if a == "code":
#             m = input("Enter your message: ")
#             print(f"Total words in your message: {len(m.split())}")
#             x = m.split()
#             message = ""

#             for i in x:
#                 if len(i) <= 2:
#                     message += i[::-1] + " "
#                 else:
#                     p = "Halum"
#                     q = "mew"
#                     slice1 = i[1:]
#                     coded = p + slice1 + i[0] + q
#                     message += coded + " "

#             message = message.strip()
#             reversed_message = message[::-1]
#             print("Your coded message:")
#             print(reversed_message)

#         elif a == "decode":
#             m = input("Enter your coded message (reversed): ")

#             # Step 1: Reverse back the entire message first
#             original_coded = m[::-1]

#             x = original_coded.split()
#             message = ""

#             for i in x:
#                 if len(i) <= 2:
#                     message += i[::-1] + " "
#                 else:
#                     z = i[5:-3]
#                     decoded = z[-1] + z[:-1]
#                     message += decoded + " "

#             message = message.strip()
#             print("Your decoded message:
