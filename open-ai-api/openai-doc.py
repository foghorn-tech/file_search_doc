import os
from bs4 import BeautifulSoup


def extract_text_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    for section in soup.find_all('div', class_='section md'):
        title = section.find('h2', class_="anchor-heading").get_text(strip=True,separator='_').strip()
        title = title.replace(' ', '_')
        if title.endswith('_Beta'):
            title = title.replace('_Beta', '')
        if title.endswith('_Legacy'):
            title = title.replace('_Legacy', '')
        text = extract_text_from_section(section)
        # create output
        os.makedirs('output', exist_ok=True)
        #save text to markdown file
        with open(f'output/OpenAI_{title}.md', 'w') as f:
            f.write(text)
    for section in soup.find_all('div', class_='section endpoint'):
        title = section.find('h2', class_="anchor-heading").get_text(strip=True,separator='_').strip()
        title = title.replace(' ', '_')
        if title.endswith('_Beta'):
            title = title.replace('_Beta', '')
        if title.endswith('_Legacy'):
            title = title.replace('_Legacy', '')
        text = extract_text_from_section(section)
        # create output
        os.makedirs('output', exist_ok=True)
        #save text to markdown file
        with open(f'output/OpenAI_{title}.md', 'w') as f:
            f.write(text)


## main function
def extract_text_from_section(section):
    text = ''
    for element in section.children:
        _, block = extract_text_from_element(element)
        text += block
    return text

def extract_text_from_element(element):
    text = ''
    origin = ''
    if element.name in ['h2', 'h3', 'p', 'li', 'strong', 'code','span', 'a']:
        if element.name == 'li':
            origin, block = extract_text_from_li(element)
        if element.name == 'a':
            origin, block = extract_text_from_a(element)
        if element.name == 'h2':
            origin, block = extract_text_from_h2(element)
        if element.name == 'h3':
            origin,  block = extract_text_from_h3(element)
        if element.name == 'p':
            origin, block = extract_text_from_p(element)
        if element.name == 'strong':
            origin, block = extract_text_from_strong(element)
        if element.name == 'code':
            origin, block = extract_text_from_code(element)
        if element.name == 'span':
            origin, block = extract_text_from_span(element)
        text += block
    
    if element.name in ['div', 'ol']:
        for child in element.children:
            # process div class = code-smaple
            block = ''
            if child.name == 'div' and 'code-sample' in child['class']:
                _, block = extract_text_from_code_sample(child)
            elif child.name == 'div' and 'param-table' in child['class']:
                _, block = extract_text_from_param_table(child)
            else:
                _, block = extract_text_from_element(child)
            text += block
    # for child in element.descendants:
    #     if child.name :
    #         text += extract_text_from_element(child)
    return origin, text

def extract_text_from_param_table(element):
    ### if have param name 
    if element.find('div', class_='param-name'):
        text = '| Parameter | Type   | Required | Description|\n'
        text += '| --- | --- | --- | --- |\n'
        for child in element.children:
            if child.name == 'div' and 'param-row' in child['class']:
                _, block = extract_text_from_param_row(child)
                text += block
    else :
        text = ''
        for child in element.children:
            _, block = extract_text_from_element(child)
            text += block
    return text, f'{text}'

def extract_text_from_param_row(element):
    name = ''
    dtype = ''
    reqd = 'Optional'
    desc = ''
    for child in element.descendants:
        if child.name == 'div' and 'param-name' in child['class']:
            _, name = extract_text_from_param_name(child)
        elif child.name == 'div' and 'param-desc' in child['class']:
            _, desc = extract_text_from_param_desc(child)
        elif child.name == 'div' and 'param-type' in child['class']:
            _, dtype = extract_text_from_param_type(child)
        elif child.name == 'div' and 'param-reqd' in child['class']:
            _, reqd = extract_text_from_param_reqd(child)
    return '', f'| {name} | {dtype} | {reqd} | {desc}| \n'
    
    

def extract_text_from_param_type(div_element):
    text = div_element.get_text().strip().replace('\n', ' ')
    return text, f'{text}'

def extract_text_from_param_reqd(div_element):
    text = div_element.get_text().strip()
    return text, f'{text}'

def extract_text_from_param_desc(div_element):
    text = div_element.get_text().strip().replace('\n', ' ')
    return text, f'{text}'

def extract_text_from_param_name(div_element):
    text = div_element.get_text().strip()
    return text, f'{text}'

def extract_text_from_a(a_element):
    text = a_element.get_text().strip()
    href = a_element.get('href')
    # process child element <a><h2>text</h2></a>
    for child in a_element.descendants:
        if child.name == 'h2':
            text = child.get_text(strip=True, separator=' ',)            
            return text, f'# [{text}]({href})\n'
        if child.name == 'h3':
            text = child.get_text().strip()
            return text, f'## [{text}]({href})\n'
    return text, f'[{text}]({href})'

def extract_text_from_span(span_element):
    text = span_element.get_text().strip()
    return text, f'{text}'

def extract_text_from_code_sample(a_element):
    alltext = ''
    codetext = ''
    ## fid div class=code-sample-title body-small
    title = a_element.find('div', class_='code-sample-title body-small')
    if title:
        alltext += f'\n**{title.get_text().strip()}**'
        
    first_level_spans = a_element.find_all('span')
    for child in first_level_spans:
        classes = child.get('class', [])
        # filter class="react-syntax-highlighter-line-number 
        if 'react-syntax-highlighter-line-number' in classes:
            continue
        # if <span><span> then skip
        children = child.find_all('span')
        if children.__len__() > 0:
            spanlist = child.find_all('span')
            text = ''
            for span in spanlist:
                text += span.get_text()
                # if endwith \ then \n
            if text.strip() != '':
                codetext += f'{text}'
        if children.__len__() == 0 and child.parent.name != 'span':
            if child.get_text().strip() != '':
                codetext += f'{child.get_text()}'
    return '', alltext + f'\n```python\n{codetext}\n```\n'

def extract_text_from_code(code_element):
    text = code_element.get_text().strip()
    return '', f'`{text}`'

def extract_text_from_li(li_element):
    text = li_element.get_text().strip()
    for sub_element in li_element.children:
        origin, block = extract_text_from_element(sub_element)
        if origin != '':
            text = text.replace(origin, block)
    return text, f'- {text}  \n\n'

def extract_text_from_strong(element):
    text = element.get_text().strip()
    return text, f'**{text}**'

def extract_text_from_h2(element):
    text = element.get_text().strip()
    return text, f'# {text} \n'

def extract_text_from_p(p_element):
    text = p_element.get_text().strip()
    for sub_element in p_element.children:
        origin, block = extract_text_from_element(sub_element)
        if origin != '':
            text = text.replace(origin, block)
    return text, f'{text} \n'

def extract_text_from_h3(element):
    text = element.get_text().strip()
    return text, f'## {text} \n'

with open('open-ai.html') as f:
    html = f.read()
extract_text_from_html(html)