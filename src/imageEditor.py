from PIL import Image
import requests
from io import BytesIO


max_width = 800  # 원하는 최대 너비
max_height = 600  # 원하는 최대 높이
def create_img_url(pars_datas):
    img_urls = []
    for i in pars_datas:
        img_urls.append(i[1])
    return img_urls


def image_edior(img_url):
    img_name = img_url.split('/')[-2]
    image_content = requests.get(img_url).content
    image = Image.open(BytesIO(image_content))
    image.thumbnail((max_width, max_height))
    output_buffer = BytesIO()
    image.save(output_buffer, format="png")
    resized_image_content = output_buffer.getvalue()
    print(f'{img_name}_upload 완료')
    return img_name, resized_image_content
