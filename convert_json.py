import json

file_name = './out.json'
class_list = {'needle':0}

with open(file_name) as f:
    js = json.load(f)

    for k, v in js['assets'].items():

        fileno = v["asset"]["name"].split(".")[0]

        line = {}
        line['file'] = fileno + '.jpg'
        line['image_size'] = [{
            'width':v["asset"]["size"]["width"],
            'height':v["asset"]["size"]["height"],
            'depth':3
        }]

        line['annotations'] = []

        for annotation in v["regions"]:

            line['annotations'].append(
                {
                    'class_id':class_list[annotation['tags'][0]],
                    'top':annotation['boundingBox']["top"],
                    'left':annotation['boundingBox']["left"],
                    'width':annotation['boundingBox']["width"],
                    'height':annotation['boundingBox']["height"]
                }
            )

        line['categories'] = []

        for name, class_id in class_list.items():

            line['categories'].append(
                {
                    'class_id':class_id,
                    'name':name
                }
            )

        f = open('./json/' + fileno + '.json', 'w')
        json.dump(line, f)
        f.close()