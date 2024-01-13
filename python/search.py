import os

def search_files(search_file_name):
    try:
        current_directory = os.getcwd()

        files = os.listdir(current_directory)

        search_results = []

        for file in files:
            if search_file_name.lower() in file.lower():
                search_results.append(file)

        if search_results:
            print(f"'{current_directory}'폴더에서 '{search_file_name}'을(를) 포함하는 파일:")
            for result in search_results:
                print(result)
        else:
            print("파일이 없습니다.")
    except Exception as e:
        print(f"에러 발생: {e}")

if __name__ == "__main__":

    search_file_name = input("검색할 파일을 입력해주세요: ")
    search_files(search_file_name)
