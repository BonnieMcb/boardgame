import json
import string

file = open("./games/fixtures/games.json", "r")

file_contents = file.read()
file_json = json.loads(file_contents)


def create_item(field_name, item_name, key_id):

    # create new dict
    single_item = {}

    # add primary key
    single_item["pk"] = key_id

    # add model field
    single_item["model"] = "products." + field_name

    # add fields object
    fields = {}
    fields["friendly_name"] = item_name
    # transform contents into db-friendly name
    # code modified from medium.com @ shorturl.at/eCQ02
    text_string = item_name.translate(str.maketrans(
        '', '', string.punctuation))
    safename = text_string.translate(str.maketrans(
        '', '', string.whitespace)).lower()
    fields["name"] = safename

    single_item["fields"] = fields

    return single_item


def map_field_to_indices(file_json, field_name):

    pk = 1
    all_items = []
    unique_item_names = []

    # main loop
    for game_object in file_json:

        target_field = game_object[field_name]  # = whole field contents

        # split into seperate string dict items
        field_list = target_field.split(", ")

        # save list of indices
        item_ids = []

        # put the seperated strings, w/o duplicates, into a new array/list
        for item_name in field_list:

            if item_name not in unique_item_names:

                single_item = create_item(field_name, item_name, pk)
                all_items.append(single_item)

                # increment primary key for next insertion
                pk += 1

                unique_item_names.append(item_name)

            # find matching index, adding 1 as pk starts at 1
            index = unique_item_names.index(item_name) + 1
            item_ids.append(index)

        # add category id field
        game_object[field_name + "_id"] = item_ids

        # delete category field
        del game_object[field_name]

        # add model field
        game_object["model"] = "products.product"

    # write the new file
    map_file = open("./games/fixtures/game_" + field_name + ".json", 'w')
    map_file.write(json.dumps(all_items))
    map_file.close()

    return file_json


# map mechanics, and write mechanics file
new_json = map_field_to_indices(file_json, "mechanic")

# map categories, and write categories file
out_json = map_field_to_indices(new_json, "category")

# write the newly-converted games file
t = open("./games/fixtures/games_converted.json", 'w')
t.write(json.dumps(out_json))
t.close()
