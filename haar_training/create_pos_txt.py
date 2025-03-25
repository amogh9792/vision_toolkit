import os
import re
import xml.etree.ElementTree as ET

annotations_folder = 'annotations'
images_folder = 'positives'
output_file = 'info.dat'

def sanitize_filename(filename):
    # Replace spaces with underscores and remove () and other special chars
    filename = filename.replace(' ', '_')
    filename = re.sub(r'[()\[\]{}]', '', filename)
    return filename

def parse_annotation(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    boxes = []
    for obj in root.findall('object'):
        bbox = obj.find('bndbox')
        xmin = int(float(bbox.find('xmin').text))
        ymin = int(float(bbox.find('ymin').text))
        xmax = int(float(bbox.find('xmax').text))
        ymax = int(float(bbox.find('ymax').text))
        width = xmax - xmin
        height = ymax - ymin
        boxes.append((xmin, ymin, width, height))
    return boxes

def create_info_dat():
    with open(output_file, 'w') as f:
        for xml_file in os.listdir(annotations_folder):
            if not xml_file.endswith('.xml'):
                continue
            image_filename = xml_file.replace('.xml', '.jpg')
            safe_image_filename = sanitize_filename(image_filename)

            original_path = os.path.join(images_folder, image_filename)
            safe_path = os.path.join(images_folder, safe_image_filename)

            # Rename the file on disk if needed
            if image_filename != safe_image_filename and os.path.exists(original_path):
                os.rename(original_path, safe_path)
                print(f"[RENAME] {image_filename} -> {safe_image_filename}")

            full_xml_path = os.path.join(annotations_folder, xml_file)
            boxes = parse_annotation(full_xml_path)
            if not boxes:
                continue

            # Always write the sanitized filename
            relative_image_path = f"{images_folder}/{safe_image_filename}".replace('\\', '/')
            line = f"{relative_image_path} {len(boxes)}"
            for (x, y, w, h) in boxes:
                line += f" {x} {y} {w} {h}"
            f.write(line + "\n")
    print(f"[INFO] info.dat generated successfully with sanitized paths")

if __name__ == "__main__":
    create_info_dat()
