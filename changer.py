import re, os

posibs = os.listdir('backgrounds')

def rewrite_background(new_bg, file_path='css/background.css'):
    img_path = f"../backgrounds/{new_bg}"
    pattern = r"url\(['\"]?(.*?)['\"]?\)"

    with open(file_path, 'r') as file:
        html_content = file.read()

    found_url = re.findall(pattern, html_content)[0]

    old_property = f"background: url('{found_url}');"
    new_property = f"background: url('{img_path}');"

    new_html = html_content.replace(old_property, new_property)

    with open(file_path, 'w') as file:
        file.write(new_html)

if __name__ == '__main__':
    for i, posib in enumerate(posibs):
        print(i, posib)

    selected_i = int(input('choose background, enter index: '))

    if 0 <= selected_i < len(posibs):
        selected_item = posibs[selected_i]

    else:
        raise IndexError('Incorrect index provided')

    rewrite_background(selected_item)

    print('succes')