from PIL import Image


def fix_img(img: str, num_color: int) -> None:
    offset = 50
    if num_color == 0:
        coordinates = (offset, 0, img.width, img.height)
        coordinates2 = (0, 0, img.width - offset, img.height)
    elif num_color == 1:
        coordinates = (offset/2, 0, img.width-(offset/2), img.height)
        cropped = img.crop(coordinates)
        return cropped
    elif num_color == 2:
        coordinates = (0, 0, img.width - offset, img.height)
        coordinates2 = (offset, 0, img.width, img.height)
    cropped = img.crop(coordinates)
    cropped2 = img.crop(coordinates2)
    finally_img = Image.blend(cropped, cropped2, 0.1)
    return finally_img


def image_merge(rgb_image: tuple) -> None:
    new_image = Image.merge('RGB', (rgb_image))
    new_image.save('result.jpg', format='JPEG')
    new_image.thumbnail((80, 80))
    new_image.save('result_80px.jpg', format='JPEG')


def main():
    image = Image.open('example.jpg')
    red, green, blue = image.split()
    new_tuple = (
        fix_img(red, 0),
        fix_img(green, 1),
        fix_img(blue, 2),
    )
    image_merge(new_tuple)

if __name__ == '__main__':
    main()
