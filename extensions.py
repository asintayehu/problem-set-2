def main():
    print(file_identifier(input("File name: ")))

def file_identifier(file_name):
        if file_name.lower().endswith(".gif"):
            return "image/gif"
        elif file_name.lower().endswith("jpg"):
            return "image/jpg"
        elif file_name.lower().endswith("jpeg"):
            return "image/jpeg"
        elif file_name.lower().endswith("png"):
            return "image/png"
        elif file_name.lower().endswith("pdf"):
            return "image/pdf"
        elif file_name.lower().endswith("txt"):
            return "image/txt"
        elif file_name.lower().endswith("zip"):
            return "image/zip"
        else: 
            return "application/octet-stream"

main()