from mimetypes import guess_type
import sys
# {TODO @ysbavishi} - Determine the type of file
def test_file(file: any):
    """
        Description: The Function tests file based on its extenstion
        Input: file
        Output (bool): 
            - if True file is pdf
            - if False file is not pdf exit process
    """

    mime_type:str = guess_type(file)[0]
    try:
        if mime_type != "application/pdf":
            raise Exception("Not a pdf")
    except Exception as e:
        print(e)
        print(file)
        input("Waiting to press enter")
        sys.exit(1)
    return True
