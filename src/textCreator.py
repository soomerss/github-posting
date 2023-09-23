

def create_table_text(pars_datas):
    """
    :param pars_datas: 0:date, 1:image, 2:title, 3:link, 4:contents
    :return:
    """
    mid_format = ''
    for i,data in enumerate(pars_datas):
        img_name = data[1].split('/')[-2]
        print(data)
        format = f"""\
        <td><div>{data[0]}</div><a href="{data[3]}"><img width="100%" src="img/{img_name}.png"/><br/><div>{data[2]}</div></a>
        <div>{data[4][:45]}</div></td>"""
        mid_format += format
        if i % 3 == 2 and i != len(pars_datas)-1:
            mid_format += """</tr><tr>"""
    table_txt = f"""\
    <table>
        <tbody>
            <tr>
            {mid_format}
            </tr>
        </tbody>
    </table>\
    """
    return table_txt

def create_readme(table_txt):
    with open('template/base_template.md','r') as f:
        file = f.readlines()
        final_txt = ''.join(file) + table_txt.strip()
        return final_txt