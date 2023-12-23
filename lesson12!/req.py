import requests
import json
import base64
# level 1 Потенциально
# eval
# f -> select
# login password
# @csrf_exempt
# EMAIL_HOST_USER
# EMAIL_HOST_PASSWORD
# MIDDLEWARE_CLASSES

# level 2 уязвимость
# sqlite3
# pickle.load

def GetFilesFromRepo(user,repo,branch):
	url = "https://api.github.com/repos/{}/{}/git/trees/{}"
	responce = requests.get(url.format(user,repo,branch))
	files_list = []
	need_check_trees = []
	if responce.status_code == 200:
		responce_json = responce.json()
		main_tree = responce_json.get("tree",[])
		for item in main_tree:
			if item["type"] == "blob":
				files_list.append(item)
			elif item["type"] == "tree":
				need_check_trees.append(item)
	while len(need_check_trees) != 0:
		temp_responce = requests.get(need_check_trees[0]["url"])
		if responce.status_code == 200:
			temp_responce_json = temp_responce.json()
			temp_tree = temp_responce_json.get("tree",[])
			for item in temp_tree:
				if item["type"] == "blob":
					files_list.append(item)
				elif item["type"] == "tree":
					need_check_trees.append(item)
		need_check_trees.remove(need_check_trees[0])
	return files_list


def CheckFiles(files_list:list,repo_name:str) -> None:
	level1 = []
	level2 = []
	if len(files_list) > 0:
		for file in files_list:
			temp_responce = requests.get(file["url"])
			if temp_responce.status_code == 200:
				temp_responce_json = temp_responce.json()
				if temp_responce_json["content"]:
					if temp_responce_json["encoding"] == "base64":
						encoded_text = base64.b64decode(temp_responce_json["content"])
						decoded_string=""
						try:
							decoded_string = encoded_text.decode('utf-8')
						except Exception as e:
							decoded_string=""
						if decoded_string:
							if decoded_string.find("eval")!=-1:
								level1.append({
									"name":file["path"],
									"url":file["url"],
									"unsafe_code_type":"eval",
								})
							if decoded_string.find("csrf_exempt")!=-1:
								level1.append({
									"name":file["path"],
									"url":file["url"],
									"unsafe_code_type":"csrf_exempt",
								})
							if decoded_string.find("pickle.load")!=-1:
								level2.append({
									"name":file["path"],
									"url":file["url"],
									"unsafe_code_type":"pickle.load",
								})
							if decoded_string.find("sqlite3")!=-1:
								level2.append({
									"name":file["path"],
									"url":file["url"],
									"unsafe_code_type":"sqlite3",
								})
	if len(level1)>0:
		str1=json.dumps(level1,indent=4)
		print(str1)
		with open(f"{repo_name}_level1.txt","w") as file1:
			file1.write(str1)
	if len(level2)>0:
		str2=json.dumps(level2,indent=4)
		print(str2)
		with open(f"{repo_name}_level2.txt","w") as file2:
			file2.write(str2)

# DanteOnline/unsafe-python-code
files_list1 = GetFilesFromRepo("DanteOnline","unsafe-python-code","master")
CheckFiles(files_list1,"DanteOnline_unsafe-python-code_master")
files_list2 = GetFilesFromRepo("windn19","PDLesson012","master")
CheckFiles(files_list2,"windn19_PDLesson012_master")
