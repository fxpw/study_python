str_for_parse1 = str(input("vvedite nums1 whit / separator "))
m_list1 = list(str_for_parse1.split("/"))

str_for_parse2 = str(input("vvedite nums2 whit / separator "))
m_list2 = list(str_for_parse2.split("/"))


list_for_out = []

for t in m_list1:
    if t not in m_list2:
        list_for_out.append(t)

print(",".join(list_for_out))
	