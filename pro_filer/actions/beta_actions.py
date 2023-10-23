"""Arquivo que estudantes devem editar"""


def show_deepest_file(context):
    if not context["all_files"]:
        print("No files found")
    else:
        index = 0
        length = 0
        for i, item in enumerate(context["all_files"]):
            if len(item.split("/")) > length:
                length = len(item.split("/"))
                index = i
        print(f"Deepest file: {context['all_files'][index]}")


def find_file_by_name(context, search_term, case_sensitive=True):
    if not search_term:
        return []

    found_files = []

    for path in context["all_files"]:
        file_name = path.split("/")[-1]

        if not case_sensitive:
            file_name.lower()
            search_term.lower()

        if search_term in file_name:
            found_files.append(path)

    return found_files
